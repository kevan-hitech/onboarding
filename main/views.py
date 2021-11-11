from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from ast import literal_eval
import os, time
import os
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import datetime

@login_required(login_url='accounts/login')
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        context = {}
        return render(request, 'main/home.html', context)
    else:
        context = {}
        return render(request, 'main/.html', context)



def download_file(request):
   the_file = r"C:\webs"
   filename = os.path.basename(the_file)
   chunk_size = 134217728
   response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size),
                           content_type=mimetypes.guess_type(the_file)[0])
   response['Content-Length'] = os.path.getsize(the_file)
   response['Content-Disposition'] = "attachment; filename=%s" % filename
   print(datetime.datetime.now(),"fetching file...")
   return response