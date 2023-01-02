from .import views
from django.urls import path


urlpatterns = [
    path("",views.HomeView.as_view()),
    path("add/", views.Ad_data.as_view(),name="add"),
    path("delete/<int:id>/", views.Delete.as_view(), name="delete"),
    path("update/<int:id>/", views.Update.as_view(), name="edit"),


]