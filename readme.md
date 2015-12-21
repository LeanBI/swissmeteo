# swissmeteo
fetch Data from Swiss Opendata Meteo Service, and upload it to S3 compatible Storage (run in Docker)

More info by [LeanBI](http://www.leanbi.ch)

##Usage

- Build Docker Image : docker build -t yourBaseName:andTag .


- Run : 
```shell
docker run \ 
	-e REST_URL=http://data.netcetera.com/smn/smn \
	-e REST_POLLING_INTERVAL=10 \
	-e S3_HOST=s3-us-west-2.amazonaws.com \
	-e S3_PORT=443 \
	-e S3_ACCESS_KEY=mykey \
	-e S3_SECRET_KEY=mypassword \
	-e S3_BUCKET=mybucket \
	-e S3_KEY=swissmeteo/data
	yourBaseName:andTag
```