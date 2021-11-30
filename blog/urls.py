from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path('', views.post_index, name="index"),
    # post
    path('detail/<slug:slug>', views.post_detail, name='detail'),
    path('create/', views.post_create, name="create"),
    path('update/<int:id>/<slug:slug>', views.post_update, name="update"),
    path('delete/<int:id>/<slug:slug>', views.post_delete, name="delete"),
    # category
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:id>/<slug:slug>', views.category, name='category'),
    path('create/category', views.add_category, name="add_category"),
    path('update/category/<int:id>/<slug:slug>',
         views.update_category, name="update_category"),
    path('delete/category/<int:id>/<slug:slug>',
         views.delete_category, name="delete_category"),
    # tag
    path('tags/', views.tag_list, name='tag_list'),
    path('tag/<int:id>/<slug:slug>', views.tag, name='tag'),
    path('create/tag', views.add_tag, name="add_tag"),
    path('update/tag/<int:id>/<slug:slug>',
         views.update_tag, name="update_tag"),
    path('delete/tag/<int:id>/<slug:slug>',
         views.delete_tag, name="delete_tag"),
]
