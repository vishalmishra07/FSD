from django.shortcuts import render
import datetime

def hours(request,offset):
    now = datetime.datetime.now()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    dt1 = datetime.datetime.now() - datetime.timedelta(hours=offset)

    context = {'current_time': now,
               'offset':offset,
               'future_time':dt,
               'before_time':dt1
               }
    return render(request,'time.html',context)