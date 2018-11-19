"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from collection import views
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from collection.backends import MyRegistrationView

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('voiceoverequpiments/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    # adding slugs as equipment is added:
    path('voiceoverequipments/<slug>/', views.voiceoverequipment_detail, name='voiceoverequipment_detail'),
    path('voiceoverequipments/<slug>/edit/', views.edit_voiceoverequipment, name='edit_voiceoverequipment'),
    # redirect view:    
    path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
     # our new browse flow:
    path('browse/name/', views.browse_by_name, name='browse'),
    path('browse/name/<initial>/', views.browse_by_name, name='browse_by_name'),
    # PW reset URLs:
    path('accounts/password/reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="password_reset"), 
    path('accounts/password/reset/done/', PasswordResetView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
    # registration
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/create_voiceoverequipment/', views.create_voiceoverequipment, name='registration_create_voiceoverequipment'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


