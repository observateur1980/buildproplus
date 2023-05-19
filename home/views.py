from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from django.views.generic.base import TemplateView, View

from home.forms import CustomerForm, ProjectForm, UnvanForm
from home.models import Project, Status, Customer


# Create your views here.


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'


class ProjectPage(LoginRequiredMixin, TemplateView):
    template_name = 'home/project.html'

    def post(self, request, *args, **kwargs):

        opt_numb_select = int(request.POST['status'])
        customer_id = int(request.POST['customer'])

        qs_statuses = Status.objects.all().values('id', 'status_opt_numb', 'status_current_status')
        qs_customers = Customer.objects.all().values('id', 'customer_first_name', 'customer_last_name',
                                                     'customer_email')
        if opt_numb_select == 1 and customer_id == 1:
            qs_projects = Project.objects.all().values('id', 'project_title', 'customer__id',
                                                       'customer__customer_first_name',
                                                       'customer__customer_last_name',
                                                       'customer__customer_email',

                                                       'project_income',
                                                       'project_cost',
                                                       'project_profit',
                                                       'project_margin',

                                                       'project_start_date', 'project_end_date')
        elif opt_numb_select != 1 and customer_id == 1:
            qs_projects = Project.objects.all().values('id', 'project_title', 'customer__id',
                                                       'customer__customer_first_name',
                                                       'customer__customer_last_name',
                                                       'customer__customer_email',

                                                       'project_income',
                                                       'project_cost',
                                                       'project_profit',
                                                       'project_margin',

                                                       'project_start_date', 'project_end_date') \
                .filter(status__status_opt_numb=opt_numb_select, customer__id__gt=1)
        elif opt_numb_select != 1 and customer_id != 1:
            qs_projects = Project.objects.all().values('id', 'project_title', 'customer__id',
                                                       'customer__customer_first_name',
                                                       'customer__customer_last_name',
                                                       'customer__customer_email',

                                                       'project_income',
                                                       'project_cost',
                                                       'project_profit',
                                                       'project_margin',

                                                       'project_start_date', 'project_end_date') \
                .filter(status__status_opt_numb=opt_numb_select, customer__id=customer_id)
        elif opt_numb_select == 1 and customer_id != 1:
            qs_projects = Project.objects.all().values('id', 'project_title', 'customer__id',
                                                       'customer__customer_first_name',
                                                       'customer__customer_last_name',
                                                       'customer__customer_email',

                                                       'project_income',
                                                       'project_cost',
                                                       'project_profit',
                                                       'project_margin',

                                                       'project_start_date', 'project_end_date') \
                .filter(status__status_opt_numb__gt=1, customer__id=customer_id)

        context = {
            'menu': "homemenu",
            'qs_statuses': qs_statuses,
            'qs_customers': qs_customers,
            'qs_projects': qs_projects,
            'opt_numb_select': opt_numb_select,
            'customer_id': customer_id,

        }

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        opt_numb_select = 3
        qs_statuses = Status.objects.all().values('id', 'status_opt_numb', 'status_current_status')

        qs_customers = Customer.objects.all().values('id', 'customer_first_name', 'customer_last_name',
                                                     'customer_email')

        qs_projects = Project.objects.all().values('id', 'project_title', 'customer__id',

                                                   'customer__customer_first_name',
                                                   'customer__customer_last_name',
                                                   'customer__customer_email',

                                                   'project_income',
                                                   'project_cost',
                                                   'project_profit',
                                                   'project_margin',

                                                   'project_start_date', 'project_end_date') \
            .filter(status__status_opt_numb=opt_numb_select, )

        context = {
            'menu': "projectmenu",
            'qs_statuses': qs_statuses,
            'qs_customers': qs_customers,
            'qs_projects': qs_projects,
            'opt_numb_select': opt_numb_select,

        }

        return self.render_to_response(context)


def create_project(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        project_form = ProjectForm(request.POST)
        unvan_form = UnvanForm(request.POST)
        if customer_form.is_valid() and project_form.is_valid() and unvan_form.is_valid():
            customer = customer_form.save()

            project = project_form.save(commit=False)
            project.customer = customer
            project.save()

            unvan = unvan_form.save(commit=False)
            unvan.customer = customer
            unvan.save()
            return redirect("home:projectpage")

    customer_form = CustomerForm()
    project_form = ProjectForm()
    unvan_form = UnvanForm()
    return render(request, "home/create_project.html",
                  {"customer_form": customer_form,
                   "project_form": project_form,
                   "unvan_form": unvan_form}
                  )



def create_company(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        project_form = ProjectForm(request.POST)
        unvan_form = UnvanForm(request.POST)
        if customer_form.is_valid() and project_form.is_valid() and unvan_form.is_valid():
            customer = customer_form.save()

            project = project_form.save(commit=False)
            project.customer = customer
            project.save()

            unvan = unvan_form.save(commit=False)
            unvan.customer = customer
            unvan.save()
            return redirect("home:projectpage")

    customer_form = CustomerForm()
    project_form = ProjectForm()
    unvan_form = UnvanForm()
    return render(request, "home/create_project.html",
                  {"customer_form": customer_form,
                   "project_form": project_form,
                   "unvan_form": unvan_form}
                  )
