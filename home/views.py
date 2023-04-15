from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic.base import TemplateView

from home.models import Project, Status, Customer


# Create your views here.


class Index(TemplateView):
    template_name = 'home/index.html'


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'




class ProjectPage(LoginRequiredMixin, TemplateView):
    template_name = 'home/project.html'

    def post(self, request, *args, **kwargs):

        status_id = int(request.POST['status'])
        customer_id = int(request.POST['customer'])

        qs_statuses = Status.objects.all().values('id', 'current_status')
        qs_customers = Customer.objects.all().values('id', 'first_name', 'last_name')
        if status_id == 1 and customer_id == 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date')
        elif status_id != 1 and customer_id == 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date') \
                .filter(status__id=status_id, customer__id__gt=1)
        elif status_id != 1 and customer_id != 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date') \
                .filter(status__id=status_id, customer__id=customer_id)
        elif status_id == 1 and customer_id != 1:
            qs_projects = Project.objects.all().values('id', 'title', 'customer__id',
                                                       'customer__first_name',
                                                       'customer__last_name',

                                                       'project_profit__income',
                                                       'project_profit__cost',
                                                       'project_profit__profit',
                                                       'project_profit__margin',

                                                       'start_date', 'end_date') \
                .filter(status__id__gt=1, customer__id=customer_id)

        context = {
            'menu': "homemenu",
            'qs_statuses': qs_statuses,
            'qs_customers': qs_customers,
            'qs_projects': qs_projects,
            'status_id': status_id,
            'customer_id': customer_id,

        }

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        status_id = 2
        qs_statuses = Status.objects.all().values('id', 'current_status')
        qs_customers = Customer.objects.all().values('id', 'first_name', 'last_name')
        qs_projects = Project.objects.all().values('id', 'title', 'customer__id',

                                                   'customer__first_name',
                                                   'customer__last_name',

                                                   'project_profit__income',
                                                   'project_profit__cost',
                                                   'project_profit__profit',
                                                   'project_profit__margin',

                                                   'start_date', 'end_date') \
            .filter(status__id=status_id, )

        context = {
            'menu': "projectmenu",
            'qs_statuses': qs_statuses,
            'qs_customers': qs_customers,
            'qs_projects': qs_projects,
            'status_id': status_id,

        }

        return self.render_to_response(context)
