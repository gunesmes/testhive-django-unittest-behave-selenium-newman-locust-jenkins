docker run --network host -i loadimpact/k6 run - \
	--vus 10 \
	--duration 10s \
	--out influxdb=http://localhost:8086/testrisk \
	<load_test-k6.js