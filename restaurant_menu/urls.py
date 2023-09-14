from django.urls import path 
from . import views 

# NOTE: as_view() METHOD WAS USED BECAUSE THE VIEW IS A CLAA BASED VIEW /
# APP 17 HAS A FUNCTION BASED VIEW

urlpatterns = [
        path('',views.MenuList.as_view(),name='home'),
        path('item/<int:pk>/',views.MenuItemDetail.as_view(),name='item_menu') # item/<int:pk> IS A DYNAMIC URL WHERE pk IS A PRIMARY KEY

]