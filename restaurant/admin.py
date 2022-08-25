from django.contrib import admin

from restaurant.models import FoodCategory, Food


@admin.register(FoodCategory)
class EventAdmin(admin.ModelAdmin):
    ...


@admin.register(Food)
class EventAdmin(admin.ModelAdmin):
    ...