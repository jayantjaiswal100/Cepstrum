from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import *
from .forms import StudentForm,ExperienceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
# Create your views here.

class HomeView(LoginRequiredMixin,ListView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for i in context['student_list']:
            if str(i) == str(self.request.user):
                context['created'] = True
                break
        print(context)
        return context
    template_name = "inplex/home.html"

class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    template_name = "inplex/create_profile.html"
    form_class = StudentForm
    success_url = reverse_lazy("inplex:all")
    def test_func(self):
        try:
            self.request.user.student
            return False
        except AttributeError:
            return True

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ExperienceCreateView(LoginRequiredMixin,CreateView):
    model = Experience
    template_name = "inplex/create_experience.html"
    form_class = ExperienceForm
    success_url = reverse_lazy("inplex:all")
    def test_func(self):
        try:
            self.request.user.experience
            return False
        except AttributeError:
            return True

    def form_valid(self, form):
        rating = request.POST.get('difficulty1')
        print(rating)
        form.instance.difficulty1=rating
        form.instance.owner = self.request.user
        return super().form_valid(form)
