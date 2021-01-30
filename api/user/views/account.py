from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from api.user.serializers.user import AccountSerializer, AccountListSerializer

from api.user.utils.role import account_role
from apps.user.models import Account
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ValidationError

User = get_user_model()


class RegisterUserAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            phone_number = data['phone_number']
            password = data['password']
            user_role = data['role']
        except KeyError:
            return Response({'error': 404})
        check_user = User.objects.filter(phone_number=phone_number)
        if check_user.exists():
            return Response({'error': 500})
        else:
            new_user = User.objects.create_user(phone_number, password)
            token, _ = Token.objects.get_or_create(user=new_user)
            user = User.objects.get(phone_number=phone_number).id
            data['user'] = user
            if account_role(user_role, user):
                serializer = AccountSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"status": 200})
            else:
                return Response({'error': 500})


class LoginUserAPIView(APIView):
    """
            post:
            Login users.
    """

    def post(self, request):
        data = request.data
        try:
            phone_number = data['phone_number']
            password = data['password']
        except KeyError:
            return Response({'error': 404})
        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        else:
            token, _ = Token.objects.get_or_create(user=user)
            role = {
                'is_director': user.is_director,
                'is_accountant': user.is_accountant,
                'is_warehouseman': user.is_warehouseman,
                'is_staff': user.is_staff,
                'is_driver': user.is_driver,
                'is_manager': user.is_manager,
                'is_chief_technological_man': user.is_chief_technological_man,
                'is_chief_specialist': user.is_chief_specialist
            }
            return Response({'status': 200, 'token': token.key, 'user_id': user.id, 'role': role})


class FilterUserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        role = request.query_params.get('role', None)
        if role == 'staff':
            accounts = Account.objects.filter(user__is_staff=True)
        elif role == 'director':
            accounts = Account.objects.filter(user__is_director=True)
        elif role == 'accountant':
            accounts = Account.objects.filter(user__is_accountant=True)
        elif role == 'warehouseman':
            accounts = Account.objects.filter(user__is_warehouseman=True)
        elif role == 'driver':
            accounts = Account.objects.filter(user__is_driver=True)
        elif role == 'manager':
            accounts = Account.objects.filter(user__is_manager=True)
        elif role == 'chief_technological_man':
            accounts = Account.objects.filter(user__is_chief_technological_man=True)
        elif role =='chief_specialist':
            accounts = Account.objects.filter(user__is_chief_specialist=True)
        else:
            return Response({'error': 404})
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)


class AccountListAPIView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer

    def get_object(self, pk):
        try:
            return Account.objects.get(id=pk)
        except Account.DoesNotExist:
            raise ValidationError('object not found')

    def list(self, request):
        queryset = Account.objects.all()
        serializer = AccountListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = self.get_object(pk)
        serializer = AccountListSerializer(queryset, many=False)
        return Response(serializer.data)


