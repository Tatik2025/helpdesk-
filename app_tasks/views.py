from django.shortcuts import render, redirect
from .forms import TaskDetailForm
from django.contrib import messages
from app_tasks.models import Type_task, Task


def index(request):
    if request.user.is_authenticated:
        access_level = request.user.access_level
        department = request.user.department
        user_tasks = Task.objects.filter(author_id = request.user.pk)
        tasks_for_user = 2
        tasks_without_executor=3
        all_tasks = 4
        if access_level ==0:
             context = {'user_tasks': user_tasks, 'access_level': access_level}
        elif access_level == 1:
            context = {'user_tasks': user_tasks, 'tasks_for_user': tasks_for_user, 'tasks_without_executor': tasks_without_executor,'access_level': access_level}
        elif access_level == 2:
            context = {'user_tasks':user_tasks,'tasks_for_user':tasks_for_user,'all_tasks':all_tasks, 'access_level':access_level}

        return render(request,"index.html",context)
    else:
        return redirect('app_users:login')

def TaskDetail(request):

    if request.method == 'POST':
        task_id         = request.POST.get('task_id')
        task            = Task.objects.get(id=task_id)

        initial_data = {
            'theme': task.theme,
            "type_task_id": task.type_task_id,
            "priority_id": task.priority_id,
            "status_id": task.status_id,
            "description": task.description,
        }
        form = TaskDetailForm(request.POST or None, user=request.user,initial=initial_data)


        if form.is_valid():
            Task_form = form.save(commit = False)
            Task_form.author_id = request.user
            Task_form.department_id = Type_task.objects.get(name = Task.type_task_id).department_id
            Task_form.save()
            messages.success(request, "Заявка успешно создана!")
            return render(request,'index.html')
        else:
            messages.error(request, "Данные заявки некорректные!")
            return render(request, 'taskdetail.html', {'form': form})
    else:
        form=TaskDetailForm(user=request.user)
        return render(request,'taskdetail.html', {'form':form})
