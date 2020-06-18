from django.urls import path

from .views import (
    # my_fbv,
    CourseView,
    CourseListView
)
app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    # path('', CourseView.as_view(template_name= 'home.html'), name='courses-list'),
    path('<int:id>', CourseView.as_view(), name='courses-detail')
]