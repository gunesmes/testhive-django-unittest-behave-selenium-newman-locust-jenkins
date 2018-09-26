#!/bin/bash

# need to restore initial test data
bash restore_db.sh $1

echo -e "\n\n * * * * * * *  SERVICE TEST STARTED  * * * * * * *\n"

# remove old reports
rm newman/*.html 2>/dev/null

# run postman collection in newman with local installtion
#newman run https://www.getpostman.com/collections/99ff74d42bbbcfcdc1e7 --reporters cli,html --reporter-html-template report-template.hbs

# run postman collection in newman with docker image
docker pull gunesmes/newman-postman-html-report
docker run --network host -v $PWD:/newman gunesmes/newman-postman-html-report run https://www.getpostman.com/collections/99ff74d42bbbcfcdc1e7 --reporters cli,html --reporter-html-template report-template.hbs