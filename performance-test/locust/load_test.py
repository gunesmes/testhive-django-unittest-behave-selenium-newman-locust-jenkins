#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task
import uuid


class UserBehaviour(TaskSet):
    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def test_ping(self):
        self.client.get('/',
                        name="index"
                        )

    @task(5)
    def test_get_users(self):
        self.client.get('/api/users',
                        name="api/users"
                        )

    @task(5)
    def test_get_user(self):
        self.client.get('/api/user?username=testusername1',
                        name="api/user"
                        )

    @task(1)
    def test_register(self):
        username = uuid.uuid4().hex[3:]
        email = username + '@test.com'
        self.client.post('/api/register',
                         data={"username": username,
                               'email': email,
                               'birthday': '2001-09-03',
                               'address': 'test address for load test, Istanbul/Turkey',
                               'client': 'app'},
                         name="api/register"
                         )


class User(HttpLocust):
    host = "http://localhost:8001"

    task_set = UserBehaviour
    # for user behaviour
    # we can assume that they wait 0.3 to 0.5 seconds on a page
    min_wait = 300
    max_wait = 500
