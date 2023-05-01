from home.models import Project, Status, Customer

statuses = [
    Status(
        opt_numb=1,
        current_status="All statuses",
    ),
    Status(
        opt_numb=2,
        current_status="Not started",
    ),
    Status(
        opt_numb=3,
        current_status="In progress",
    ),
    Status(
        opt_numb=4,
        current_status="Completed",
    ),
    Status(
        opt_numb=5,
        current_status="Canceled",
    ),
]

Status.objects.bulk_create(statuses)
