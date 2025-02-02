from django.urls import path
from .views import all_faqs, specific_faq

urlpatterns = [
    path('', all_faqs, name = 'all_faqs'),
    path('<int:pk>/',specific_faq, name = 'specific_faq')
]