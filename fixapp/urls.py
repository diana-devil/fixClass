from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static

urlpatterns=[
    path('',views.fix),#后面两个实现路由分层
    path('fix_student/',views.fix_student,name='fix_student'),#在这里设置name，以便在模板中写name的时候可以找到
    path('fix_teacher/',views.fix_teacher,name='fix_teacher'),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher')
]