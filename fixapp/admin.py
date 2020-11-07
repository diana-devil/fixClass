from django.contrib import admin
from .models import class_fix

# Register your models here.


class fix_classAdmin(admin.ModelAdmin):
    list_display = ['time','stu_name','stu_id','phone','email','class_id','msg','flag','photo']
    #需要显示的属性
    search_fields = ['class_id']
    #查询列表数据


admin.site.register(class_fix,fix_classAdmin)
