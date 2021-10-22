from django.urls import path
from . import views

urlpatterns = [
    # path that will hook up the root URL of the app to the project_index view
    path("", views.project_index, name="project_index"),
    # path to the specific project
    # note that rather than having the first parameter empty have to have the pk num
    path("<int:pk>/", views.project_detail, name="project_detail"),
]