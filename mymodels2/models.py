from django.db import models

# class Language(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Framework(models.Model):
#     language = models.ForeignKey(Language, on_delete=models.CASCADE)
#     f_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.f_name
#

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)
    pcost = models.DecimalField(decimal_places=2, max_digits=10)
    pmfdt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    pexpdt = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.pname
