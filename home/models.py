from django.db import models
from django.utils import timezone


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


class ProjectProfit(models.Model):
    income = models.DecimalField(max_digits=8, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2)
    margin = models.FloatField(null=True, blank=True, default=None)


class Status(models.Model):
    opt_numb = models.IntegerField(unique=True);
    current_status = models.CharField(max_length=50);

    def __str__(self):
        return self.current_status

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class Project(models.Model):
    title = models.CharField(max_length=400)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,
                               blank=True, null=True, to_field='opt_numb')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    project_profit = models.ForeignKey(ProjectProfit, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
