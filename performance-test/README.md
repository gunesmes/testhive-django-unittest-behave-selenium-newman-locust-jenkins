# Locust
## Docker-Locust
Run Locust in Dockers for performance testing.

Locust + Docker + Python + Master + Slave


### Write required python libraries inside the requirements.txt

In Dockerfile there is a step at the end of the process to install required libraries defined in the requirements.txt so you must add all your requirements inside this file as in following format:

    pyquery
    requests

### Get the Image
    docker pull gunesmes/docker-locust

### Run the image with executing your tests
    cp /Users/mesut/.jenkins/workspace/testhive-sample-pipeline/performance-test/load_test.py . 
    docker run --network host --rm --name locust -v $PWD:/locust gunesmes/docker-locust -f /locust/load_test.py --clients=10 --hatch-rate=1 --run-time=30 --no-web --only-summary --csv=load_test_result


# K6
Since the K6 has embed treshold feature there is no need to evaluate the result. For load test, the number of the virtual user (vus) should be stay constant, but for the spike test, the number of the virtual user should be increased suddenly and should be decreased suddenly.

## Run Load Test with K6
```bash
docker run --network host -i loadimpact/k6 run - \
	--vus 10 \
	--duration 30s \
	--out influxdb=http://localhost:8086/testrisk \
	<load_test-k6.js
```

## Run Spike Test with K6
```bash
docker run --network host -i loadimpact/k6 run - \
	--vus 10 \
	--stage 5s:10,5m:20,10s:5 \
	--out influxdb=http://localhost:8086/testrisk \
	<load_test-k6.js
```
