from django.contrib import admin
from .models import Question, Choice, UserResponse

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserResponse)
