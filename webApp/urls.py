from django.urls import path
from webApp import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('contact',views.contact, name="contact"),
    path('portfolio',views.portfolio, name="portfolio"),
    path('services', views.services, name="services"),
    path('pricing',views.pricing,name="pricing"),
    path('blog',views.blog,name="blog"),
    path('blog-single',views.blog_single,name="blog-single"),
    path('about',views.about,name="about"),
    path('team',views.team, name="team"),
]