from django.shortcuts import render
from django.views import View



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

    def get(self,request,id):
        student = Student.objects.get(id=id)
        #print(student.sex)
        form = StudentForm(instance=student)
        return render(request,'data/edit_student.html',{'form':form})
