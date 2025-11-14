from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("admin/", admin.site.urls),
    path("attachments/", include("apps.attachments.urls")),
    path("interactions/", include("apps.interactions.urls")),
    path("roles/", include("apps.roles.urls")),
    path("tickets/", include("apps.tickets.urls")),
    path("users/", include("apps.users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
