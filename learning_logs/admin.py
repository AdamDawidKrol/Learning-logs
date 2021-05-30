from django.contrib import admin
from learning_logs.models import Topic
from learning_logs.models import Entry
from learning_logs.models import Students
from learning_logs.models import MainTopic

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Students)
admin.site.register(MainTopic)

# Register your models here.
