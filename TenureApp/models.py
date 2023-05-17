from django.db import models

# Create your models here.

class Assets(models.Model):
    FLAT_TYPES = (
        ("FT", "Family or Bachelor Flat"),
        ("FF", "Family Flat"),
        ("MB", "Male Flat"),
        ("FB", "Female Flat"),
        ("MM", "Male Mess"),
        ("FM", "Female Mess")
    )

    KITCHEN_TYPE = (
        (0, "Not Available"),
        (1, "Shared"),
        (2, "Attached")
    )

    WASHROOM_TYPE = (
        (1, "Shared"),
        (2, "Attached")
    )
    title = models.CharField(max_length = 20)
    collection = models.CharField(max_length = 50)
    type = models.CharField(max_length=2, choices = FLAT_TYPES)
    # location
    # district
    kitchen = models.PositiveSmallIntegerField(choices = KITCHEN_TYPE)
    washroom = models.PositiveSmallIntegerField(choices = WASHROOM_TYPE)

class Tenancy(models.Model):
    STATUS = (
        (2, "REJECT"),
        (1, "REQUEST"),
        (0, "RESOLVE"),
    )
    AssetID = models.ForeignKey(Assets, on_delete=models.CASCADE)
    Status = models.PositiveSmallIntegerField(choices=STATUS)