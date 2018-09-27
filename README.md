# Project Structure

* **app**               --> Application develop with Django. There is readme about running and unittest.
* **app/src/tests**     --> Unit test folder. You find more information about it in README in app.
* **service-test**      --> Service tests are prepeared in Postman and created a collection. For more info, there is a README file in the project.
* **web-automation**    --> For web automation project, test cases are written in BBD with Python so Behave as a framework is used for the project. For more information and how to run in docker, you can README file in the project.
* **performance-test**  --> Locust is used for performance testing. Performance test should be run against to test environment so need to set the host in the script.

# CI
For running all the tests as a stage in development process a development pipeline can be preperad in Jenkins. jenkins can be run in a docker but the data should be mounted by `v` for persistency. The following command can be run. Username/Password: `admin/admin`

```bash
docker run -d -v data-jenkins:/var/jenkins_home:z -p 8080:8080 -p 50000:50000 --name map-jenkins jenkins/jenkins:lts
```

A simple pipeline should be look like this. Tests are 
```bash
node(build-slave) {
   stage('Preparation') {
      git 'https://github.com/gunesmes/code-run-test-automation-ci.git'
   }
   stage('Build') {
       sh 'cd /var/jenkins_home/workspace/mapillary/app'
       sh 'docker-compose up'
   }
   stage('Unit Test') {
       sh 'cd /var/jenkins_home/workspace/mapillary/app/src/test'
       sh 'bash run_unit_tests.sh'
   }
   stage('Service Test') {
       sh 'cd /var/jenkins_home/workspace/mapillary/service-test' 
       sh 'bash service_tests.sh'
   }
   stage('UI Test') {
       sh 'cd /var/jenkins_home/workspace/mapillary/web-automation'
       sh 'bash run_web_automation.sh'
   }
   stage('Test Deployment') {
   		 sh 'echo live deployment started'
   }
   stage('Performance Test') {
       sh 'bash run_performance_test.sh'
   }
   stage('Live Deployment') {
   		 sh 'echo test deployment started'
   }
}
```


![Jenkins Sample Pipeline](jenkins-sample-pipeline.png)
