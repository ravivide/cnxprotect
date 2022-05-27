from django.contrib import admin
from .models import Dictionary
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from CNXProtect_Utl.models import File
from .models import *


admin.site.register(Dictionary)
admin.site.register(Dictionary1)
admin.site.register(Customer)
# admin.site.register(Product)
admin.site.register(File)
admin.site.register(File_1)
admin.site.register(File_pdf)
admin.site.register(Master_Data)
admin.site.register(Master_Data1)
admin.site.register(MSA)
admin.site.register(Add_Keywords)

admin.site.register(Master_Data3)
# admin.site.register(Order)