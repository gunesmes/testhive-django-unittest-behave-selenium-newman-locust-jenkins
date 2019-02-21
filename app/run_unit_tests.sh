#!/usr/bin/env bash
# If django_nose coverage not used, this is to run each unit test separately

for module in \
	"models" \
	"forms" \
	"views"
	do
	echo -e "\n - ${module} is testing . . . \n"
    docker exec -it testhive-app bash -c "cd /code && python manage.py test tests.test_${module} -v 2"
done

nohup docker system prune -f &