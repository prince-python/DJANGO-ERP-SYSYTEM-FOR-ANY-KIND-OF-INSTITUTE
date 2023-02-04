
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addcourse', views.addcourse),
    path('showcourse', views.showcourse),
    path('showstudents', views.showstudents),
    path('payamount', views.payamount),
    path('showam', views.showam),
    path('searchenquiry', views.searchenquiry),
    path('studentdelete/<int:id>/',views.studentdelete,name='studentdelete'),
    path('cdelete/<int:id>/',views.cdelete,name='cdelete'),
    path('studentupdate/<int:id>/',views.studentupdate,name='studentupdate'),
    path('studentupdatesave/<int:id>/',views.studentupdatesave,name='studentupdatesave'),
    path('cupdate/<int:id>/',views.cupdate,name='cupdate'),
    path('cupdates/<int:id>/',views.cupdates,name='cupdates'),
    
]