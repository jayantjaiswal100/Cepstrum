import json
from django.http.response import Http404, HttpResponse, JsonResponse
from dataclasses import field
from django.shortcuts import render
import razorpay
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .models import Donation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
import razorpay
client = razorpay.Client(auth=("rzp_test_5yvtSG4kkzANL2", "DmdWo45YVkEIfxTObkiw28hx"))

class DonationList(ListView,LoginRequiredMixin):
    model = Donation
    context_object_name = 'dp_list'
    template_name='donation/list.html'

class DonationCreateView(CreateView,LoginRequiredMixin):
    model = Donation
    template_name = "donation/index.html"
    fields = ('phone','event','amount',)

    def get_success_url(self):
        return reverse('dp:pay', kwargs={'pk' : self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        data = { "amount": int(form.instance.amount*100), "currency": "INR" }
        payment = client.order.create(data=data)
        form.instance.order_id = payment['id']
        return super().form_valid(form)

@method_decorator(csrf_exempt,name='dispatch')
class DonationDetailView(DetailView,LoginRequiredMixin):
    model = Donation
    template_name = "donation/confirmation.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["paisa"] = self.object.amount*100
        return context

    def post(self,request,*args,**kwargs):
        a = json.loads(request.body.decode('utf-8'))
        print(a['payment_id'])
        print(type(self.get_object()))
        self.get_object().setpaymentid(a['payment_id'])  
        # self.get_object().save()
        print(self.get_object().payment_id)
        return JsonResponse({
              "message":"Worked fine"
            })

    




    

