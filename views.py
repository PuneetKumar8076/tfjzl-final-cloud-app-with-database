from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == "POST":
        selected_choices = request.POST.getlist('choice')

        submission = Submission.objects.create()

        for choice_id in selected_choices:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)

        return redirect('onlinecourse:show_exam_result',
                        course_id=course.id,
                        submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):

    submission = get_object_or_404(Submission, pk=submission_id)

    choices = submission.choices.all()

    score = 0
    total = choices.count()

    for choice in choices:
        if choice.is_correct:
            score += 1

    context = {
        'score': score,
        'total': total,
        'course': course_id
    }

    return render(request, 'exam_result_bootstrap.html', context)
