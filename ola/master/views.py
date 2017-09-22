from django.shortcuts import render
from .models import Request_id,DriverDtil
# Create your views here.

import datetime

def index(request):
    album_id = 3
    Request = Request_id.objects.all().order_by('id').reverse()
    time = []
    for i in Request:
        print('Before',i.req_time)
        tz_info = i.req_time.tzinfo

        now = datetime.datetime.now(tz_info) - i.req_time
        time.append(now)
        i.req_time = now
        print('After',i.req_time)
    print (time)
    return render(request, 'home/index.html', {'Request': Request, 'Time':time, 'album_id':album_id})


def customer(request):
    return render(request, 'home/CUSTOMER.html' )

def customerFun(request):

    #return render(request, 'home/contact-us.html')
    if request.method == "POST":
        text_form = request.POST.get('text')
        temp = Request_id(Cust_ID_id=int(text_form),Driver_ID_id=6)
        temp.save()

        print ("Hello world",text_form)
        form = 'Success!! Message Sent.'
    #return render(request, 'home/contact-us.html', {'form': form})
    form = 'Success!! Message Sent.'
    return render(request, 'home/CUSTOMER.html', {'form': form})


#def driver(request):
def drivers(request, d_id):
    print 'Hello000000w Sir',d_id
    cnt = Request_id.objects.filter(drop=None).filter(Driver_ID=d_id).count()

    message = ''
    if cnt != 0:
        message = 'disabled'

    Waiting = Request_id.objects.all().exclude(pickup__isnull=False)
    Ongoing = Request_id.objects.filter(Driver_ID=d_id).filter(drop=None)
    completed = Request_id.objects.filter(Driver_ID=d_id).filter(drop__isnull=False)
    for i in completed:
        print 'Ongoing ',i.Driver_ID,i.req_time,i.pickup,i.drop,i.Cust_ID
    return render(request, 'home/report.html',{'message':message, 'Ongoing':Ongoing, 'completed':completed, 'Waiting':Waiting, 'd_id':d_id} )

def driver(request):
    print 'Hellow Sir'
    completed = DriverDtil.objects.all()
    return render(request, 'home/DRIVER.html',{ 'completed':completed})

from django.db.models import Count
def DRIVERselect(request, r_id, c_id, d_id):
    cnt = Request_id.objects.filter(drop=None).filter(Driver_ID=d_id).count()
    print r_id, c_id, d_id, 'Hellow Sir',cnt
    message =''
    if cnt == 0:
        now = datetime.datetime.utcnow()
        update = Request_id.objects.filter(id=r_id).update(pickup=now, Driver_ID=d_id , Status=1)
    else:
        message='disabled'


    Waiting = Request_id.objects.all().filter(pickup__isnull=True)
    Ongoing = Request_id.objects.filter(Driver_ID=d_id).filter(drop=None)
    completed = Request_id.objects.filter(Driver_ID=d_id).filter(drop__isnull=False)
    for i in completed:
        print 'Ongoing ', i.Driver_ID, i.req_time, i.pickup, i.drop, i.Cust_ID
    return render(request, 'home/report.html', {'message':message,'Ongoing': Ongoing, 'completed': completed, 'Waiting': Waiting, 'd_id':d_id})
