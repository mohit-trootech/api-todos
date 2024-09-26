from django.contrib import admin
from django.urls import include, path
from schema_graph.views import Schema
from utils.constants import Urls
from debug_toolbar.toolbar import debug_toolbar_urls
from todos.views import (
    todos_list_view,
    todos_detail_view,
    todos_home_view,
    todos_about_view,
)

app_name = "todos"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", todos_home_view, name=Urls.TODOS_HOME.value),
    path("about/", todos_about_view, name=Urls.TODOS_ABOUT.value),
    path("todos/", todos_list_view, name=Urls.TODOS_REVERSE.value),
    path("todos/<int:pk>/", todos_detail_view, name=Urls.TODO_DETAIL_REVERSE.value),
    path("schema/", Schema.as_view(), name=Urls.SCHEMA_REVERSE.value),
] + debug_toolbar_urls()
