from django.contrib import admin
from django.urls import path
from lycee import views
from lycee.views import StudentCreateView, StudentUpdateView, CursusCallView, ParticularCallView

urlpatterns = [

  path('', views.index, name='index'),
  
  path('admin/', admin.site.urls),
            path('lycee',views.index,name="index"),
      path('lycee/<int:cursus_id>',views.detail,name='detail'),
      path('lycee/student/<int:student_id>',views.detail_student,name="detail_student"),
      path('lycee/cursuscall/view',views.callview,name="call view"),
      path('lycee/cursuscall/view/<int:presence_id>',views.detail_callview,name='update student'),
      path('lycee/student/create',StudentCreateView.as_view(),name='create student'),
      path('lycee/student/edit/<pk>',StudentUpdateView.as_view(),name='update student'),
      path('lycee/cursuscall/<cursus>',CursusCallView.as_view(),name='Call of row'),
      path('lycee/cursuscall',ParticularCallView.as_view(),name='Particular call of row'),
    
    
]