from django.contrib import admin

from myapp.models import studentModel

# myapp theke models er vitore studentmodel ke import korlam

admin.site.register(studentModel)


# createsuperuser toiri korlam username:admin   password:1234