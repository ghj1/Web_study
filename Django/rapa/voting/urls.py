from django.urls import path
from django.urls.resolvers import URLPattern
from voting import views

app_name = 'voting'
urlpatterns =[
    # /voting/
    path('',views.index, name = 'index'),
    # /voting/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /voting/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /voting/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
] 

