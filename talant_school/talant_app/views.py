from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
def index(request):
    sliders = Slider.objects.filter(is_active=True)
    about = About.objects.first()
    clubs = Club.objects.all()
    administration = AdministrationMember.objects.all()
    education_levels = EducationLevel.objects.all()
    news = News.objects.all().order_by('-date')[:3]
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = OrderForm()        

    context = {
        'sliders': sliders,
        'about': about,
        'clubs': clubs,
        'administration': administration,
        'education_levels': education_levels,
        'news': news,
        'form': form,
       
    }
    return render(request, 'index.html', context)

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    context = {
        'club': club,
    }
    return render(request, 'club.html', context)


def news(request,id):
    news = News.objects.get(id=id)
    return render(request, 'news.html',{'news':news})

def student(request):
    return render(request, 'student.html')

def specialties(request):
    return render(request, 'specialties.html')

def raspisanie(request):
    return render(request, 'raspis.html')

def rules(request):
    return render(request, 'rules.html')

def student_parliament(request):
    return render(request, 'student_parliament.html')

def accreditation(request):
    return render(request, 'accreditation.html')