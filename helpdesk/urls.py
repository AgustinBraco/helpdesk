from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("admin/", admin.site.urls),
    path("clients/", include("apps.clients.urls")),
    path("comments/", include("apps.comments.urls")),
    path("employees/", include("apps.employees.urls")),
    path("files/", include("apps.files.urls")),
    path("roles/", include("apps.roles.urls")),
    path("states/", include("apps.states.urls")),
    path("tickets/", include("apps.tickets.urls")),
    path("visits/", include("apps.visits.urls")),
]
