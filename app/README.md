
# Runnign the APP
I have used the Docker as much as possible. For the application, everything is packed in `docker-compose.yml` so you 
run the app with the following command, ensure that you have Docker and Docker deamon is running:
```bash
docker-compose up
```

# Running the Unit Tests
In `src/tests` folder, there are unit test modules written against the `views`, `models` and `forms`. 
```bash
tests
├── test_forms.py
├── test_models.py
└── test_views.py

```

These are 
`django.test` so they can be run by `manage.py` with following command:
```bash
python  manage.py test src.tests.test_models
```

Since the project is running in `Docker`, we need to run them inside Docker instance. We can use the following command
to run them in running docker instance for application.
```bash
docker exec -it app_web_1  bash -c "cd /code && python  manage.py test src.tests.test_models"
```


# Running Unit Test on CI
For CI, whole tests can be by run `bash run_unit_test.sh`
```bash
~/P/p/m/app (master ⚡☡) bash run_unit_tests.sh
System check identified no issues (0 silenced).
----------------------------------------------------------------------
Ran 2 tests in 0.007s

OK
System check identified no issues (0 silenced).
----------------------------------------------------------------------
Ran 4 tests in 0.037s

OK
System check identified no issues (0 silenced).
----------------------------------------------------------------------
Ran 2 tests in 0.012s

OK
``` 


