from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('schedule/course_details/<int:id>', CourseView.as_view(), name='course_url'),
    path('schedule/teacher_details/<int:id>', TeacherView.as_view(), name='teacher_url'),
    path('schedule/add_course/', StudentRegisterFormView.as_view(), name='add_course'),
    path('schedule/main/', CourseListView.as_view(), name='course_list'),
    path('signup/', SignupView.as_view(), name='sign_up'),
    path('login/', MyLoginView.as_view(), name='login'),

]