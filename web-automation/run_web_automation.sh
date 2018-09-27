#!/bin/bash

SECONDS=0
behave_image=gunesmes/python-selenium-behave-page-object-docker:latest


echo " - Get the latest docker images"
docker pull ${behave_image}

echo -e "\n - Test running on \n    https://localhost:8001\n\n"

rm -rf report/*  2>/dev/null
rm -rf html_report/* 2>/dev/null

for tag in \
	"create" \
	"create_check" \
	"user_check" 
	do

	for platform in \
		"desktop" \
		"iphone6" \
		"iphoneX" \
		"pixel2"
		do
			
		run_name=test_${tag}_on_${platform}
		echo " - Running tests: $tag on $platform"
		
		docker run --network host --shm-size 256M --name ${run_name} -v $PWD:/project ${behave_image} bash -c "export BROWSER=$platform && behave -f allure_behave.formatter:AllureFormatter -o report features --tags @'$tag' && exit 0 " &
	done
done


echo -e "\n - - - - - -  RESULT  - - - - - - - "

wait
echo -e "\n - All processes done!"

duration_total=$SECONDS
echo -e " - $(($duration_total / 60)) minutes and $(($duration_total % 60)) seconds elapsed.\n"

docker ps -a > ./docker-list.txt
> ./docker-logs.txt

for var in $(docker ps -a|grep behave|awk '{print $1}')
do 
echo --------------------------- >> ./docker-logs.txt
echo "Logs of docker-"$var >> ./docker-logs.txt
docker logs $var >> ./docker-logs.txt
echo --------------------------- >> ./docker-logs.txt
done

prefix=${branch_name}_qa_
for var in $(docker ps -a|grep ${prefix}|awk -F ${prefix} '{print $2}') 
do
	docker rm -f ${prefix}${var} &
done

nohup docker system prune -f &