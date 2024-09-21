from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user = get_user_model()

class Todo(models.Model):
    title=models.CharField(verbose_name='عنوان',max_length=300)
    content=models.TextField(verbose_name="محتوا",max_length=500)
    priority=models.IntegerField(verbose_name="اولویت",default=1)
    is_done=models.BooleanField(verbose_name="انجام شده/نشده")
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')
    
    
    def __str__(self) -> str:
        return f'{self.title}/ is_done ={self.is_done}'
    
    class Meta():
        verbose_name="انجام کار"
        verbose_name_plural = "انجام کارها"
        db_table="لیست انجام کارها"
