from todos.serializers import TodoSerializer
from rest_framework import generics
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


class TodosListView(generics.ListCreateAPIView):
    """
    class with mixins to List & Create Todos
    """

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [ApiPermissionOrReadOnly]


todos_list_view = TodosListView.as_view()


class TodosDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    class with mixins to Reretrive, Update & Delete Todos
    """

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [ApiPermissionOrReadOnly]


todos_detail_view = TodosDetailView.as_view()
