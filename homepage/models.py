from django.db import models

class Zero_Product(models.Model):
    id = models.AutoField(primary_key=True)  # 고유 ID 자동 생성

    # 제품 기본 정보
    Manufacturer = models.CharField(default="Unknown", max_length=50, verbose_name="제조사명")  # 제조사
    product_name = models.CharField(max_length=50, verbose_name="제품명")  # 제품명
    Capacity = models.CharField(max_length=50, default=0, verbose_name="용량 (g)")  # 용량
    Product_calorific_value = models.CharField(max_length=50, default=0, verbose_name="열량 (g)")  # 열량

    # 영양 성분
    carbohydrates = models.CharField(max_length=50, verbose_name="탄수화물 (g)")  # 탄수화물
    protein = models.CharField(max_length=50, verbose_name="단백질 (g)")  # 단백질
    fat = models.CharField(max_length=50, verbose_name="지방 (g)")  # 지방
    saturated_fat = models.CharField(max_length=50, default=0, verbose_name="포화지방 (g)")  # 포화지방
    trans_fat = models.CharField(max_length=50, default=0, verbose_name="트렌스지방 (g)")  # 트랜스지방
    Cholesterol = models.CharField(max_length=50, default=0, verbose_name="콜레스테롤 (mg)")  # 콜레스테롤
    sodium = models.CharField(max_length=50, default=0, verbose_name="나트륨 (mg)")  # 나트륨
    Caffeine = models.CharField(max_length=50, default=0, verbose_name="카페인 (g)")  # 카페인
    sugar = models.CharField(max_length=50, default=0, verbose_name="당류 (g)")  # 당류
    Sugar_alcohol = models.CharField(max_length=50, default=0, verbose_name="당알콜 (g)")  # 당알콜

    # 당 관련 주의 성분
    maltitol = models.CharField(max_length=50, default=0, verbose_name="말티톨 (g)")  # 말티톨
    maltitol_syrup = models.CharField(max_length=50, default=0, verbose_name="말티톨 시럽 (g)")  # 말티톨 시럽
    glucose_syrup = models.CharField(max_length=50, default=0, verbose_name="물엿 (g)")  # 물엿

    # 혈당 지표
    GI = models.CharField(max_length=50, default=0, verbose_name="GI지수")  # GI 지수
    GL = models.CharField(max_length=50, default=0, verbose_name="GL지수")  # GL 지수

    # 원재료 정보
    Raw_materials = models.TextField(default="Unknown", max_length=255, verbose_name="원재료명")  # 원재료

    # 혈당 이모지 (😁 😬 등 사용자에게 시각적 피드백)
    emoji = models.CharField(max_length=20, default="😊")

    def __str__(self):
        return self.product_name  # Django admin 표시용

    class Meta:
        verbose_name = "제로식품"
        verbose_name_plural = "제로식품 목록"
