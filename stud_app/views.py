from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse

from stud_app.models import *

from .forms import StudentForm

# Create your views here.
def index(request):
 return render(request, 'students/index.html',{
     'students':Student.objects.all()
 })
 
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
 
def add(request):
    """
    If the request is a POST request, then validate the form and save the data to the database. If the
    request is a GET request, then just render the form
    
    :param request: The request object is a Django object that contains metadata about the request sent
    to the server
    :return: The form is being returned.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_field_of_study = form.cleaned_data['field_of_study']
            
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                field_of_study = new_field_of_study
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form':StudentForm(),
                'success':True
            })
        else:
            form = StudentForm()
    return render(request, 'students/add.html', {
        'form': StudentForm()
    })

def edit(request, id):
    """
    If the request is a POST request, then get the student with the given id, create a form with the
    POST data and the student instance, and if the form is valid, save the form and render the edit.html
    template with the form and a success message
    
    :param request: The request object is the first parameter to all Django views. It contains metadata
    about the request, such as the HTTP method, the remote IP address, and the raw HTTP headers
    :param id: The id of the student we want to edit
    :return: The form is being returned.
    """
    if request.method == 'POST':
        student =Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success':True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form':form
    })
    
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
     