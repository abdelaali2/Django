from django.contrib import admin
from Polls.models import Question, Answer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Question.answers.through


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
