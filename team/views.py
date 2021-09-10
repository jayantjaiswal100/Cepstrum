from .models import Team
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .serializers import TeamSerializers
# Create your views here.
from django.views.generic import ListView


class TeamListView(ListView):
    model = Team
    template_name = "team_list.html"

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



