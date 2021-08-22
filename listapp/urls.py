from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # リクエストされたパス部分がadmin/に合致した場合、admin.site.urlsを呼び出す
    path('admin/', admin.site.urls), 

    # listアプリのurls.pyを呼び出す
    path('', include('list.urls')),
]
