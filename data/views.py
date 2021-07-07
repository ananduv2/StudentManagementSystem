from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy



from .models import Student,Batch,TrainerTask,Trainer
from .forms import StudentForm

# Create your views here.

class TrainerView(View):
    
    def get(self,request):
        trainer =Trainer.objects.get(name=request.user)
        students=Student.objects.all()
        student_count=students.count()
        batch=Batch.objects.all()
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
        #print("Hello")
        student = Student.objects.get(id=id)
        #c=[]
        #n=[]
        #for i in student.course_enrolled.all():
            #c.append(i)
        #for i in student.now_attending.all():
            #n.append(i)
        form = StudentForm(instance=student)
        #form.fields['course_enrolled'].initial=c
        return render(request,'data/edit_student.html',{'form':form})

class StudentDeleteView(View):
    def post(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('students')

    def get(self,request,id):
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request,'data/confirm_deletion_student.html',{'form':form})
        



    


    
