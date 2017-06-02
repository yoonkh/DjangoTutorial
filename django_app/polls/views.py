from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Question, Choice
from django.urls import reverse


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = get_list_or_404(
        Question.objects.order_by('-pub_date')[:5]
    )

    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question_id 가 pk인 Question객체를 가져와
    # context라는 이름을 가진 dict에 'question'이라는 키 값으로 위 변수를 할당
    # 이후 'polls/detail.html'과 context를 렌더한 결과를 리턴

    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist as e:
    #     raise Http404('Question does not exist')
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice",
            )
            return redirect('polls:detail', question_id)


    else:
        return HttpResponse("You're voting on questoin %s." % question_id)
