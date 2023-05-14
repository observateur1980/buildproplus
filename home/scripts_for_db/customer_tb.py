from home.models import  Customer

customers = [
    Customer(
        customer_first_name="All",
        customer_last_name="customers",

    ),


]

Customer.objects.bulk_create(customers)
