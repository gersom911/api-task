from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from drf_spectacular.utils import extend_schema,extend_schema_view
# Create your views here.
@extend_schema_view(   

    list = extend_schema(description='permite obtener una lista de tareas'),
    retrieve = extend_schema(description='permite obtener una  tareas'),
    create = extend_schema(description='permite crear una tarea'),
    update =extend_schema(description='permite va cambiar una lista de tareas'),
    destroy = extend_schema(description='permite eliminar una lista de tareas')

)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
