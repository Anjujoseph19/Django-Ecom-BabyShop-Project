from django.urls import path
from . import views
from store.controller import authview

urlpatterns = [
    path('',views.home,name='home'),
    path('collections/',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),


    path('register/',authview.register_user,name='register'),
    path('login/',authview.login_user,name='login'),
    path('logout/',authview.logout_user,name='logout'),

]
