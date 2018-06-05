from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Home_buyer, Comment
from django.urls import reverse
from django.utils import timezone
def index(request):
    home_list = Home_buyer.objects.order_by('-pub_date')
    context = {'home_list': home_list}
    return render(request, 'query_buyer/index.html', context)
def detail(request, home_buyer_id):
    home = get_object_or_404(Home_buyer, pk=home_buyer_id)
    return render(request, 'query_buyer/detail.html', {'home': home})

def results(request, home_buyer_id):
    response = "You're looking at the results of Home %s."
    return HttpResponse(response % home_buyer_id)
def vote(request, home_buyer_id):
    home = get_object_or_404(Home_buyer, pk=home_buyer_id)

    selected_home = Home_buyer.objects.get(pk=home_buyer_id)
    selected_home.comment_set.create(comment_text=request.POST["comment"])
    return HttpResponseRedirect(reverse('query_buyer:detail', args=(home.id,)))

def form(request):
    return render(request, 'query_buyer/form.html')
def save(request):
    h = Home_buyer(
    home_description = request.POST["home_description"],
    home_room = int(request.POST["home_room"]),
    home_price_start = int(request.POST["home_price_start"]),
    home_price_finish=int(request.POST["home_price_finish"]),
    home_type = request.POST["home_type"],
    pub_date = timezone.now(),
    )
    h.save()
    if request.POST.get("enter")=="Enter":
        return HttpResponseRedirect(reverse('query_buyer:index'))
    elif request.POST.get("add")=="Add another":
        return HttpResponseRedirect(reverse('query_buyer:form'))

