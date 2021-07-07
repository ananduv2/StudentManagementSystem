from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q



from .models import Student,Batch,TrainerTask,Trainer,StudentCourseData
from .forms import StudentForm

# Create your views here.

class TrainerView(View):
    
    def get(self,request):
        trainer =Trainer.objects.get(name=request.user)
        students=Student.objects.all()
        for i in students:
            course_data = StudentCourseData.objects.filter(student=i)
            i.course_enrolled=[]
            i.now_attending=[]
            for j in course_data:
                i.course_enrolled.append(j.batch.subject)
                if j.batch.status == "Ongoing":
                    i.now_attending.append(j.batch.subject)
            print(type(i.now_attending))
            i.save()
        student_count=students.count()
        batch=Batch.objects.filter(~Q(status="Completed"))
        batch_count=batch.count()
        user=request.user
        task=TrainerTask.objects.filter(user=trainer,complete=False)
        task_count=task.count()
        return render(request,'data/dashboard.html',{'tasks':task,'task_count':task_count,'students': students, 'batch': batch, 'user':user,'student_count':student_count,'batch_count':batch_count})


class StudentEditView(View):

    def post(self,request,id):
        student = Student.objects.get(id=id)
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')  
        return HttpResponse("updation failed")

    def get(self,request,id):
        student = Student.objects.get(id=id)
        course_data = StudentCourseData.objects.filter(student=student)
        course_enrolled=[]
        now_attending=[]
        for i in course_data:
            course_enrolled.append(i.batch.subject)
            if i.batch.status == "Ongoing":
                now_attending.append(i.batch.subject)
        form = StudentForm(instance=student)
        return render(request,'data/edit_student.html',{'form':form,'course_data':course_data,'now_attending':now_attending,'course_enrolled':course_enrolled})

class StudentDeleteView(View):
    def post(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('students')

    def get(self,request,id):
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request,'data/confirm_deletion_student.html',{'form':form})
        



    


    
