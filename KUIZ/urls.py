from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('exam/<int:pk>', views.exam, name='exam'),
    path('detail/<int:pk>', views.detail_by_section, name='detail'),
    path('exam/<int:pk>/question/<int:question_id>', views.question, name='question'),
    # path('exam/<int:pk>/question/<int:question_id>/answer', views.answer, name='question'),
    # path('exam/<int:pk>/question/score', views.score, name='score'),
]
