#!/bin/bash
echo "##############################################################"
echo "#Created by: Saroj Kumar"
echo "#Date	 : 09/05/2019 "
echo "#Usage	 : This script is used to Test REST DELETE API call."
echo "##############################################################"

echo -e "\n\n"
echo "#######################################################"
echo "# Delete Task by providing Task_id"
echo "#######################################################"

curl_query=`curl -X DELETE http://127.0.0.1:8000/api/tasks/?task_id=9`

#Hard-coded value on the above line to delete task!

retval=$?

echo $curl_query|python -m json.tool

if [ $retval -ne 0 ]
then
    echo "Error status code: $retval"
    exit -1
else
    echo "Success: $retval"
fi

