from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
def index(request):
    sliders = Slider.objects.filter(is_active=True)
    about = About.objects.first()  # Берём первую запись "О нас"
    clubs = Club.objects.filter(is_active=True)
    administration = AdministrationMember.objects.all()
    education_levels = EducationLevel.objects.all()
    news = News.objects.all().order_by('-date')[:3]  # Последние 3 новости
    footer = FooterContact.objects.first()  # Данные футера
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
        'footer': footer,
    }
    return render(request, 'index.html', context)

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    footer = FooterContact.objects.first()  # Данные футера

    context = {
        'club': club,
        'footer':footer
    }
    return render(request, 'club.html', context)


def news(request,id):
    news = News.objects.get(id=id)
    footer = FooterContact.objects.first() 
    return render(request, 'news.html',{'news':news,'footer':footer})

def student(request):
    admission = Admission.objects.first()  # Берём первую запись
    footer = FooterContact.objects.first()  # Данные футера
    context = {
        'admission': admission,
        'footer': footer,
    }
    return render(request, 'student.html', context)

def specialties(request):
    clubs = Club.objects.all()  # Берём только активные специальности
    footer = FooterContact.objects.first()  # Данные футера
    context = {
        'clubs': clubs,
        'footer': footer,
    }
    return render(request, 'specialties.html', context)

def raspisanie(request):
    schedules = Schedule.objects.filter(is_active=True)  # Берём только активные расписания
    footer = FooterContact.objects.first()  # Данные футера
    schedules_with_images = [
        {
            'name': schedule.name,
            'description': schedule.description,
            'image_url': schedule.image.url if schedule.image else static('imgs/default.jpg'),
            'google_drive_link': schedule.google_drive_link
        }
        for schedule in schedules
    ]
    context = {
        'schedules': schedules_with_images,
        'footer': footer,
    }
    return render(request, 'raspis.html', context)

def rules(request):
    rule = Rule.objects.first()  # Берём первую запись
    footer = FooterContact.objects.first()  # Данные футера
    context = {
        'rule': rule,
        'footer': footer,
    }
    return render(request, 'rules.html', context)

def student_parliament(request):
    parliament = StudentParliament.objects.first()  # Берём первую запись
    footer = FooterContact.objects.first()  # Данные футера
    context = {
        'parliament': parliament,
        'footer': footer,
    }
    return render(request, 'student_parliament.html', context)

def accreditation(request):
    accreditation = Accreditation.objects.first()  # Берём первую запись
    footer = FooterContact.objects.first()  # Данные футера
    context = {
        'accreditation': accreditation,
        'footer': footer,
    }
    return render(request, 'accreditation.html', context)