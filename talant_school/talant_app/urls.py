from . import  views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('club/<int:club_id>/', views.club_detail, name='club_detail'),
    path('news/<int:id>', views.news,name='news'),
    path('student/', views.student,name='student'),
    path('specialties/', views.specialties, name='specialties'),
   path('raspisanie/', views.raspisanie, name='raspisanie'),
   path('rules/', views.rules, name='rules'),
   path('student-parliament/', views.student_parliament, name='student_parliament'),
   path('accreditation/', views.accreditation, name='accreditation'),   
]
