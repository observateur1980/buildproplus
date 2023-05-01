from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from django.views.generic.base import TemplateView, View

from home.models import Project, Status, Customer



# Create your views here.


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'


class ProjectPage(LoginRequiredMixin, TemplateView):
    template_name = 'home/project.html'

    def post(self, request, *args, **kwargs):

        opt_numb_select = int(request.POST['status'])
        customer_id = int(request.POST['customer'])

        qs_statuses = Status.objects.all().values('id', 'opt_numb', 'current_status')
        qs_customers = Customer.objects.all().values('id', 'first_name', 'last_name')
        if opt_numb_select == 1 and customer_id == 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date')
        elif opt_numb_select != 1 and customer_id == 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date') \
                .filter(status__opt_numb=opt_numb_select, customer__id__gt=1)
        elif opt_numb_select != 1 and customer_id != 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date') \
                .filter(status__opt_numb=opt_numb_select, customer__id=customer_id)
        elif opt_numb_select == 1 and customer_id != 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date') \
                .filter(status__opt_numb__gt=1, customer__id=customer_id)

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
        qs_statuses = Status.objects.all().values('id', 'opt_numb', 'current_status')
        qs_customers = Customer.objects.all().values('id', 'first_name', 'last_name')
        qs_projects = Project.objects.all().values('id', 'title', 'customer__id',

                                                   'customer__first_name',
                                                   'customer__last_name',

                                                   'project_profit__income',
                                                   'project_profit__cost',
                                                   'project_profit__profit',
                                                   'project_profit__margin',

                                                   'start_date', 'end_date') \
            .filter(status__opt_numb=opt_numb_select, )

        context = {
            'menu': "projectmenu",
            'qs_statuses': qs_statuses,
            'qs_customers': qs_customers,
            'qs_projects': qs_projects,
            'opt_numb_select': opt_numb_select,

        }

        return self.render_to_response(context)


def project_create(request, template_name='home/create_project.html'):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('project_page')
    return render(request, template_name, {'form': form})


class CreateProject(View):
    template_name = 'home/create_project.html'
    success_url = 'projectpage'

    def get(self, request, *args, **kwargs):
        qs_statuses = Status.objects.all().values('id', 'opt_numb', 'current_status')
        context = {
            'qs_statuses': qs_statuses,
        }
        return render(request, self.template_name, context)
