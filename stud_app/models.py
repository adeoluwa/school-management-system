from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    student_number = models.PositiveIntegerField()
    field_of_study = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'Students: {self.first_name} {self.last_name}'
    
    
class Staff(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    employee_number = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Staff: {self.first_name}{self.last_name}'
    