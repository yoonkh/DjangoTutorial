from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from polls.models import Question


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
    return HttpResponse("You're voting on question %s." % question_id)
