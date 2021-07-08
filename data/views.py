from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q



from .models import Student,Batch,TrainerTask,Trainer,StudentCourseData
from .forms import StudentForm,CourseBatchForm,TaskForm

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
        return render(request,'data/edit_student.html',{'form':form,'course_data':course_data,'now_attending':now_attending,'course_enrolled':course_enrolled,'student':student})

class StudentDeleteView(View):
    def post(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('students')

    def get(self,request,id):
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request,'data/confirm_deletion_student.html',{'form':form})

class AddCourseBatch(View):

    def get(self,request,id):
        student = Student.objects.get(id=id)
        form =CourseBatchForm(initial={'student':student})
        return render(request,'data/add_course_data.html',{'form':form})

    def post(self,request,id):
        form =CourseBatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
        return redirect('students')

class DeleteCourseBatch(View):

    def post(self,request,id):
        batch = StudentCourseData.objects.get(id=id)
        batch.delete()
        return redirect('students')

    def get(self,request,id):
        batch = StudentCourseData.objects.get(id=id)
        msg = "Do you wish to delete?"
        return render(request,'data/confirmation_msg.html',{'msg':msg})


class TaskUpdate(View):

    def get(self,request,id):
        task = TrainerTask.objects.get(id=id)
        form  = TaskForm(instance=task)
        return render(request,'data/task_view.html',{'form':form})

    def post(self,request,id):
        task = TrainerTask.objects.get(id=id)
        form =TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('students')
        return redirect('students')



        



    


    
