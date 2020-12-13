from django.views.generic import TemplateView, ListView
from django.shortcuts import render

class TestPage(TemplateView):
    """docstring for TestPage."""
    template_name = 'test.html'


    # def __init__(self, arg):
    #     super(TestPage, self).__init__()
    #     self.arg = arg

#class EventListView(ListView):
 #   model = Events
  #  template_name = "index.html"
   # ordering = ['date']


class ThanksPage(TemplateView):
    """docstring for ThanksPage."""
    template_name = 'thanks.html'
    # def __init__(self, arg):
    #     super(ThanksPage, self).__init__()
    #     self.arg = arg

class HomePage(TemplateView):
    """docstring for ThanksPage."""
    template_name = 'index.html'
    # def __init__(self, arg):
    #     super(ThanksPage, self).__init__()
    #     self.arg = arg


