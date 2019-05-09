#!/bin/bash
echo "##############################################################"
echo "#Created by: Saroj Kumar"
echo "#Date	 : 09/05/2019 "
echo "#Usage	 : This script is used to Test REST PUT API call."
echo "##############################################################"

echo -e "\n\n"
echo "#######################################################"
echo "# update TASK by providing id,task_name, date, state "
echo "#######################################################"

curl_query=`curl -d '{"task_id":10,"task_name":"Test Task 3","task_date":"2019-05-06","task_state":3}' -H 'Content-Type: application/json' -X PUT http://127.0.0.1:8000/api/tasks/`

#Hard-coded value on the above line to update task!
#task_state(TO-DO=1, IN-PROGRESS=2, DONE=3)

retval=$?

echo $curl_query|python -m json.tool

if [ $retval -ne 0 ]
then
    echo "Error status code: $retval"
    exit -1
else
    echo "Success: $retval"
fi

