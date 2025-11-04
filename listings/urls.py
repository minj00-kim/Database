from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.ListingListView.as_view(), name='listing_list'),
    path('create/', views.ListingCreateView.as_view(), name='listing_create'),
    path('<slug:slug>/', views.ListingDetailView.as_view(), name='listing_detail'),
    path('<slug:slug>/edit/', views.ListingUpdateView.as_view(), name='listing_edit'),
    path('<slug:slug>/delete/', views.ListingDeleteView.as_view(), name='listing_delete'),

    path('<slug:slug>/favorite-toggle/', views.favorite_toggle, name='favorite_toggle'),
    path('<slug:slug>/report/', views.report_view, name='report'),
    path('<slug:slug>/message/', views.message_create, name='message_create'),

    path('my-messages/', views.MyMessageListView.as_view(), name='my_messages'),
]
