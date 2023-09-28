from django.contrib import admin
from .models import User, Skill, Question, Notification, Answer
# Register your models here.

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Question)
admin.site.register(Notification)
admin.site.register(Answer)