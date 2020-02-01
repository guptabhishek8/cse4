from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^signin/', views.signin, name="signin"),
    url(r'^postsignin/', views.postsignin, name="postsignin"),
    url(r'^termspage/', views.termspage, name="termspage"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^home/', views.home, name="home"),
    url(r'^signout/', LogoutView.as_view(next_page='index'), name="logout"),
    url(r'^domain/', views.domain, name="domain"),

]
