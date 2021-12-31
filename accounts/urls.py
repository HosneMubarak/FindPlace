from django.urls import path
from .views import user_account_activate, TestView

urlpatterns = [
    path('', TestView.as_view(), name='test_view'),
    path('api/activate/<uid>/<token>', user_account_activate,
         name='user_account_activate'),
]
