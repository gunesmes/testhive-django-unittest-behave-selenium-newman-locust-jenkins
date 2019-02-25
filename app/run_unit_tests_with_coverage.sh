#!/usr/bin/env bash
# If django_nose coverage not used, this is to run each unit test separately

docker exec testhive-app bash -c "cd /code && python manage.py test -v 2"

nohup docker system prune -f &