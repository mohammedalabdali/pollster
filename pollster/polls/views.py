from django.shortcuts import render

from .models import Question,Choice


#get question and view them
def index(request):
    question_list=Question.objects.order_by('-pub_date')[:5]
    context={'question_list':question_list}
    return render(request,'polls/index.html',context)

#show specific question
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
        context={'question':question}
    except Question.DoesNotExist:
        raise Http404('question dose not exists')
    return render(request,'polls/detail.html',context)

#show result of votes for specific question
def result(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={'question':question}
    return render(request,'polls/result.html',context)