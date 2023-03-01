from django.contrib import admin
from.models import Vehicles,test_drive,customer
from django.contrib.auth.models import Group,User

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
     list_display=['name','price','available','created','updated']
     list_editable=['price','available']
     list_per_page=20
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Vehicles,VehicleAdmin)


class test_driveAdmin(admin.ModelAdmin):
    def usrname(self, object):
        return object.username_id
    list_display=('venue','carmodel','testdate','testtime', 'usrname')
    # exclude=('password',)
    def has_add_permission(self,request,obj= None):
        return False
    def has_change_permission(self,request,obj= None):
        return False
    def has_delete_permission(self,request,obj= None):
        return False        
    verbose_name_plural="testdrive"
admin.site.register(test_drive,test_driveAdmin)


class customerAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email']
    exclude=('password',"Contact",)
    def has_add_permission(self,request,obj= None):
        return False
    def has_change_permission(self,request,obj= None):
        return False
    def has_delete_permission(self,request,obj= None):
        return False        
    verbose_name_plural="customers"
admin.site.register(customer,customerAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)