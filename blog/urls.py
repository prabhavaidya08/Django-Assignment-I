from django.contrib import admin  
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from blog import views  
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index, name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about.html', views.about, name= "about"),
    path('post.html', views.post, name= "post"),
    path('contact.html', views.contact, name= "contact"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/blogger.ico')))
]


