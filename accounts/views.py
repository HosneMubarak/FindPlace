from .models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
from requests.exceptions import HTTPError
from django.conf import settings

# importing base_url from settings
BASE_URL = settings.BASE_URL


class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        context = {
            "msg": f"If you are authenticated then you can see this and your email is {request.user.email}",
        }
        return Response(context)

@api_view(['GET', ])
def user_account_activate(request, uid, token):
    print('user_account_activate()', uid, token)

    try:
        account_activate_url = BASE_URL + "auth/users/activation/"
        response = requests.post(
            account_activate_url,
            headers={
                "Content-Type": "application/json",
            },
            json={
                'uid': uid,
                'token': token,
            },
            verify=False
        )

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'user_account_activate_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'user_account_activate_api(): Other error occurred: {err}')
    else:
        print('user_account_activate_api(): Success!')

    if response.status_code == 204:
        context = {
            'message': 'account successfully created!'
        }
        return Response(context)
    else:
        context = {
            'message': 'account has not been created! please check'
        }
    return Response(context)
