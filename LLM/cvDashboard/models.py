from django.db import models

class CVs(models.Model):
    CV = models.FileField(upload_to='CV_files', null=True)

    def __str__(self):
        return f"CV-{self.pk}"
# Create your models here.
#