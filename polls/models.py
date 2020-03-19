from django.db import models


class A(models.Model):
    a = models.CharField(max_length=255)
    b = models.IntegerField(default=0)

    def get_a(self):
        return self.a
