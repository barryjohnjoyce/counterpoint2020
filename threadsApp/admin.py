from django.contrib import admin
from .models import ThreadSubject, Thread, ThreadComment

admin.site.register(ThreadSubject)
admin.site.register(Thread)
admin.site.register(ThreadComment)