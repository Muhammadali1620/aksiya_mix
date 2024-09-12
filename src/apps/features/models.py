from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from apps.categories.models import Category
from apps.discounts.models import Discount
from apps.general.models import AbstractModel


class Feature(AbstractModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    measure = models.CharField(max_length=20, blank=True)

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        unique_together = (('category', 'slug'),)

    def __str__(self):
        return self.name


class FeatureValue(AbstractModel):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class DiscountFeature(AbstractModel):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='features')
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE, related_name='product_feature')
    price = models.DecimalField(max_digits=20, 
                                decimal_places=1, 
                                default=0, 
                                validators=[MinValueValidator(0)])
    ordering_number = models.PositiveSmallIntegerField()

    def clean(self):
        if self.discount.category.id != self.feature_value.feature.category.id:
            raise ValidationError('Feature value category does not match discount category')
    
    def __str__(self):
        return self.price