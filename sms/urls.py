"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from data.views import *

urlpatterns = [
    path('admin/', admin.site.urls),


    path('student_list/',TrainerView.as_view(),name='students'),
    path('student/<str:id>/',StudentEditView.as_view(),name='student_edit'),
    path('student/delete/<str:id>/',StudentDeleteView.as_view(),name='student_delete'),
    path('student/add_course_data/<str:id>/',AddCourseBatch.as_view(),name='add_course_data'),
    path('student/delete_course_data/<str:id>/',DeleteCourseBatch.as_view(),name='delete_course_data'),
]
