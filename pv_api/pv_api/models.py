from django.db import models 

class State(models.Model):
    state = models.CharField(max_length=4)
    pv_yield = models.IntegerField()