from django.urls import path
from django.views.generic import TemplateView

from centers.views import index, city_index, center_list, center_view, centers_json

urlpatterns = [
    path("", index, name="centers_index"),
    path("<int:city_id>/", city_index, name="centers_city_index"),
    path("<int:city_id>-/", center_list, name="center_list"),
    path("<int:city_id>-<int:neighborhood_id>/", center_list, name="center_list"),
    path("center/<int:center_id>", center_view, name="center"),
    path("centers.json", centers_json, name="centers_json"),
    path("map", TemplateView.as_view(template_name="centers/map.html"), name="centers_map"),
]
