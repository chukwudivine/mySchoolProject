from django.contrib import admin


from projects.models import Department, Supervisor, Project

admin.site.register(Department)
admin.site.register(Supervisor)
admin.site.register(Project)
