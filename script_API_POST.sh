#!/bin/bash
echo "##############################################################"
echo "#Created by: Saroj Kumar"
echo "#Date	 : 09/05/2019 "
echo "#Usage	 : This script is used to Test REST POST API call."
echo "##############################################################"

echo -e "\n\n"
echo "#######################################################"
echo "# Add TASK by providing task_name, date, state "
echo "#######################################################"

curl_query=`curl -d '{"tasks":"Test Task 1","due_date":"2019-08-10","task_state":1}' -H 'Content-Type: application/json' http://127.0.0.1:8000/api/tasks/`

#Hard-coded value on the above line to add task!
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

