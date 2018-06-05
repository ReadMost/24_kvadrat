from django.urls import path
from . import views
app_name = 'query_buyer'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:home_buyer_id>/', views.detail, name='detail'),
    path('<int:home_buyer_id>/results/', views.results, name='results'),
    path('<int:home_buyer_id>/vote/', views.vote, name='vote'),
    path('form/', views.form, name='form'),
    path('save/', views.save, name='save'),

]