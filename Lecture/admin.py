from django.contrib import admin
from .models import LectureSchedule, Fourth_Year_Subjects, CS1
# Register your models here.

admin.site.register(Fourth_Year_Subjects)
admin.site.register(LectureSchedule)
admin.site.register(CS1)