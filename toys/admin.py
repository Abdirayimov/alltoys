from django.contrib import admin

from toys.models import Toy, Tag, User, Company, Employee

admin.site.register(Toy)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Employee)
