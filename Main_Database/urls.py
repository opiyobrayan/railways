
from django.urls import path
from . import views
from .views import AddArticleView


urlpatterns = [
    path('', views.home,name='home'),
    path('activities/', views.Activities,name='activities'),
    path('activities/<pk>/',views.add_participant,name='add-participant'),
    path('htmx/activity-form/',views.create_activity_form,name='activity-form'),
    path('htmx/participant/<pk>/',views.detail_participant,name='participant-detail'),
    path('registered-participant/<pk>',views.register_participant,name='registered-participant'),
    path('htmx/participant/<pk>/update',views.update_participant,name='update-participant'),
    path('htmx/participant/<pk>/delete',views.delete_participant,name='delete-participant'),
    path('home-poll',views.homepoll,name='home-poll'),
    path('create-poll',views.create_poll,name='create-poll'),
    path('result-poll/<poll_id>',views.result_poll,name='result-poll'),
    path('vote-poll/<poll_id>',views.vote_poll,name='vote-poll'),
    path('home-input',views.homeinput,name='home-input'),
    path('activity-input',views.register_activity,name='activity-input'),
    path('project-input',views.register_project,name='project-input'),
    path('participant-input',views.register_participant,name='participant-input'),
    path('organization-input',views.register_organization,name='organization-input'),
    path('add-report',AddArticleView.as_view(), name='add-article'),

]
