from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('newest/', views.NewestJobsView.as_view()),
    path('<int:pk>/', views.JobsDetailView.as_view()),
]
