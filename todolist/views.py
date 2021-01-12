from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView

from .models import *
from .forms import *

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}

    return render(request, 'todolist/home.html', context)

def list(request):
    tasks = Task.objects.order_by('due_date')
    context = {'tasks':tasks}
    return render(request, 'todolist/list.html', context)

def about(request):
    return render(request, 'todolist/about.html')

class TaskDetailView(DetailView):

    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/dashboard/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)