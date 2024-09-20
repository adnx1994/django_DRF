from django.db import models

# Create your models here.



class Todo(models.Model):
    title=models.CharField(verbose_name='عنوان',max_length=300)
    content=models.TextField(verbose_name="محتوا",max_length=500)
    priority=models.IntegerField(verbose_name="اولویت",default=1)
    is_done=models.BooleanField(verbose_name="انجام شده/نشده")
    
    
    def __str__(self) -> str:
        return f'{self.title}/ is_done ={self.is_done}'
    
    class Meta():
        verbose_name="انجام کار"
        verbose_name_plural = "انجام کارها"
        db_table="لیست انجام کارها"
