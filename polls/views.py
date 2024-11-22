from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice

def index(request):
    """
    Display the latest poll questions.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered index page with the latest polls.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

def detail(request, question_id):
    """
    Display details of a specific poll question.

    Parameters:
    request (HttpRequest): The HTTP request object.
    question_id (int): The ID of the question to display.

    Returns:
    HttpResponse: Rendered detail page for the specified question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    Display the results of a specific poll question.

    Parameters:
    request (HttpRequest): The HTTP request object.
    question_id (int): The ID of the question whose results to display.

    Returns:
    HttpResponse: Rendered results page for the specified question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required  # Ensure the user is logged in before voting
def vote(request, question_id):
    """
    Process a vote for a specific poll question.

    Parameters:
    request (HttpRequest): The HTTP request object.
    question_id (int): The ID of the question being voted on.

    Returns:
    HttpResponseRedirect: Redirects to the results page after voting.
    """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice."
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    else:
        # Handle non-POST requests if needed (e.g., GET)
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Invalid request method."
        })
