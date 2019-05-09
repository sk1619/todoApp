#!/bin/bash
echo "##########################################################"
echo "#Created by: Saroj Kumar"
echo "#Date	 : 09/05/2019 "
echo "#Usage	 : This script is used to Test REST GET API call."
echo "##########################################################"

#API URL = "curl -v http://localhost:8000/api/tasks/"
echo -e "\n\n"
echo "#######################################################"
echo "#                  Retrieve all data "
echo "#######################################################"

curl_query=`curl http://localhost:8000/api/tasks/`
retval=$?
flag=-200

echo $curl_query|python -m json.tool

if [ $retval -ne 0 ]
then
    echo "Error status code: $retval"
    exit -1
else
    flag=0
fi

echo -e "\n\n"
echo "#######################################################"
echo "#                  Retrieve by ID "
echo "#######################################################"

curl_query=`curl http://localhost:8000/api/tasks/?task_id=1` #hard-coded value of id(TO-DO=1, IN-PROGRESS=2, DONE=3)

retval=$?

echo $curl_query|python -m json.tool

if [ $retval -ne 0 ]
then
    echo "Error status code: $retval"
    exit -1
else
    flag=0
fi

echo -e "\n\n"

echo "#######################################################"
echo "#                  Retrieve by Date "
echo "#######################################################"

    
curl_query=`curl http://localhost:8000/api/tasks/?task_date=2019-05-17`

retval=$?

echo $curl_query|python -m json.tool

if [ $retval -ne 0 ]
then
    echo "Error status code: $retval"
    exit -1
else
    flag=0
fi

if [ ${flag} -eq 0 ]
then
   echo "Success: $flag"
   exit 0
fi
