from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import *
from .filters import *
from .forms import StudentForm,ExperienceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
# Create your views here.

class HomeView(LoginRequiredMixin,ListView):
    model = Experience
    def get_queryset(self):
        return Experience.objects.filter().order_by('owner')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_list'] = Student.objects.all()
        context['filter'] = ExpFilter(self.request.GET, queryset=self.get_queryset())
        for i in context['student_list']:
            if str(i) == str(self.request.user):
                context['created'] = True
                break
        print(context)
        return context
    template_name = "inplex/home.html"

class StudentDetailView(LoginRequiredMixin,DetailView):
    model = Student
    template_name = "inplex/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exp'] = Experience.objects.all()
        return context

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
        form.instance.owner = self.request.user
        return super().form_valid(form)
