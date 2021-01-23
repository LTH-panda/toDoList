from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    content = {'todos' : todos}
    return render(request,'my_to_do_web/index.html', content)

def createTodo(request):
    user_input_content = request.POST['todoContent']
    new_todo = ToDo(content = user_input_content)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("createTodo =>>" + user_input_content )
    
def deleteTodo(request):
    delete_todo_id = request.GET['todoNum']
    delete_todo = ToDo.objects.get(id = delete_todo_id)
    delete_todo.delete()
    # delete_todo.isDone = True
    return HttpResponseRedirect(reverse('index'))        