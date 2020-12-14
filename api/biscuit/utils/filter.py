from rest_framework import filters
from django.db.models import Q

from apps.biscuit.models import Biscuit
from apps.client.models import Client
from apps.user.models import Account


def convert_query_params_to_dict(query_params):
    data = {}
    data['created_date'] = query_params.get('date_one', None)
    data['status'] = query_params.get('status', None)
    data['created_date_two'] = query_params.get('date_two', None)
    data['biscuit'] = query_params.get('biscuit', None)
    data['client'] = query_params.get('client', None)
    return data


def convert_biscuit_query_params_to_dict(query_params):
    data = {}
    data['created_date'] = query_params.get('date_one', None)
    data['created_date_two'] = query_params.get('date_two', None)
    data['status'] = query_params.get('status', None)
    data['biscuit'] = query_params.get('biscuit', None)
    data['staff'] = query_params.get('staff', None)
    return data


class SaleBiscuitFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        data = convert_query_params_to_dict(request.query_params)
        data = {k: v for k, v in data.items() if v is not None}
        if 'client' in data:
            client_company = data['client']
            client = Client.objects.filter(company=client_company)
            if client.exists():
                data['client'] = str(client.first().id)
            else:
                data['client'] = str(-1)
        if 'biscuit' in data:
            biscuit_name = Biscuit.objects.filter(name=data['biscuit'])
            if biscuit_name.exists():
                data['biscuit'] = str(biscuit_name.first().id)
            else:
                data['biscuit'] = str(-1)
        if 'created_date' in data and 'created_date_two' in data:
            queryset = queryset.filter(created_date__range=[data['created_date'], data['created_date_two']])
            data.pop('created_date')
            data.pop('created_date_two')
            queryset.filter(**data)
            return queryset
        return queryset.filter(**data)


class AddBiscuitFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        data = convert_query_params_to_dict(request.query_params)
        data = {k: v for k, v in data.items() if v is not None}
        if 'staff' in data:
            first_name = data['staff']
            staff = Account.objects.filter(first_name=first_name)
            if staff.exists():
                data['staff'] = str(staff.first().id)
            else:
                data['staff'] = str(-1)
        if 'biscuit' in data:
            biscuit_name = Biscuit.objects.filter(name=data['biscuit'])
            if biscuit_name.exists():
                data['biscuit'] = str(biscuit_name.first().id)
            else:
                data['biscuit'] = str(-1)
        if 'created_date' in data and 'created_date_two' in data:
            queryset = queryset.filter(created_date__range=[data['created_date'], data['created_date_two']])
            data.pop('created_date')
            data.pop('created_date_two')
            queryset.filter(**data)
            return queryset
        return queryset.filter(**data)