from home.models import Project, Status, Customer

statuses = [
    Status(
        status_opt_numb=1,
        status_current_status="All statuses",
    ),
    Status(
        status_opt_numb=2,
        status_current_status="Not started",
    ),
    Status(
        status_opt_numb=3,
        status_current_status="In progress",
    ),
    Status(
        status_opt_numb=4,
        status_current_status="Completed",
    ),
    Status(
        status_opt_numb=5,
        status_current_status="Canceled",
    ),
]

Status.objects.bulk_create(statuses)
