from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy,reverse
# Create your views here.
class StudentCreateView(CreateView):
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
