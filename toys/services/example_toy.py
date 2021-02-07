from django.db import transaction

from toys.models import User, Toy


def create_toy():
    with transaction.atomic():
        user = User.objects.create(first_name="test user")
        try:
            with transaction.atomic():
                toy = Toy.objects.create(name="Test toy")
                raise Exception("Uzr!")
        except Exception:
            pass
    print(user)