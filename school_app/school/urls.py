from django.urls import path, include
from . import views
from .teachers import views as tviews
from .parents import views as pviews
from .auth import views as aviews


auth_urls = [
    path("login/",aviews.login_user, name = "login"),
    path("logout/",aviews.logout_user, name = "logout")
]

teachers_urls = [
    path("",tviews.home, name = "teachers_home"),
    path("classes/",tviews.classes, name = "classes")
]

parents_urls = [
    path("",pviews.home, name = "home"),
]

urlpatterns = [
    path("auth/",include(auth_urls)),
    path("teachers/",include(teachers_urls)),
    path("parents/",include(parents_urls))

]