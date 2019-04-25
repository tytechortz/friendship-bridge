from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    pass