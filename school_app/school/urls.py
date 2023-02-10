from django.urls import path, include
from . import views
from .teachers import views as tviews
from .parents import views as pviews

teachers_urls = [
    path("",tviews.home, name = "home"),
    path("classes/",tviews.classes, name = "classes")
]

parents_urls = [
    path("",pviews.home, name = "home"),
]

urlpatterns = [
    path("teachers/",include(teachers_urls)),
    path("parents/",include(parents_urls))

]