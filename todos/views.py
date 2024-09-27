from todos.serializers import TodoSerializer
from rest_framework import generics, viewsets
from utils.custom_permissions import ApiPermissionOrReadOnly
from django.views.generic import TemplateView
from utils.constants import Templates
from todos.models import Todo


class TodosHomeView(TemplateView):
    template_name = Templates.INDEX.value


todos_home_view = TodosHomeView.as_view()


class TodosAboutView(TemplateView):
    template_name = Templates.ABOUT.value


todos_about_view = TodosAboutView.as_view()


class TodosViewSet(viewsets.ModelViewSet):
    """
    class with mixins to List & Create Todos
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [ApiPermissionOrReadOnly]
