from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from bios.models import Bio, Intrest, Projects
from django.utils import timezone
from bios.forms import BioForm, IntrestForm, ProjectForm, TechSkillForm
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .filters import BioFilter, ProjectFilter
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
class BioListView(ListView,LoginRequiredMixin):
    model = Bio
    template_name = "bios/bio_list.html"

    def get_queryset(self):
        return Bio.objects.filter(published_date__lte=timezone.now()).order_by('-updated_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BioFilter(self.request.GET, queryset=self.get_queryset())
        return context

class BioCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = 'bios/bio_form.html'
    form_class = BioForm
    success_url = reverse_lazy('bios:all')

    def test_func(self):
        try:
            self.request.user.bio
            return False
        except AttributeError:
            return True

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BioDeleteView(LoginRequiredMixin,DeleteView):
    model = Bio
    template_name = 'bios/bio_delete.html'
    success_url = reverse_lazy('bios:all')


class BioUpdateView(LoginRequiredMixin, View):
    template_name = 'bios/bio_form.html'
    success_url = reverse_lazy('bios:all')
    def get(self, request, pk) :
        pic = get_object_or_404(Bio, id=pk, owner=self.request.user)
        form = BioForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        pic = get_object_or_404(Bio, id=pk, owner=self.request.user)
        form = BioForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.updated_date = timezone.now()
        pic.save()
        form.save_m2m()

        return redirect(self.success_url)


class BioDetailView( LoginRequiredMixin,DetailView):
    model = Bio
    template_name = "bios/bio_detail.html"

class ProjectListView(LoginRequiredMixin, ListView):
    model = Projects
    template_name = "bios/project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProjectFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ProjectDetailView(DetailView):
    model = Projects
    template_name = "bios/project_detail.html"

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bios/project_create.html'
    form_class = ProjectForm
    success_url = reverse_lazy('bios:project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, View):
    template_name = 'bios/project_create.html'
    success_url = reverse_lazy('bios:project_list')
    def get(self, request, pk) :
        pic = get_object_or_404(Projects, id=pk, owner=self.request.user)
        form = ProjectForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        pic = get_object_or_404(Projects, id=pk, owner=self.request.user)
        form = ProjectForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()
        form.save_m2m()

        return redirect(self.success_url)


class IntrestCreateView(CreateView):
    form_class = IntrestForm
    template_name = 'bios/intrest_create.html'
    def get_success_url(self):
        return reverse('bios:all')

class TechSkillCreateView(CreateView):
    form_class = TechSkillForm
    template_name = 'bios/techskill_create.html'
    def get_success_url(self):
        return reverse('bios:project_list')
