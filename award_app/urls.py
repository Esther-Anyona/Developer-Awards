from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('new/profile/',views.new_profile, name='profile'),
    path('project/', views.project, name='project'),
    path('rating/<int:pk>/',views.rating,name='rating'),
    path('search/', views.search, name='search'),
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT)
