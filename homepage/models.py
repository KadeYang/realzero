from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Zero_Product(models.Model):
    id = models.AutoField(primary_key=True)  
    product_name = models.CharField(max_length=50, verbose_name="제품명")
    carbohydrates = models.FloatField(verbose_name="탄수화물 (g)")
    protein = models.FloatField(verbose_name="단백질 (g)")
    fat = models.FloatField(verbose_name="지방 (g)")
    sodium = models.FloatField(verbose_name="나트륨 (mg)")
    maltitol = models.FloatField(verbose_name="말티톨 (g)")
    maltitol_syrup = models.FloatField(verbose_name="말티톨 시럽 (g)")
    glucose_syrup = models.FloatField(verbose_name="물엿 (g)")

    def __str__(self):
        return self.product_name
        # product_name이 물건의 이름이고, __str__은 그 이름을 말해준다.
    class Meta:
        verbose_name = "제로식품"
        verbose_name_plural = "제로식품 목록"
        # Django 관리자 페이지에서 모델이 "제로식품 목록"으로 보이고
        # 각 객체는 product_name으로 구별됩니다.