# from django.db import models
# class Destination(models.Model):
#   name = models.CharField(max_length=100)
#  img = models. ImageField(upload_to='pics')
#  desc = models.TextField()
#  price = models.IntegerField()
#  offer = models.BooleanField(default=False)
# Create your models here.

from django.db import models


# Create your models here.
class Dictionary(models.Model):
    # id = models.CharField(max_length=200, primary_key=True)
    objects = None
    keywords = models.TextField()


class Dictionary1(models.Model):
    # id = models.CharField(max_length=200, primary_key=True)
    objects = None
    keywords = models.TextField()


class MSA(models.Model):
    # id = models.CharField(max_length=200, primary_key=True)
    objects = None
    account = models.TextField()


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class File(models.Model):
    notesfile = models.FileField(upload_to='media')
    # title = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.notesfile
    #
    # # name = models.CharField(max_length=200, null=True)
    # def is_valid(self):
    #     pass


class File_1(models.Model):
    notesfile_1 = models.FileField(upload_to='media')
    # title = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.notesfile
    #
    # # name = models.CharField(max_length=200, null=True)
    # def is_valid(self):
    #     pass


class File_pdf(models.Model):
    notesfile1 = models.FileField(upload_to='media')
    # title = models.CharField(max_length=50)
    # def __str__(self):
    #     return self.notesfile1
    #
    # # name = models.CharField(max_length=200, null=True)
    # def is_valid(self):
    #     pass


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Master_Data(models.Model):
    notesfile_1 = models.FileField(upload_to='Master_File')
    # title = models.CharField(max_length=50)


class Master_Data1(models.Model):
    notesfile_11 = models.FileField(upload_to='Master_File1')
    # title = models.CharField(max_length=50)


class Master_Data3(models.Model):
    notesfile_111 = models.FileField(upload_to='Master_File3')
    # title = models.CharField(max_length=50)


class Add_Keywords(models.Model):
    name = models.TextField(max_length=200, null=True)
    # notesfile_1 = models.FileField(upload_to='Master_File')
    # title = models.CharField(max_length=50)