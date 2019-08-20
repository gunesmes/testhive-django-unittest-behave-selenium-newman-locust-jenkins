# docker-locust
Run Locust in Dockers for performance testing.

Locust + Docker + Python + Master + Slave


## write required python libraries inside the requirements.txt

In Dockerfile there is a step at the end of the process to install required libraries defined in the requirements.txt so you must add all your requirements inside this file as in following format:

    pyquery
    requests

## get the image
    docker pull gunesmes/docker-locust

## run the image with executing your tests
    cp /Users/mesut/.jenkins/workspace/testhive-sample-pipeline/performance-test/load_test.py . 
    docker run --network host --rm --name locust -v $PWD:/locust gunesmes/docker-locust -f /locust/load_test.py --clients=10 --hatch-rate=1 --run-time=30 --no-web --only-summary --csv=load_test_result



