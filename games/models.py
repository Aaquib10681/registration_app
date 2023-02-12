from django.db import models


class Category(models.Model):
    """ This model will store all the Games """
    name = models.CharField(max_length=128)
    info = models.CharField(max_length=8192, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        category_name = f'{self.name}'
        return category_name


class PlayerInformation(models.Model):
    """ This model will Store Individual player information """
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='game_category')
    
    name = models.CharField(max_length=512)
    parentage = models.CharField(max_length=512, null=True, blank=True)
    address = models.CharField(max_length=1024, null=True, blank=True)
    mobile_num = models.CharField(max_length=16, null=True, blank=True)
    email_address = models.CharField(max_length=128, null=True, blank=True)
    
    dob = models.DateField(max_length=8)
    age = models.CharField(max_length=20, null=True, blank=True)
    qualification = models.CharField(max_length=64, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
        
    def __str__(self):
        player_info = f'{self.name}'
        return player_info
