from django import forms
from django.forms import TextInput, ChoiceField, Select

from home.models import Project, Customer, Unvan


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_first_name', 'customer_last_name', 'customer_email')
        widgets = {
            'customer_first_name': TextInput(attrs={'id': 'customer_first_name', 'name': 'customer_first_name',
                                           'class': 'form-control',  }),

            'customer_last_name': TextInput(attrs={'id': 'customer_last_name', 'name': 'customer_last_name',
                                          'class': 'form-control', }),
            'customer_email': TextInput(attrs={'id': 'customer_email', 'name': 'customer_email',
                                                   'class': 'form-control', }),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'status', 'project_start_date', 'project_end_date')
        widgets = {
            'project_title': TextInput(attrs={'id': 'project_title', 'name': 'project_title',
                                      'class': 'form-control', }),

            'status': Select(attrs={'id': 'project_status', 'name': 'project_status',
                                    'class': 'form-select', }),

            'project_start_date': TextInput(attrs={'id': 'project_start_date', 'name': 'project_start_date',
                                           'class': 'form-control', }),

            'project_end_date': TextInput(attrs={'id': 'project_end_date', 'name': 'project_end_date',
                                         'class': 'form-control', })

        }


class UnvanForm(forms.ModelForm):
    class Meta:
        model = Unvan
        fields = ('unvan_title', 'unvan_city', 'unvan_state', 'unvan_zip')
        widgets = {
            'unvan_title': TextInput(attrs={'id': 'unvan_title', 'name': 'unvan_title',
                                      'class': 'form-control', }),

            'unvan_city': TextInput(attrs={'id': 'unvan_city', 'name': 'unvan_city',
                                     'class': 'form-control', }),

            'unvan_state': TextInput(attrs={'id': 'unvan_state', 'name': 'unvan_state',
                                      'class': 'form-control', }),

            'unvan_zip': TextInput(attrs={'id': 'unvan_zip', 'name': 'unvan_zip',
                                    'class': 'form-control', }),
        }
