from django.shortcuts import render
from .models import Celebration, Year,Pictures
# Create your views here.
from django.views.generic import ListView, DetailView


class CelebrationListView(ListView):
    model = Celebration
    template_name = "celebration/celebration_list.html"

class CelebrationDetailView(DetailView):
    model = Celebration
    template_name = "celebration/celebration_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CelebrationDetailView, self).get_context_data(*args, **kwargs)
        context['pictures_list'] = Pictures.objects.all()
        return context
