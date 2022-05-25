from django.db import models
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField

# Create your models here.
class Book(models.Model):
    title = models.CharField("Title",max_length=200, blank=True, null=True)
    author_name = models.CharField("Author Name",max_length=200, blank=True, null=True)
    # date_of_publication = models.CharField("Date of Publication",max_length=200, blank=True, null=True)
    number_of_pages = models.PositiveIntegerField("Number of Pages",blank=True, null=True, default=0)
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
    
    
class School(models.Model):
    region_id = models.PositiveIntegerField("Region ID",blank=True, null=True, default=100)
    school = models.CharField("School",max_length=200, blank=True, null=True)
    email = models.EmailField("Email",max_length=200, blank=True, null=True)
    principal = models.CharField("Principal",max_length=200, blank=True, null=True)
    phone = models.CharField("phone",max_length=200, blank=True, null=True)
    address = models.CharField("address",max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.school
    

class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    first_name = models.CharField("First Name",max_length=200, blank=True, null=True)
    last_name = models.CharField("Last Name",max_length=200, blank=True, null=True)
    email = models.EmailField("Email",max_length=200, blank=True, null=True)
    gender = StatusField(choices_name='GENDER_CHOICES',default="Male", blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL,
         related_name="student_school", null=True, blank=True)
    books = models.ForeignKey(Book, on_delete=models.SET_NULL,
         related_name="student_book", null=True, blank=True)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.first_name
    
    @property
    def full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()