from .forms import CreatePostForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recruit
from django.utils import timezone

# Create your views here.

def home(request):
    recruits = Recruit.objects
    return render(request, 'home.html',{'recruits' : recruits})

def detail(request,recruit_id):
    recruit_detail = get_object_or_404(Recruit, pk = recruit_id)
    return render(request,'detail.html',{'recruit_detail' : recruit_detail})

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            recruit = form.save(commit=False)
            recruit.pub_date = timezone.datetime.now()
            recruit.save()
        return redirect('/detail/' + str(recruit.id))
    else:
        form = CreatePostForm()
    return render(request, 'create.html', {'form': form})

def update(request, recruit_id):
    recruit = Recruit.objects.get(id=recruit_id)
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES, instance=recruit)
        if form.is_valid():
            recruit = form.save()
            return redirect('/detail/' + str(recruit.id))
    else:
        form = CreatePostForm(instance=recruit)
        return render(request, 'create.html', {'form': form})

def delete(request, recruit_id):
    recruit = Recruit.objects.get(id=recruit_id)
    recruit.delete()
    return redirect('home')