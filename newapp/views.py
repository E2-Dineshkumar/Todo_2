from rest_framework import viewsets
from newapp.serializers import TodoSerializer
from newapp.models import Todo
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    pagination_class=PageNumberPagination

