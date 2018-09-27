# docker-locust
Run Locust in Dockers for performance testing.

Locust + Docker + Python + Master + Slave

## get the image
    docker pull gunesmes/docker-locust

## run the image with executing your tests
    docker run -p 8089:8089 --rm --name locust -v $PWD:/locust gunesmes/docker-locust -f /locust web_performance.py

## write required python libraries inside the requirements.txt

In Dockerfile there is a step at the end of the process to install required libraries defined in the requirements.txt so you must add all your requirements inside this file as in following format:

  pyquery
  requests

## simpliest running the tags in run.sh

Ensure that you are in the project folder, and the path in run.py is correct




