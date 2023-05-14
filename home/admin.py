from django.contrib import admin
from .models import Project, Customer, ProjectProfit, Status, Unvan


class role_inlineCustomerProject(admin.TabularInline):
    model = Project
    extra = 0


class role_inlineCustomerAddress(admin.TabularInline):
    model = Unvan
    extra = 0


class CustomerModelAdmin(admin.ModelAdmin):
    inlines = (role_inlineCustomerProject, role_inlineCustomerAddress)

    fields = [
        'id',
        'customer_first_name',
        'customer_last_name',
        'customer_email',


    ]

    readonly_fields = ['id', ]
    list_display = ('customer_first_name', 'customer_last_name', 'customer_email')

    class Meta:
        model = Customer


class ProjectModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'project_title',
        'status',
        'customer',
        'project_profit',
        'project_created_date',
        'project_start_date',
        'project_end_date',

    ]

    readonly_fields = ['id', ]
    list_display = ('project_title', 'status',
                    'customer',
                    'project_profit',
                    'project_created_date',
                    'project_start_date',
                    'project_end_date',)

    class Meta:
        model = Project


class ProjectProfitModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'project_profit_income',
        'project_profit_cost',
        'project_profit_profit',
        'project_profit_margin',

    ]

    readonly_fields = ['id', ]
    list_display = ('id', 'project_profit_income', 'project_profit_cost', 'project_profit_profit', 'project_profit_margin')

    class Meta:
        model = ProjectProfit


class StatusModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'status_opt_numb',
        'status_current_status',

    ]

    readonly_fields = ['id', ]
    list_display = ('id', 'status_opt_numb', 'status_current_status',)

    class Meta:
        model = Status


class UnvanModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'unvan_title',
        'unvan_city',
        'unvan_state',
        'unvan_zip',
        'unvan_created_date',

    ]

    readonly_fields = ['id', ]
    list_display = ('unvan_title', 'unvan_city',
                    'unvan_state',
                    'unvan_zip',
                    'unvan_created_date',
                    )

    class Meta:
        model = Unvan


admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Customer, CustomerModelAdmin)
admin.site.register(ProjectProfit, ProjectProfitModelAdmin)
admin.site.register(Status, StatusModelAdmin)
admin.site.register(Unvan, UnvanModelAdmin)
