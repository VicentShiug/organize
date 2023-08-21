from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from ..models import User
from ..serializers import UserSerializer
from ..services import ServiceUser

class UserResource(viewsets.ViewSet, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = ServiceUser
    
    def get_service(self):
        service = ServiceUser()
        return service
    
    
    def get_object(self, pk=None):
        service = self.get_service()
        pessoa = service.get_user(pk)
        return pessoa

    @action(detail=False, methods=['get'])
    def on_list_users(self, request):
        users = self.get_service().list_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['get'])
    def get_user(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    @action(detail=False, methods=['post', 'put'])
    def on_save_user(self, request):
        service = self.get_service()
        user, created = service.save_user(request.data)
        serializer = UserSerializer(user)
        results = {}
        results['results'] = serializer.data
        results['detail'] = 'Usuário criado com sucesso!' if created else 'Usuário atualizado com sucesso!'
        return Response(results, status=201 if created else 202)
    
    
    @action(detail=True, methods=['delete'])
    def on_delete_user(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        results = {}
        results['detail'] = 'Usuário deletado com sucesso!'
        return Response(results, status=202)
    
    @action(detail=False, methods=['get'])
    def get_user_by_name(self, request):
        user_name = request.GET['name']
        user = User.objects.get(name=user_name)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def get_user_by_email(self, request):
        user_email = request.GET['email']
        user = User.objects.get(email=user_email)
        serializer = UserSerializer(user)
        return Response(serializer.data)
