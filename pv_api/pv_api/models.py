from django.db import models 

class State(models.Model):
    state = models.CharField(max_length=2)
    pv_yield = models.IntegerField()

    def __str__(self):
        return self.state