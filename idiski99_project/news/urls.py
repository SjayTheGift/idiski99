from django.urls import path
from .views import CategoryPageView, PostListPageView, PostDetailPageView

urlpatterns = [
    path('category/<slug:slug>/', CategoryPageView.as_view(), name='category_post'),
    path('<slug:slug>/', PostDetailPageView.as_view(), name='post_detail'),
    path('', PostListPageView.as_view(), name='post_list'),

]