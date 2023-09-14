from django.shortcuts import render 
from django.views import generic
from .models import Item, MEAL_TYPE

# THIS IS A CLASS BASED VIEW

# EACH OF THIS CLASSES ARE DESIGNEXD FOR A VERY PARTICULAR TYPE OF PAGE

class MenuList(generic.ListView):
#  THIS TYPE OF CLASS IS DESIGNED FOR PAGES THAT HAVE MANY DATA TO DISPLAY SUCH AS FRONT OF PAGE OF BLOGS WITH MANY LINKS
 # IN SHORT IT DISPLAYS A LIST OF DATA
    queryset = Item.objects.order_by("-date_created") # The minus does the ordering in reverse
    template_name = "index.html"  

    def get_context_data(self, **kwargs): # THIS IS ALSO  PRE_DEFINED METHOD NAME 
        context = super().get_context_data(**kwargs) 
        context['meals'] = MEAL_TYPE
        return context 

        # context is a dictionary in which it keys can be accessed in html code and the value is display
        # CONTEXT IS USED FOR SENDING DATA FROM PYTHON TO HTML


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item.html"


