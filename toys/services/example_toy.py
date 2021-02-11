from django.db import transaction

from toys.models import Company, Employee


def update_name():
    with transaction.atomic():
        company = Company.objects.filter(id=1).update(name="TTT toys")
        try:
            with transaction.atomic():
                for emp in Employee.objects.all():
                    emp.salary *= 10
                    emp.save()
                    raise Exception("Sorry")
        except Exception as e:
            print(e)
