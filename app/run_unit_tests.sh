#!/usr/bin/env bash


for module in \
	"models" \
	"views" \
	"forms"
	do
    docker exec -it app_web_1  bash -c "cd /code && python  manage.py test src.tests.test_${module} -v 0"
done

nohup docker system prune -f &