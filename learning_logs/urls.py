"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    
    #Show all topics
    path('topics/', views.topics, name="topics"),
    
    #Show main topics
    path('main_topics/', views.main_topics, name="main_topics"),
    
    #Detail page for a single topic
    path('topics/(?P<topic_id>\d+)/', views.topic, name="topic"),
    
     #Detail page for a single main topic
    path('main_topic/(?P<maintopic_id>\d+)/', views.main_topic, name="main_topic"),
    
    #Making new topic
    path('new_topic/(?P<maintopic_id>\d+)/', views.new_topic, name="new_topic"),
    
    #path('new_topic/\\(\\?P(?P<maintopic_id>[^/]+)\\\\d\\+\\)/$', views.new_topic, name="new_topic"),
    
    #Making new main topic
    path('new_main_topic/', views.new_main_topic, name="new_main_topic"),
    
    #Making new entry
    path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name="new_entry"),
    
    #Editing existing entry
    path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name="edit_entry"),
    
    #Delete entry
    path('delete_entry/(?P<entry_id>\d+)/', views.delete_entry, name = "delete_entry"),
    
    #path('new_topic/', views.new_topic, name='new_topic')
]