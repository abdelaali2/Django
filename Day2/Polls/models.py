from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Answer(models.Model):
    title = models.CharField(_("Answer"), max_length=50)
    
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    title = models.CharField(_("Question Title"), max_length=50)
    question_text = models.TextField()
    pub_date = models.DateTimeField(_("Published at"), auto_now_add=True)
    answers = models.ManyToManyField(Answer, verbose_name=_("Answers"))
    
    def __str__(self):
        return self.title