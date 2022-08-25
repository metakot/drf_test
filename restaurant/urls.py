from django.urls import path, include

from . import views


urlpatterns = [
    path('foods/', views.CategoriesWithInnerFoodsListView.as_view()),
]