from django.contrib import admin
from django.urls import path
from schema_graph.views import Schema
from utils.constants import Urls
from debug_toolbar.toolbar import debug_toolbar_urls
from todos.views import index

app_name = "todos"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos", index, name=Urls.TODOS_REVERSE.value),
    path("schema/", Schema.as_view(), name=Urls.SCHEMA_REVERSE.value),
] + debug_toolbar_urls()
