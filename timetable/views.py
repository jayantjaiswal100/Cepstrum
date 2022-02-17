from typing import NoReturn
from timetable.models import Timetable
from django.shortcuts import render
from django.contrib.messages.api import error
from django.http import HttpResponseRedirect, response
from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

days=['mon','tue','wed','thur','fri']
slots=['8_9','9_10','10_11','11_12','12_1','2_3','3_4','4_5']


def index(request):
    return render(request,'timetable/index.html')

def showtable(request):
    roll=request.GET['rollNumber']
    if(roll==''):
        return HttpResponseRedirect('/timetable')
    r=roll
    roll=int(roll)
    if Timetable.objects.filter(year=int(r[:2])):
        if Timetable.objects.filter(branch=r[5]).exists() :
            tt=Timetable.objects.filter(year=int(r[:2]),branch=r[5])
            for i in tt:
                d={"tt":i }
            print(r[:2])
            print(r[5])
            return render(request,'timetable/table.html',d)
        else:
            print("not found")
    else:
         return render(request,'timetable/index.html',{"invalid":True})
    # if Timetable.objects.filter(roll_number=roll).exists() :
    #     tt=Timetable.objects.filter(roll_number=roll)
    #     for i in tt:
    #         d={"tt":i }
    #     return render(request,'timetable/table.html',d)
    # else:
    #     return render(request,'timetable/index.html',{"invalid":True})
        # return HttpResponseRedirect('/')


# def adminpanel(request):
#     if (request.user.is_authenticated):
#         return render(request,'timetable/admin.html')
#     else:
#         return redirect('timetable/login')

# def logout(request):
#     auth.logout(request)
#     return redirect('/timetable')

# def login(request):
#     if (request.method == "POST"):
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username = username, password = password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('adminpanel')
#         else:
#             return render(request,'timetable/login.html',{"invalid":True})
#     else:
#         return render(request, 'timetable/login.html')

# def submit(request):
#     lower=int(request.POST['lower'])
#     upper=int(request.POST['upper'])
#     getslots=request.POST.getlist('slot')
#     for roll in range(lower,upper+1):
#         Timetable.objects.filter(roll_number=roll).delete()
#         Timetable.objects.update_or_create(
#             roll_number=roll,
#             mon_8_9 = getslots[ 0 ],
#             mon_9_10 = getslots[ 1 ],
#             mon_10_11 = getslots[ 2 ],
#             mon_11_12 = getslots[ 3 ],
#             mon_12_1 = getslots[ 4 ],
#             mon_2_3 = getslots[ 5 ],
#             mon_3_4 = getslots[ 6 ],
#             mon_4_5 = getslots[ 7 ],
#             tue_8_9 = getslots[ 8 ],
#             tue_9_10 = getslots[ 9 ],
#             tue_10_11 = getslots[ 10 ],
#             tue_11_12 = getslots[ 11 ],
#             tue_12_1 = getslots[ 12 ],
#             tue_2_3 = getslots[ 13 ],
#             tue_3_4 = getslots[ 14 ],
#             tue_4_5 = getslots[ 15 ],
#             wed_8_9 = getslots[ 16 ],
#             wed_9_10 = getslots[ 17 ],
#             wed_10_11 = getslots[ 18 ],
#             wed_11_12 = getslots[ 19 ],
#             wed_12_1 = getslots[ 20 ],
#             wed_2_3 = getslots[ 21 ],
#             wed_3_4 = getslots[ 22 ],
#             wed_4_5 = getslots[ 23 ],
#             thur_8_9 = getslots[ 24 ],
#             thur_9_10 = getslots[ 25 ],
#             thur_10_11 = getslots[ 26 ],
#             thur_11_12 = getslots[ 27 ],
#             thur_12_1 = getslots[ 28 ],
#             thur_2_3 = getslots[ 29 ],
#             thur_3_4 = getslots[ 30 ],
#             thur_4_5 = getslots[ 31 ],
#             fri_8_9 = getslots[ 32 ],
#             fri_9_10 = getslots[ 33 ],
#             fri_10_11 = getslots[ 34 ],
#             fri_11_12 = getslots[ 35 ],
#             fri_12_1 = getslots[ 36 ],
#             fri_2_3 = getslots[ 37 ],
#             fri_3_4 = getslots[ 38 ],
#             fri_4_5 = getslots[ 39 ],
#         )
#     return redirect('adminpanel')
