# from django.shortcuts import render
from rest_framework.views import APIView
from todo.models import States, TaskList
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date


class TodoView(APIView):

    def get(self, request):

        try:
            data = []

            task_state_id = request.GET.get('task_id')
            task_due_date = request.GET.get('task_date')

            # To retrieve data filter by task_state i.e.,TO-DO=1, IN-PROGRESS=2 and DONE=3
            if task_state_id is not None:
                task_obj = TaskList.objects.filter(task_state=task_state_id)

                for values in task_obj:
                    data.append({
                        'id': values.id,
                        'tasks': values.tasks,
                        'due_date': values.due_date,
                        'state': values.task_state.states,
                    })

            # To retrieve data filter by due date in format YYYY-MM-DD
            elif task_due_date is not None:

                current_date = date.today()

                task_obj = TaskList.objects.filter(due_date__range=[current_date, task_due_date])

                for values in task_obj:
                    data.append({
                        'id': values.id,
                        'tasks': values.tasks,
                        'due_date': values.due_date,
                        'state': values.task_state.states,
                    })

            # To retrieve all data
            else:
                task_obj = TaskList.objects.all()

                for values in task_obj:
                    data.append({
                        'id': values.id,
                        'tasks': values.tasks,
                        'due_date': values.due_date,
                        'state': values.task_state.states,
                    })

            no_data_msg = {
                "msg": "No result found."
            }

            if not data:
                return HttpResponse(json.dumps(no_data_msg, cls=DjangoJSONEncoder), content_type='application/json',
                                    status=200)

            # serialized_data = TaskListSerializer(data, many=True)
            else:
                return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json',
                                    status=200)

        except:
            error = {
                "msg": "Unable to Retrieve Tasks."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

    #########################################################################
    # POST API - by providing tasks as taskname, due_date and task_state as i.e.,TO-DO=1, IN-PROGRESS=2 and DONE=3
    #########################################################################
    def post(self, request):
        try:
            tasks = request.data.get('tasks')
            due_date = request.data.get('due_date')
            task_state = request.data.get('task_state')

            state_obj = States.objects.get(id=task_state)

            addtask = TaskList(tasks=tasks, due_date=due_date, task_state=state_obj)
            addtask.save()

            success = {
                "msg": "Task added successfully."
            }

            return HttpResponse(json.dumps(success, cls=DjangoJSONEncoder), content_type='application/json', status=200)


        except:
            error = {
                "msg": "Unable to add Task."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

    #########################################################################
    # DELETE API - by providing task_id
    #########################################################################

    def delete(self, request):
        try:
            id = request.GET.get('task_id')
            del_task = TaskList(id=id)
            del_task.delete()

            success = {
                "msg": "Task deleted successfully."
            }

            return HttpResponse(json.dumps(success, cls=DjangoJSONEncoder), content_type='application/json', status=200)


        except:
            error = {
                "msg": "Unable to delete Task."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)

    #########################################################################
    # PUT API - by providing task_id, task_name, due_date and task_state as i.e.,TO-DO=1, IN-PROGRESS=2 and DONE=3
    #########################################################################

    def put(self, request):
        try:
            id = request.data.get('task_id')
            task_name = request.data.get('task_name')
            task_due_date = request.data.get('task_date')
            task_state = request.data.get('task_state')

            if id is not None and id is not '':
                task_obj = TaskList.objects.get(id=id)
                task_obj.tasks = task_name
                task_obj.due_date = task_due_date
                task_obj.task_state_id = task_state

                # if task_name is not None and task_due_date is not None and task_state is not None:
                #    due_date task_obj.tasks = task_name
                #     task_obj.due_date = task_due_date
                #     task_obj.task_state_id = task_state
                #
                # else:
                #     if task_name is not None and task_due_date is not None:
                #         task_obj.tasks = task_name
                #         task_obj.due_date = task_due_date
                #
                #     elif task_name is not None and task_state is not None:
                #         task_obj.tasks = task_name
                #         task_obj.task_state_id = task_state
                #
                #     elif task_due_date is not None and task_state is not None:
                #         task_obj.due_date = task_due_date
                #         task_obj.task_state_id = task_state
                #
                #     elif task_name is not None:
                #         task_obj.tasks = task_name
                #
                #     elif task_due_date is not None:
                #         task_obj.due_date = task_due_date
                #
                #     elif task_state is not None:
                #         task_obj.task_state_id = task_state

                task_obj.save()
                msg = {
                    "message": "Task updated successfully."
                }

            else:
                msg = {
                    "message": "No result found to update."
                }

            return HttpResponse(json.dumps(msg, cls=DjangoJSONEncoder), content_type='application/json', status=200)

        except:

            error = {
                "msg": "Unable to update task."
            }

            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)
