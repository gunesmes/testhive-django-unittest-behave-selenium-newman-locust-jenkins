#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery
from locust import events
from locust.stats import *
import random
import requests
import sys


# sys.settrace
sys.setrecursionlimit(10000000)

class UserBehaviour(TaskSet):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36'
    links = []


    def get_urls(self, url, locator, key):
        re = self.client.get("/", headers = { 'User-Agent': self.user_agent })
        print("lson")
        print(re.content)

        # will parse the html and get the valid and host specific links 
        pq = PyQuery(re.content)
        link_elements = pq(locator)
        for link in link_elements:
            if key in link.attrib and "http" not in link.attrib[key] and "javascript" not in link.attrib[key] and "/detay" not in link.attrib[key]:
                self.links.append(link.attrib[key].strip(" "))

        return self.links


    def on_start(self):
        self.links 	= self.get_urls("/", "a", "href")


    @task(1)
    def test_links(self):
        # this is a task to run performance testing
        # we will send http request to the url taken from the main page of you provided as host 
        try:
            url = random.choice(self.links)
            self.client.get(url, headers = { "User-Agent": self.user_agent})
        except IndexError:
            pass

    def on_stop(self):
        del links

class User(HttpLocust):
    host = "http://map-test.dev"

    task_set = UserBehaviour
    # for user behaviour
    # we can assume that they wait 0.3 to 0.5 seconds on a page
    min_wait = 300
    max_wait = 500

