from django.db import models

# Create your models here.
class link(models.Model):
    linkTitle = models.CharField(max_length=5)
    linkUrl   = models.CharField(max_length=200)
    def titleStr(self):
        return self.linkTitle
    def linkStr(self):
        return self.linkUrl
    def __str__(self):
        return self.linkTitle