from django.urls import path
from food.views import dish

app_name = 'food'

urlpatterns = [
    path('search/', dish, name='dish'),  # Update the name and view function
    # Other URL patterns for your app
]
