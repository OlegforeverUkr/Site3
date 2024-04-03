from django.urls import path
from baskets import views

app_name = "baskets"

urlpatterns = [
    path('basket_add/<int:product_id>/', view=views.basket_add, name='basket_add'),
    path('basket_change/<int:product_id>/', view=views.basket_change, name='basket_change'),
    path('basket_remove/<int:product_id>/', view=views.basket_remove, name='basket_remove'),
]