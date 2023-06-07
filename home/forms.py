from django import forms
from django.forms import TextInput, ChoiceField, Select, CheckboxInput

from home.models import Project, Customer, Unvan, Company, CompanyUnvan, SubcontractorCategory


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_title', 'company_email',)
        widgets = {
            'company_title': TextInput(attrs={'id': 'company_title', 'name': 'company_title',
                                              'class': 'form-control', }),

            'company_email': TextInput(attrs={'id': 'company_email', 'name': 'company_email',
                                              'class': 'form-control', }),
        }


class CompanyUnvanForm(forms.ModelForm):
    class Meta:
        model = CompanyUnvan
        fields = ('company_unvan_title', 'company_unvan_city', 'company_unvan_state', 'company_unvan_zip')
        widgets = {
            'company_unvan_title': TextInput(attrs={'id': 'unvan_title', 'name': 'unvan_title',
                                                    'class': 'form-control', }),

            'company_unvan_city': TextInput(attrs={'id': 'unvan_city', 'name': 'unvan_city',
                                                   'class': 'form-control', }),

            'company_unvan_state': TextInput(attrs={'id': 'unvan_state', 'name': 'unvan_state',
                                                    'class': 'form-control', }),

            'company_unvan_zip': TextInput(attrs={'id': 'unvan_zip', 'name': 'unvan_zip',
                                                  'class': 'form-control', }),
        }


class SubcontractorCategoryForm(forms.ModelForm):
    class Meta:
        model = SubcontractorCategory
        fields = ('subcontractorcategory_electric', 'subcontractorcategory_plumber', 'subcontractorcategory_carpenter')
        widgets = {
            'subcontractorcategory_electric': CheckboxInput(attrs={'id': 'subcontractorcategory_electric',
                                                                   'name': 'subcontractorcategory_electric',
                                                                   'class': 'form-check-input', }),
            'subcontractorcategory_plumber': CheckboxInput(attrs={'id': 'subcontractorcategory_plumber',
                                                                   'name': 'subcontractorcategory_plumber',
                                                                   'class': 'form-check-input', }),
            'subcontractorcategory_carpenter': CheckboxInput(attrs={'id': 'subcontractorcategory_carpenter',
                                                                   'name': 'subcontractorcategory_carpenter',
                                                                   'class': 'form-check-input', }),

        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_first_name', 'customer_last_name', 'customer_email')
        widgets = {
            'customer_first_name': TextInput(attrs={'id': 'customer_first_name', 'name': 'customer_first_name',
                                                    'class': 'form-control', }),

            'customer_last_name': TextInput(attrs={'id': 'customer_last_name', 'name': 'customer_last_name',
                                                   'class': 'form-control', }),
            'customer_email': TextInput(attrs={'id': 'customer_email', 'name': 'customer_email',
                                               'class': 'form-control', }),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'status', 'project_start_date', 'project_end_date',)

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
