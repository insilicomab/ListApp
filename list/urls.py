from django.urls import path
from .views import ListTop, ListIndex, ListNew, ListEdit, deletefunc

# URLパターンを逆引きできるように名前をつける
app_name = 'list'

urlpatterns = [

    # リクエストされたパス部分が''に合致した場合、views.pyのListTopクラスをインスタンス化する
    path('', ListTop.as_view(), name='top'),

    # リクエストされたパス部分が'index'に合致した場合、views.pyのListIndexクラスをインスタンス化する
    path('index/', ListIndex.as_view(), name='index'),

    # リクエストされたパス部分が'new'に合致した場合、views.pyのListNewクラスをインスタンス化する
    path('new/', ListNew.as_view(), name='new'),

    # リクエストされたパス部分が'edit/pk'に合致した場合、views.pyのListEditクラスをインスタンス化する
    path('edit/<int:pk>', ListEdit.as_view(), name='edit'),

    # リクエストされたパス部分が'delete/pk'に合致した場合、views.pyのdeletefuncを呼び出す
    path('delete/<int:pk>', deletefunc, name='delete'),
]