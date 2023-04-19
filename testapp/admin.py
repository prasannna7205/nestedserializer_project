from django.contrib import admin
from testapp.models import Auther,Book
# Register your models here.

class AutherAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','subject']
class BookAdmin(admin.ModelAdmin):
    list_display=['id','title','Auther','release_date','rating']
admin.site.register(Auther,AutherAdmin)
admin.site.register(Book,BookAdmin)
