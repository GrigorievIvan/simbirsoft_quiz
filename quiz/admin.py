from django.contrib import admin
from .models import Answer, Answers, Choice, Question, Quiz

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Answers)
admin.site.register(Choice)
admin.site.register(Quiz)