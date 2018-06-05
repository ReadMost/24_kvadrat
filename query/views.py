from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Home, Comment
from django.urls import reverse
from django.utils import timezone

def index(request):
    home_list = Home.objects.order_by('-pub_date')
    context = {'home_list': home_list}
    return render(request, 'query/index.html', context)
def detail(request, home_id):
    home = get_object_or_404(Home, pk=home_id)
    return render(request, 'query/detail.html', {'home': home})

def results(request, home_id):
    response = "You're looking at the results of Home %s."
    return HttpResponse(response % home_id)
def vote(request, home_id):
    home = get_object_or_404(Home, pk=home_id)

    selected_home = Home.objects.get(pk=home_id)
    selected_home.comment_set.create(comment_text=request.POST["comment"])
    return HttpResponseRedirect(reverse('query:detail', args=(home.id,)))
def form(request):
    return render(request, 'query/form.html')
def save(request):
    h = Home(
    home_title=request.POST["home_title"],
    home_description = request.POST["home_description"],
    home_room = int(request.POST["home_room"]),
    home_price = int(request.POST["home_price"]),
    home_type = request.POST["home_type"],
    home_image = request.POST["home_image"],
    pub_date = timezone.now(),
    )
    h.save()
    if request.POST.get("enter")=="Enter":
        return HttpResponseRedirect(reverse('query:index'))
    elif request.POST.get("add")=="Add another":
        return HttpResponseRedirect(reverse('query:form'))



