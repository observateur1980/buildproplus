from django.contrib import admin
from .models import Project, Customer, ProjectProfit, Status


class CustomerModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'first_name',
        'last_name'

    ]

    readonly_fields = ['id', ]
    list_display = ('first_name', 'last_name')

    class Meta:
        model = Customer


class ProjectModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'title',
        'status',
        'customer',
        'project_profit',
        'created_date',
        'start_date',
        'end_date',

    ]

    readonly_fields = ['id', ]
    list_display = ('title', 'status' ,
                    'customer',
                    'project_profit',
                    'created_date',
                    'start_date',
                    'end_date',)

    class Meta:
        model = Project


class ProjectProfitModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'income',
        'cost',
        'profit',
        'margin',

    ]

    readonly_fields = ['id', ]
    list_display = ('id', 'income', 'cost', 'profit', 'margin')

    class Meta:
        model = ProjectProfit


class StatusModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'current_status',

    ]

    readonly_fields = ['id', ]
    list_display = ('id', 'current_status',)

    class Meta:
        model = Status


admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Customer, CustomerModelAdmin)
admin.site.register(ProjectProfit, ProjectProfitModelAdmin)
admin.site.register(Status, StatusModelAdmin)
