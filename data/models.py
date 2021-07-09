from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    state = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal')
)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length=200,unique=True)
    sex = models.CharField(max_length=10,null=True,choices=(('Male','Male'),('Female','Female')))
    house = models.CharField(max_length=100,null=True)
    street =models.CharField(max_length=100,null=True)
    street2 =models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True,choices=state)
    start_date = models.DateField(null=True)
   

    def __str__(self):
        return self.name

class TrainerTask(models.Model):
    user = models.ForeignKey(Trainer,on_delete=models.CASCADE,related_name='owner')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    complete = models.BooleanField(default=False)
    
    

    def __str__(self):
        s=" - "
        return "%s %s %s" % (self.user,s, self.title)

    class Meta:
        ordering =['complete','-created']


class Batch(models.Model):
    subject = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='subject')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE,related_name='trainer',null=True)
    batch_type=models.CharField(max_length=100,null=True,choices=(('Weekday','Weekday'),('Weekend','Weekend')),default='Weekday')
    start_date = models.DateField(null=True)
    timings = models.CharField(max_length=100,null=True)
    end_date = models.DateField(null=True)
    status = models.CharField(max_length=100,choices=(('Yet to start','Yet to start'),('Ongoing','Ongoing'),('Completed','Completed')),null=True)

    def __str__(self):
        return "%s %s %s" % (self.subject, self.start_date.strftime('%d/%m/%Y'), self.timings)

class Student(models.Model):
    state = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal')
)
    
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    sex = models.CharField(max_length=10,null=True,choices=(('Male','Male'),('Female','Female')))
    house = models.CharField(max_length=100,null=True)
    street =models.CharField(max_length=100,null=True)
    street2 =models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True,choices=state)
    course_enrolled = models.CharField(max_length=100,null=True)
    now_attending = models.CharField(max_length=100,null=True)
    start_date = models.DateField(null=True)
    shared = models.BooleanField(default=False,choices=((True, 'Yes'), (False, 'No')))
    payment = models.CharField(max_length=10,choices=(('Full','Full'),('Half','Half')),default='Half')

    def __str__(self):
        return self.name

class StudentCourseData(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='student',null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,related_name='batch')
    
    def __str__(self):
        s=" 's "
        return "%s %s %s" % (self.student,s, self.batch)






