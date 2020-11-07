from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import class_fix
from django.contrib import messages
from fixapp import models
# Create your views here.


def fix(request):

     return render(request, "fix_class.html")


def fix_student(request):
    if request.method == "POST":
        id = request.POST.get("stu_id", None)
        phone = request.POST.get("phone", None)
        class_id = request.POST.get("class_id", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open('msgdata.txt', 'a+') as f:
            f.write("{}--{}--{}--{}--{}--\n".format(class_id, msg,id, \
                                                phone, time.strftime("%Y-%m-%d %H:%M:%S")))

    return render(request, "fix_student.html")


def fix_teacher(request):
    datalist = []
    if request.method == "GET":
        class_id = request.GET.get("class_id", None)
        if class_id != None:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if class_id=='':
                        cnt = cnt + 1
                        d = {"stu_id": linedata[2], "phone": linedata[3], "msg": linedata[1] \
                            , "time": linedata[4], "class_id": linedata[0]}
                        datalist.append(d)
                    if linedata[0] == class_id:
                        cnt = cnt + 1
                        d = { "stu_id": linedata[2],"phone": linedata[3],"msg": linedata[1] \
                            , "time": linedata[4],"class_id": linedata[0]}
                        datalist.append(d)
                    if cnt >= 100:
                        break
    return render(request, "fix_teacher.html", {"data":datalist})


def student(request):  #存信息进数据库
    if request.method == "POST":     #用户提交到服务器

        now_time = str(datetime.now())
        hour_time = now_time[0:19]
        day_time = now_time[0:10]

        cid=request.POST.get("class_id")
        m = request.POST.get("msg")

        if (request.FILES.get("photo")): #判断照片是否为空
            file = request.FILES['photo']
        else:
            file='0.jpg'

        if(request.POST.get("stu_name")):#判断学生姓名是否为空
            sd=request.POST.get("stu_name")
        else:
            sd='一位不愿意透露姓名的小可爱'

        if (request.POST.get("stu_id")):#判断学生学号是否为空
            id1 = request.POST.get("stu_id")
        else:
            id1 = '******'

        if (request.POST.get("phone")):#判断学生联系电话是否为空
            ph = request.POST.get("phone")
        else:
            ph = '******'

        if (request.POST.get("email")):#判断学生邮箱是否为空
            em = request.POST.get("email")
        else:
            em = '******'


        if(m):#判断报修内容和报修班级是否为空
            if(cid):
                new = class_fix(
                    time=hour_time,
                    stu_name=sd,
                    stu_id=id1,
                    phone=ph,
                    email=em,
                    class_id=cid,
                    msg=m,
                    flag=0,
                    #user=day_time,
                    photo=file,
                )
            else:
                messages.error(request, '亲，报修教室不可为空呢！')
                return render(request, "student.html")
        else:
            messages.error(request, '亲，报修内容不可为空呢！')
            return render(request, "student.html")
        new.save()  # 更新数据库
    messages.error(request, '亲，感谢您为建设美好校园做出贡献，ღ( ´･ᴗ･` )比心')
    return render(request, "student.html")



def teacher(request): #对数据库信息进行查询

    if request.method == "GET":
        id = request.GET.get("class_id", None)
        if id=='':
            fix_class_list = class_fix.objects.all()
        else:
            fix_class_list = class_fix.objects.filter(class_id=id)

    n = len(fix_class_list)
    new_list = list(range(n))

    for i in range(n):#实现倒序
        new_list[i]=fix_class_list[n-1-i]

    context = {'fix_class_list': new_list}
    return render(request,"teacher.html",context)