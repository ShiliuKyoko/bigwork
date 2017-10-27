"""bigproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Tadmin.views import Testadmin,detail,detail_commnetPOST,index_login,index_register,error_page,test,table_page,aboutme
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout
from Tadmin.api import a_article_list,a_article_info

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^first/$',Testadmin,name='index' ),
    url(r'^$',Testadmin ),
    url(r'^detail/(?P<page_num>\d+)$', detail, name='detail'),
    url(r'^detail/(?P<page_num>\d+)/commnet$', detail_commnetPOST, name='commentPOST'),
    url(r'^login/$', index_login, name='login'),
    url(r'^register/$', index_register, name='register'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^login/register$', index_register),
    url(r'^error_page/$',error_page, name='error_page'),
    url(r'^api/article/$', a_article_list),
    url(r'^api/article/(?P<id>\d+)$', a_article_info),
    url(r'^edit/$',test,name='edit_page'),
    url(r'^table/$',table_page,name='table_page'),
    url(r'^about/$',aboutme,name='aboutme'),

]
