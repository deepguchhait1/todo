from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import CustomUserCreationForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from django.urls import reverse_lazy

# User Authentication part 
class CustomLoginView(LoginView):
    template_name= 'base/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, f"Welcome back, {form.get_user().username}!")
        return super().form_valid(form)

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        try:
            user = form.save()
            if user is not None:
                login(self.request, user)
                messages.success(self.request, f"Account created successfully for {user.username}")
            return super(RegisterPage, self).form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Registration error: {str(e)}")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        # Add form errors to messages
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super(RegisterPage, self).form_invalid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class Tasklist(LoginRequiredMixin, ListView):
    model=Task
    context_object_name='tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model=Task
    context_object_name='task'
    template_name= 'base/task.html'

    
class TaskCreate(LoginRequiredMixin, CreateView):
    model=Task
    fields = ['titel', 'description', 'complete']
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields = ['titel', 'description', 'complete']
    success_url=reverse_lazy('tasks')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model=Task
    context_object_name='task'
    template_name= 'base/task_confirm_delete.html'
    success_url=reverse_lazy('tasks')



