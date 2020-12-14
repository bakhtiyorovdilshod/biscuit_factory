from django.contrib.auth import get_user_model
User = get_user_model()


def account_role(user_role, user_id):
    user = User.objects.get(id=user_id)
    if user_role == 'director':
        user.is_director = True
        user.save()
        return True
    elif user_role == 'accountant':
        user.is_accountant = True
        user.save()
        return True
    elif user_role == 'warehouseman':
        user.is_warehouseman = True
        user.save()
        return True
    elif user_role == 'staff':
        user.is_staff = True
        user.save()
        return True
    elif user_role == 'driver':
        user.is_driver = True
        user.save()
    elif user_role == 'manager':
        user.is_manager = True
        user.save()
        return True
    elif user_role == 'chief_technological_man':
        user.is_chief_technological_man = True
        user.save()
        return True
    elif user_role == 'chief_specialist':
        user.is_chief_specialist = True
        user.save()
        return True
    else:
        return False
