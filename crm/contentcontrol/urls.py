from crm.urls import path, include
from . import views

app_name = 'CRMConfig'

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user),
    path('add_record/', views.add_record),
    path('delete_record/<int:id>/', views.delete_record),
    path('record/<int:id>', views.individual_record),
    path('record/update_record/<int:id>', views.update_record)
]