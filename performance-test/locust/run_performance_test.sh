docker run --network host --rm --name locust -v $PWD:/locust gunesmes/docker-locust -f /locust/load_test.py --clients=10 --hatch-rate=1 --run-time=30 --no-web --only-summary --csv=load_test_result

