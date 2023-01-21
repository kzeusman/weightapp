from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weight(models.Model):
	title = models.CharField(max_length=25,default=False)
	weight = models.CharField(max_length=100)
	memo = models.CharField(max_length=200 ,blank=True)
	created = models.DateTimeField()
	datecompletes = models.DateTimeField(null=True, blank=True)
	important = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
