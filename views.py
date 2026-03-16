from django.shortcuts import render
from .models import Question, Choice, Submission

def submit(request):

```
if request.method == "POST":
    selected_choices = request.POST.getlist('choice')

    for choice_id in selected_choices:
        choice = Choice.objects.get(id=choice_id)
        Submission.objects.create(choice=choice)

return render(request, 'result.html')
```

def show_exam_result(request):

```
submissions = Submission.objects.all()

score = 0
total = submissions.count()

for submission in submissions:
    if submission.choice.is_correct:
        score += 1

context = {
    'score': score,
    'total': total
}

return render(request, 'exam_result.html', context)
```
