from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import User
from .serializers import UserSerializer

from .resources import printdoido

# @action(detail=False, methods=['get'])
# def get_users():

#   users =

#   serializer = UserSerializer(users, many=True)

#   return responses(serializer.data)
@api_view(['GET'])
def on_list_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        printdoido('Alooooooooooooo')
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

# @action(detail=True, methods=['get'])
# @renderer_classes([TemplateHTMLRenderer, JSONRenderer])


@api_view(['GET'])
def get_user(request, id):
    if request.method == 'GET':
        user = User.objects.get(id=id)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
  # Pega user pelo nome
    if request.method == 'GET':
        try:
            if request.GET['user']:

                user_name = request.GET['user']

                user = User.objects.get(name=user_name)

                serializer = UserSerializer(user)
                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Cria user
    if request.method == 'POST':

        new_user = request.data

        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Editar user
    if request.method == 'PUT':
        user_id = request.data['id']

        updated_user = User.objects.get(id=user_id)

        print(request.data)

        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
    #Deletando user
    
    if request.method == 'DELETE':
      try:
        user_to_delete = User.objects.get(pk = request.data['id'])
        
        user_to_delete.delete()
        
        return Response(status=status.HTTP_202_ACCEPTED)
      
      except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
