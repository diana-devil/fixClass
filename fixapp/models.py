from django.db import models
import datetime
# Create your models here.

'''
教室保修类 class_fix
1、上报时间：time
2、学生姓名：stu_name
3、学生学号：stu_id
4、学生联系方式：phone
5、学生邮箱：email
6、保修教室:class_id
7、保修内容:msg
8、维修状态：flag

9、逻辑删除:is_deleta


生成迁移： manage.py makemigrations

执行迁移 : manage.py migrate
'''
class class_fix(models.Model):
    time = models.CharField('报修时间',max_length=50)

    stu_name=models.CharField('报修人',max_length=20)
    stu_id=models.CharField('学生学号',max_length=20)
    phone=models.CharField('联系电话',max_length=20)
    email=models.CharField('联系邮箱',max_length=30)
    class_id = models.CharField('待维修班级',max_length=20,default='***')
    msg = models.TextField('待维修事项',)
    flag = models.BooleanField('维修状态', choices=((1,'已维修'),(0,'未维修')))
    photo = models.ImageField('现场照片',upload_to='photo', default='0.jpg')

    is_delete = models.BooleanField(default=0)

'''class img(models.Model):
    user=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='ptotos',default='user1.jpg')'''