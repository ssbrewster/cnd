from django.db import models

class PostcodeValidator(models.Model):
    pattern = models.CharField(max_length=64)
    error = models.CharField(max_length=255)

    def __unicode__(self):
        return self.pattern


class Country(models.Model):
    class Meta:
        ordering = ['sort', 'name']

    name = models.CharField(max_length=64)
    sort = models.IntegerField(default=10)
    iso = models.CharField(max_length=2)
    postcode_validator = models.ForeignKey(PostcodeValidator)

    def __unicode__(self):
        return self.name
