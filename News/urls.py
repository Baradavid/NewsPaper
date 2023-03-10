from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete, subscribe, CategoryListView

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view()),
    path('create', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]
