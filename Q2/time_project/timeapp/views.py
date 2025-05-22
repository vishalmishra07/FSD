from django.shortcuts import render
import datetime

def hours(request, offset):
    now = datetime.datetime.now()
    dt_future = now + datetime.timedelta(hours=offset)
    dt_before = now - datetime.timedelta(hours=offset)
    
    context = {
        'current_time': now,
        'offset': offset,
        'future_time': dt_future,
        'before_time': dt_before
    }
    
    return render(request, 'time.html', context)