from django.contrib.auth import get_user_model
User = get_user_model()


def account_role(user_role, user_id):
    user = User.objects.get(id=user_id)
    if user_role == 'director':
        user.is_director = True
    elif user_role == 'accountant':
        user.is_accountant = True
    elif user_role == 'warehouseman':
        user.is_warehouseman = True
    elif user_role == 'staff':
        user.is_staff = True
    elif user_role == 'driver':
        user.is_driver = True
    elif user_role == 'manager':
        user.is_manager = True
    elif user_role == 'chief_technological_man':
        user.is_chief_technological_man = True
    elif user_role == 'chief_specialist':
        user.is_chief_specialist = True
    user.save()