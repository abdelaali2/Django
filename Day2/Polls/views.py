from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from Polls.models import Question

# Create your views here.

class MyLoginView(LoginView):
    template_name = 'my_login.html'

class MyLogoutView(LogoutView):
    next_page = '/'

def view_all_Questions(req):
    questions_list = Question.objects.all()
    customContext = {"questionsList": questions_list}
    return render(req, "questions_index.html", context=customContext)


# @login_required
def view_question_details(req, q_id):
    question = get_object_or_404(Question, pk=q_id)
    customContext = {"question": question}
    return render(req, "question_details.html", context=customContext)
