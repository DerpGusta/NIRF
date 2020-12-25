from django.contrib import admin
from Task_Manager import models

admin.site.register(models.Department)
admin.site.register(models.Branch)
admin.site.register(models.Key_Area)
admin.site.register(models.Metric)
admin.site.register(models.FacultyUser)
admin.site.register(models.ManagementUser)
admin.site.register(models.Activity)