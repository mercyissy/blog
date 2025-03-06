from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('add-blog/', add_blog, name='add-blog'),
    path('', home, name='home'),
    path('view-blog/<int:blog_id>/', viewblog, name='view-blog'),
    path('delete-blog/<int:blog_id>/', delete_blog, name='delete-blog'),
    path('edit-blog/<int:blog_id>/', edit_blog, name='edit-blog'),
    path('view-all-blogs/', viewAllBlogs, name='view-all-blogs'),
    # path('blog/view-all/', viewAllBlogs, name='view-all-blogs'),
    path('approve-reject-blog/<int:blog_id>/<str:action>/', approve_reject_blog, name='approve-reject-blog')
]
   


