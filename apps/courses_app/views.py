# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        "all_courses" : courses
    }
    return render(request, "courses_app/index.html", context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/') 
    else:
        new_course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        print(new_course.name)
        print(new_course.desc)
        return redirect('/')


def delete(request, id):
    print('entered delete')
    my_course = Course.objects.get(id=id)
    context = {
        "my_id" : my_course.id,
        "my_name" : my_course.name,
        "my_desc" : my_course.desc
    }
    return render(request, "courses_app/delete.html", context)

def confirm_delete(request, id):
    print("entered confirm_delete")
    b = Course.objects.get(id=id)
    b.delete()
    return redirect('/')