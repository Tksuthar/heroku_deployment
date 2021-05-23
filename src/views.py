# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import RegistrationForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


form_data = {}
def response(request):
    # check request method is POST or GET
    if request.method =='POST':
        # accessing input value
        form_data['firstname']=request.POST.get('firstname')
        form_data['registration_id']=request.POST.get('registration_id')
        form_data['branch']=request.POST.get('branch')
        form_data['section']=request.POST.get('section')

        # inserting data into database
        form=RegistrationForm()
        form.firstname = form_data['firstname']
        form.registration_id = form_data['registration_id']
        form.branch = form_data['branch']
        form.section = form_data['section']
        form.save()
        context=RegistrationForm.objects.all()
        print(context)
    return render(request, 'response.html', {'context':context})
