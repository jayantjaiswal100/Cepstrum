from django.shortcuts import render
from django.views.generic import ListView
from .models import PaperMan
from .filters import PapermanFilter
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .serializers import PaperManSerializers
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


class PaperManList(mixins.ListModelMixin, GenericAPIView):
    queryset = PaperMan.objects.all()
    serializer_class = PaperManSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)