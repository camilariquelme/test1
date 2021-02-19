from django.shortcuts import render
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "time": strftime("%b %d, %Y", localtime()),
        "hora":strftime("%H:%M %p",localtime())
    }
    return render(request,'index.html', context)