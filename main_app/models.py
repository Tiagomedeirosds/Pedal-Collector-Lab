from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


SETUPS = (
    ('T', 'Tested'),
    ('E', 'Effects-Order-Saved'),
    ('C', 'Cleaned'),
)

# Create your models here.
class Guitar(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('guitars_detail', kwargs={'pk': self.id})

class Pedal(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    type = models.CharField(max_length=100)
    year = models.IntegerField()
    guitars = models.ManyToManyField(Guitar)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pedal_id': self.id}) 

    def che_for_today(self):
        return self.checked_set.filter(date=date.today()).count() >= len(SETUPS)       



class Checked(models.Model):
    date = models.DateField('checked date')
    setup = models.CharField(
        max_length=1,
        choices=SETUPS,
        default=SETUPS[0][0]
    )

    pedal = models.ForeignKey(Pedal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_setup_display()} on {self.date}"

    class Meta:
        ordering = ['-date']    

