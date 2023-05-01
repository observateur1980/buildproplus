from home.models import Project, Status, Customer

customers = [
    Customer(
        first_name="All",
        last_name="customers",
    ),


]

Status.objects.bulk_create(customers)
