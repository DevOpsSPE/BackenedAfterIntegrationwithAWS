"""SCP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt


from django.urls import path, include, re_path
from django.conf import settings
from SCPapp import views as s
from MockSchedularApp import views as m
from SCPapp import views
from django.conf.urls.static import static
from VideoModule import views as VideoModuleViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getData/', views.getData.as_view()),
    path('getData/<int:id>/', views.patchData.as_view()),
    path('postData/', views.postData.as_view()),
    path('patchData/<int:id>/', views.patchData.as_view()),
    path('pyq/comments/<int:id>/', views.getPostCommentsPYQ.as_view()),
    path('deleteData/<id>/', csrf_exempt(views.deleteData.as_view())),
    path('interviewData/<int:id>/', views.interviewDataId.as_view()),
    path('interviewData/', views.interviewData.as_view()),
    path('exp/comments/<int:id>/', views.getPostCommentsExp.as_view()),
    path('loginData/<str:rollNumber>/', views.loginDataId.as_view()),
    path('loginData/', views.loginData.as_view()),
    
    path('getVideoData/', VideoModuleViews.getData.as_view()),
    path('getVideoData/<int:id>/', VideoModuleViews.getDataById.as_view()),
    path('postVideoData/', VideoModuleViews.postData.as_view()),
    path('deleteVideoData/<int:id>/', csrf_exempt(VideoModuleViews.deleteData.as_view())),
    path('updateVideoData/<int:id>/', VideoModuleViews.updateData.as_view()),
    path('commentsOnVideo/<int:id>/', VideoModuleViews.getPostComments.as_view()),

    re_path(r'^api/students/$', m.students_list),
    re_path(r'^api/students/([0-9]+)$', m.students_detail),
    re_path(r'^api/students/sendmail/([0-9]+)$', m.sendmail),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
