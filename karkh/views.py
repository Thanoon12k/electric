from django.shortcuts import render
from .models import Transformars
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
def index(request):
   
    if request.method=='GET':
        return render(request, 'index.html',{'transformers':Transformars.objects.filter(fixed=False),'tt':timezone.now()})
    elif request.method=='POST':
        search=request.POST.get('search')
        pk=request.POST.get('pk')
        data=Transformars.objects.filter(fixed=False)
       
        if pk:
            Transformars.objects.filter(id=pk).update(fixed=True)
        elif search:
            search =(Q(number__icontains=search))|(Q(address__icontains=search))
            data=Transformars.objects.filter(search).filter(fixed=False)
        
        return render(request, 'index.html',{'transformers':data,'tt':datetime.now()})
