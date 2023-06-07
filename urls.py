from django.urls import path
#from mypackage import views
from . import views

#url configuration
urlpatterns = [
    path('hello/', views.say_hello)

]
# "hello/" --> we always end routes w a forward slash