from django.contrib import admin
from django.urls import include, path
from schema_graph.views import Schema
from utils.constants import Urls
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter
from todos.views import (
    TodosViewSet,
    todos_home_view,
    todos_about_view,
)

routers = DefaultRouter()
routers.register("todos", TodosViewSet)

app_name = "todos"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("api/", include(routers.urls), name=Urls.TODOS_REVERSE.value),
    path("", todos_home_view, name=Urls.TODOS_HOME.value),
    path("about/", todos_about_view, name=Urls.TODOS_ABOUT.value),
    path("schema/", Schema.as_view(), name=Urls.SCHEMA_REVERSE.value),
] + debug_toolbar_urls()
