from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destino/', views.destino, name='destino'),
    path('students/', views.students, name='students'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('programs/', views.programs, name='programs'),
    path('stages/', views.stages, name='stages'),
    path('categories/', views.categories, name='categories'),
    path('results/', views.results, name='results'),
    path('teams/', views.teams, name='teams'),
    path('images/', views.images, name='images'), 
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
