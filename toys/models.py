from django.db import models


class ActiveObjectsManager(models.Manager):
    def get_request(self):
        return super().get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.street


class User(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True)

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    def __str__(self):
        return self.first_name


class Tag(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Toy(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='toys', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='toys')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AdminUser(User):
    is_admin = models.BooleanField(default=True)


class ToyWithLongName(Toy):
    class Meta:
        proxy = True

    def __str__(self):
        return f" Toy with name {self.name}"
