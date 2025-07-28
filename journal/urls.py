from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from . import views

urlpatterns = [
    # 📝 Journal Entry Views
    path('', views.entry_list, name='entry_list'),
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('entry/new/', views.entry_new, name='entry_new'),
    path('entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry_delete'),

    # 🔐 Auth Views
    path('accounts/login/', auth_views.LoginView.as_view(template_name='journal/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', CreateView.as_view(
        template_name='journal/signup.html',
        form_class=UserCreationForm,
        success_url='/'
    ), name='signup'),
]