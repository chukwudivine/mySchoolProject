from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supervisor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name='supervisors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    student = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name='projects', on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents')
    supervisor = models.ForeignKey(Supervisor, related_name='projects', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
