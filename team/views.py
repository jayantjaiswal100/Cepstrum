from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .serializers import TeamSerializers
# Create your views here.
from django.views.generic import ListView


class TeamListView(ListView):
    model = Team
    template_name = "team_list.html"

class PrevTeamListView(ListView):
    model = PrevTeam
    template_name = "prev_team_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = Year.objects.all()
        context['mylist'] = zip(PrevTeam.objects.all(), Year.objects.all())
        return context


class TeamList(mixins.ListModelMixin, GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class TeamRetrive(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)



