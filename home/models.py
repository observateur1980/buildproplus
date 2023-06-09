from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

# Extending User Model Using a One-To-One Link


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True, )
    company_title = models.CharField(max_length=400)
    company_email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return self.company_title + ' ' + self.company_category

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'


class CompanyUnvan(models.Model):
    company = models.ManyToManyField(Company,  blank=True, null=True)
    company_unvan_title = models.CharField(max_length=400)
    company_unvan_city = models.CharField(max_length=400)
    company_unvan_state = models.CharField(max_length=400)
    company_unvan_zip = models.CharField(max_length=400)
    company_unvan_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company_unvan_title


class SubcontractorCategory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    subcontractorcategory_electric = models.BooleanField(default=False)
    subcontractorcategory_plumber = models.BooleanField(default=False)
    subcontractorcategory_carpenter = models.BooleanField(default=False)


class Customer(models.Model):
    customer_first_name = models.CharField(max_length=400)
    customer_last_name = models.CharField(max_length=400)
    customer_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.customer_first_name + ' ' + self.customer_last_name

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


class Status(models.Model):
    status_opt_numb = models.IntegerField(unique=True);
    status_current_status = models.CharField(max_length=50);

    def __str__(self):
        return self.status_current_status

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class Project(models.Model):
    project_title = models.CharField(max_length=400)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,
                               blank=True, null=True, )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

    project_income = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    project_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    project_profit = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    project_margin = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    project_created_date = models.DateTimeField(default=timezone.now)
    project_start_date = models.DateField(blank=True, null=True)
    project_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'


class Unvan(models.Model):
    unvan_title = models.CharField(max_length=400)
    unvan_city = models.CharField(max_length=400)
    unvan_state = models.CharField(max_length=400)
    unvan_zip = models.CharField(max_length=400)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    unvan_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.unvan_title
