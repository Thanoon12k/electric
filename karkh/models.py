from django.db import models

class Transformars(models.Model):
    section_name        = models.CharField(max_length=100,verbose_name="اسم القاطع")
    maintinance_name    = models.CharField(max_length=100,verbose_name="اسم الصيانة  ")
    number              = models.CharField(max_length=100,verbose_name="رقم المحولة ")
    capacity            = models.CharField(max_length=100,verbose_name="سعة المحولة")
    address             = models.CharField(max_length=100,verbose_name="عنوان المحولة ")
    status              = models.CharField(choices=[('جديدة','جديدة'),('مستعملة','مستعملة')],
                                            max_length=100,verbose_name=" الحالة")
    
    fixed              = models.BooleanField(default=False, verbose_name="تم الاصلاح ")
    
    brokentime          = models.DateField(verbose_name="وقت العطل ")
    addtime             = models.DateField(auto_now=True,verbose_name="وقت التسجيل ")
    class Meta:
        ordering=['-id']
        verbose_name_plural ='المحولات'
    def __str__(self):
        return str(self.section_name)   
    def tr_id(self):
        return self.id