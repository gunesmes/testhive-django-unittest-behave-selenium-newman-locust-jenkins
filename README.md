
docker run -d -v databas-jenkins:/var/jenkins_home:z -p 8080:8080 -p 8001:8001 -p 50000:50000 --name myjenkins jenkins/jenkins:lts


