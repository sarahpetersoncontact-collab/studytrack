from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subject = request.POST.get("subject")
        deadline = request.POST.get("deadline")

        if title and subject and deadline:
            Task.objects.create(
                title=title,
                subject=subject,
                deadline=deadline
            )

        return redirect("index")

    tasks = Task.objects.all().order_by("deadline")

    return render(request, "planner/index.html", {
        "tasks": tasks
    })
def complete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()

    return redirect("index")


def delete_task(request, task_id):
    if request.method == "POST":
        Task.objects.filter(id=task_id).delete()

    return redirect("index")