from django.urls import path

from theatre.urls import urlpatterns

from plays.views import ShowDetailView

urlpatterns = [
    path('<int:pk>', ShowDetailView.as.view())
]