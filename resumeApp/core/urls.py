from django.urls import path
from . import views
urlpatterns = [

    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('project/',views.project,name='project'),
    path('add_project/',views.add_project,name='add_project'),
    path('update_project/<int:pk>',views.update_project,name='update_project'),
    path('delete_project/<int:pk>',views.delete_project,name='delete_project'),
    path('project_images/',views.project_images,name='project_images'),



    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('update_about/<int:pk>',views.update_about,name='update_about'),
    path('education/',views.education,name='education'),
    path('add_education/',views.add_education,name='add_education'),
    path('update_education/<int:pk>',views.update_education,name='update_education'),
    path('delete_education/<int:pk>',views.delete_education,name='delete_education'),
    path('update_interest/<int:pk>',views.update_interest,name='update_interest'),
    path('delete_interest/<int:pk>',views.delete_interest,name='delete_interest'),
    path('reference/',views.reference,name='reference'),
    path('add_reference/',views.add_reference,name='add_reference'),
    path('update_reference/<int:pk>',views.update_reference,name='update_reference'),
    path('delete_reference/<int:pk>',views.delete_reference,name='delete_reference'),




] 