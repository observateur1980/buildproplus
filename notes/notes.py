class ProjectProfit(models.Model):
    project_profit_income = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    project_profit_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    project_profit_profit = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    project_profit_margin = models.FloatField(null=True, blank=True, default=0.00)

    class ProjectProfitModelAdmin(admin.ModelAdmin):
        fields = [
            'id',
            'project_profit_income',
            'project_profit_cost',
            'project_profit_profit',
            'project_profit_margin',

        ]

        readonly_fields = ['id', ]
        list_display = (
        'id', 'project_profit_income', 'project_profit_cost', 'project_profit_profit', 'project_profit_margin')

        class Meta:
            model = ProjectProfit
