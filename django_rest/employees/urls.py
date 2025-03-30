from urls import path, include
from . import views


# class based views
urlpatterns = [
    path('emplooyees/', include(views.employees)),
    #path("/", .as_view(), name="")
]
