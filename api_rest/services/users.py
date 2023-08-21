from sqlite3 import IntegrityError
from rest_framework.exceptions import APIException


from ..models import User


class ServiceUser():

    def list_core(self):
        qs = User.objects.all()
        return qs

    def list_users(self):
        # users = User.objects.all()
        qs = self.list_core()
        return qs

    def get_user(self, pk):
        try:
            user = self.list_users().get(pk=pk)
            return user
        except User.DoesNotExist:
            raise APIException('Pessoa não cadastrada!')

    def save_user(self, user_data):
        try:
            user_obj, created = User.objects.update_or_create(
                id=user_data.get('id'),
                defaults={
                    'nickname': user_data.get('nickname'),
                    'name': user_data.get('name'),
                    'email': user_data.get('email'),
                    'age': user_data.get('age'),
                }
            )
            return (user_obj, created)
        except IntegrityError:
            raise APIException('User já cadastrado!')

    def delete_user(self, pk):
        user = self.get_user(pk)
        user.delete()
        return user
