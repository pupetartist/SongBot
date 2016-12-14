from django.shortcuts import render

# Create your views here.

def index(request):
    return render_to_response("templates/index.html", RequestContext(request))