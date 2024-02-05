from django.shortcuts import get_object_or_404, render
from item.models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user)
    
    return render(request,'my_dashboard/index.html',{
        'items':items
    })