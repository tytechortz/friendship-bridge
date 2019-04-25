from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('members/', views.member_list, name='member_list'),
    path('core_members/', views.core_members, name='core_member_list'),
    path('outer_core_members/', views.outer_core_members, name='outer_core_member_list'),
    path('event_members/', views.event_members, name='event_member_list'),
    path('members/<int:pk>', views.member_detail, name="member_detail"),
    path('members/new', views.member_create, name='member_create'),
    path('members/<int:pk>/edit', views.member_edit, name="member_edit"),
    path('members/<int:pk>/delete', views.member_delete, name='member_delete'),
]