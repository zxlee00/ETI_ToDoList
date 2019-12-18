from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todo_view(request):
    current_user_id = request.user.id
    all_todo_items = TodoItem.objects.raw('SELECT * from todo_todoitem WHERE userID = ' + str(current_user_id))
    return render(request, 'todo_index.html',
        {'all_items': all_todo_items})

def add_todo(request):
    current_user_id = request.user.id
    new_item = TodoItem(content = request.POST['content'], userID = current_user_id)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.deleted = False
    todo.save()
    return HttpResponseRedirect('/todo/')

def todo_pending(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return HttpResponseRedirect('/todo/')
    
def todo_completed(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return HttpResponseRedirect('/todo/')
