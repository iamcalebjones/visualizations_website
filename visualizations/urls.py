from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("plot_list", views.plot_list, name="plot_list"),
    path("choose_session", views.choose_session, name="choose_session")
]
