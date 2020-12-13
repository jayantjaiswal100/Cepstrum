from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from alumni.models import Bio
from alumni.forms import AlumniForm
from django.utils import timezone
from .filters import AlumniFilter
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

class AlumniListView(ListView,LoginRequiredMixin):
    model = Bio
    template_name = "alumni/bio_list.html"

    def get_queryset(self):
        return Bio.objects.filter(published_date__lte=timezone.now()).order_by('-updated_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AlumniFilter(self.request.GET, queryset=self.get_queryset())
        return context

class AlumniCreateView(UserPassesTestMixin,LoginRequiredMixin,CreateView):
    template_name = "alumni/bio_form.html"
    form_class = AlumniForm
    success_url = reverse_lazy("alumni:all")

    def test_func(self):
        try:
            self.request.user.bio
            return False
        except AttributeError:
            return True

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AlumniUpdateView(LoginRequiredMixin, View):
    template_name = 'alumni/bio_form.html'
    success_url = reverse_lazy('alumni:all')
    def get(self, request, pk) :
        pic = get_object_or_404(Bio, id=pk, owner=self.request.user)
        form = AlumniForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        pic = get_object_or_404(Bio, id=pk, owner=self.request.user)
        form = AlumniForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.updated_date = timezone.now()
        pic.save()

        return redirect(self.success_url)

class AlumniDetailView( LoginRequiredMixin,DetailView):
    model = Bio
    template_name = "alumni/bio_detail.html"
