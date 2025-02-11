from django.shortcuts import render

# Create your views here.

def comms_list(req):
    return render(req, 'comms/comms_list.html')