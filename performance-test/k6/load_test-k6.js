// cat script.js
import {
    check,
    sleep,
    group
} from "k6";
import {
    parseHTML
} from "k6/html";
import http from "k6/http";
import {
    Trend,
    Rate,
    Counter,
    Gauge
} from "k6/metrics";


let valid_urls = ["/", "/api/users", "/api/user?username=testusername1"]
let host = "http://0.0.0.0:8001"

export let TrendRTTGet = new Trend("RTTGet");
export let TrendRTTPost = new Trend("RTTPost");
export let options = {
    thresholds: {
        "RTTGet": [
            "p(95)<800",
            "p(90)<700",
            "max<900",
            "avg<600",
            "med<600",
            "min<100",
        ],
        "RTTPost": [
            "p(95)<850",
            "p(90)<700",
            "max<900",
            "avg<600",
            "med<600",
            "min<200",
        ]
    },
    // scenarios: {
    //     constant_request_rate: {
    //         executor: 'constant-arrival-rate',
    //         rate: 100,
    //         timeUnit: '1s', // 10 iterations per second, i.e. 10 RPS
    //         duration: '2m',
    //         preAllocatedVUs: 10000, // how large the initial pool of VUs would be
    //         maxVUs: 20000, // if the preAllocatedVUs are not enough, we can initialize more
    //     },
    // },

};


export function setup() {
    // pass this
}


export default function() {
    group("GET", function() {
        var url = valid_urls[Math.floor(Math.random() * valid_urls.length)];
        var link = host + url;
        console.log(link);

        let res = http.get(link);
        check(res, {
            "status is 200": (r) => r.status === 200
        });
        TrendRTTGet.add(res.timings.duration);

    });

    group("POST", function() {
        var url = "/api/register/"
        var link = host + url
        var username = (new Date()).getTime().toString(36) + Math.floor(Math.random() * 100000000).toString()
        console.log(link + username);

        let formData = {
            username: username,
            email: username + '@gmail.com',
            birthday: '2001-01-02',
            address: 'test address is going here'
        };

        let res = http.post(link, formData);
        check(res, {
            "status is 201 or 202": (r) => [201, 202].includes(r.status),
        });
        TrendRTTPost.add(res.timings.duration);

    });

    sleep(3);
};


export function teardown() {
    // pass this
}