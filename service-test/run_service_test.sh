#!/bin/bash

# need to restore initial test data
bash restore_db.sh $1

echo -e "\n\n * * * * * * *  SERVICE TEST STARTED  * * * * * * *\n"

# remove old reports
rm newman/*.html 2>/dev/null

# get custom docker image
docker pull gunesmes/newman-postman-html-report

# run postman collection in newman with local installation and collection json
#newman run blog-sample-service.postman_collection.json -e blog-local.postman_environment.json --reporters cli,html --reporter-html-template report-template.hbs

# run postman collection in newman with local installation and collection url
#newman run https://www.getpostman.com/collections/ac3d0d9bbd8ae1bcfe5d -e blog-local.postman_environment.json --reporters cli,html --reporter-html-template report-template.hbs

# run postman collection in newman with docker image
## html result
# docker run --network host -v $PWD:/newman gunesmes/newman-postman-html-report run blog-sample-service.postman_collection.json -e blog-local.postman_environment.json --reporters cli,html --reporter-html-template report-template.hbs

## xml result
docker run --platform linux/amd64 --network host -v $PWD:/newman gunesmes/newman-postman-html-report run blog-sample-service.postman_collection.json -e blog-local.postman_environment.json --reporters junit --reporter-junit-export newman/service-test-report.xml
