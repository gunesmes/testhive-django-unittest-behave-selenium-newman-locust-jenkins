docker run --network host -i loadimpact/k6 run - \
	--vus 10 \
	--duration 120s \
	--out influxdb=http://aadmin:admin@localhost:8086/testrisk \
	<load_test-k6.js