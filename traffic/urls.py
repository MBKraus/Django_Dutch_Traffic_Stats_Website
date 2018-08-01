from django.conf.urls import url

from . import views

app_name = 'traffic'

urlpatterns = [
    url(
        r"^morning/$",
        views.MorningAll.as_view(),
        name="morning"
    ),
    url(
        r"^evening/$",
        views.EveningAll.as_view(),
        name="evening"
    ),
    url(
        r"^total/$",
        views.TotalAll.as_view(),
        name="total"
    ),

]