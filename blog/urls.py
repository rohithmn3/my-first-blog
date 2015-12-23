from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'), #(?P<pk>[0-9]+) this matches any numbers not letters,
                                                                         #and Django will take everything that you place here and transfer it to a view as a
                                                                         #variable called 'pk'
]
#That means if you enter http://127.0.0.1:8000/post/5/ into your browser,
#Django will understand that you are looking for a view called post_detail
#and transfer the information that pk equals 5 to that view. [ pk is shortcut for primary key ]
