#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 17, 2015

@author: Sébastien Brennion
'''
import urllib
import os
import json
from dateutil import parser, tz
import time
import logging
import sys

class swissmeteo():
    def __init__(self,**kwargs):
        self.last_update=None
        self.url=os.environ["REST_URL"]
        self.polling_interval=int(os.environ["REST_POLLING_INTERVAL"])
    def request(self):

        while True :
            response = urllib.urlopen(self.url)
            response_string=response.read()
            response_json= json.loads(response_string)
            
            response_date_string=response_json[0]["dateTime"]
            
            if response_date_string==self.last_update :
                time.sleep(30)
                logger.info("request result has same timestamp=%s --> wainting..." % response_date_string)
                next()
            
            response_date=parser.parse(response_date_string).astimezone(tz.tzlocal())
            logger.info("received answer with timestamp=%s" %   response_date_string)
            self.store(response_date_string,response_string)
            logger.info("waiting next request for %s seconds" % self.polling_interval)
            time.sleep(self.polling_interval)
            
            
    
    def store(self,tstamp,mystring):
        fileName=os.environ["S3_KEY"] + "-" + tstamp + ".txt" 
        object_storage().store(os.environ["S3_BUCKET"],fileName,mystring)


class object_storage():
    def __init__(self):
        import boto
        import boto.s3.connection
        
        self.conn= boto.connect_s3(aws_access_key_id=os.environ["S3_ACCESS_KEY"], 
                                   aws_secret_access_key=os.environ["S3_SECRET_KEY"],
                                   host=os.environ["S3_HOST"],
                                   port=int(os.environ["S3_PORT"]),
                                   calling_format=boto.s3.connection.OrdinaryCallingFormat())
        
    def store(self,myBucket,mykey,myString):
        bucket=self.conn.get_bucket(myBucket)
        key = bucket.new_key(mykey)
        key.set_contents_from_string(myString)
        logger.info("Data stored in %s"  % myBucket + "/" + mykey)



if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    swissmeteo().request()
    
    
    
    
    
    
    
    
    