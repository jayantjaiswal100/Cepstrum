from django.shortcuts import render
from django.views.generic import ListView
from .models import PaperMan
from .filters import PapermanFilter

# Create your views here.

class PaperManListView(ListView):
    model = PaperMan
    template_name = "paperman/paperman_list.html"

    def get_queryset(self):
        return PaperMan.objects.filter()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filter'] = PapermanFilter(self.request.GET, queryset=self.get_queryset())
        return context
