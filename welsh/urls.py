# URL path configuration
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

testresultpatterns = [
	path('year7/topic1/test/result/', views.checkresults, name= 'y7_t1_testresult'),
	path('year7/topic2/test/result/', views.checkresults, name= 'y7_t2_testresult'),
	path('year7/topic3/test/result/', views.checkresults, name= 'y7_t3_testresult'),
	path('year7/topic4/test/result/', views.checkresults, name= 'y7_t4_testresult'),
	path('year7/topic5/test/result/', views.checkresults, name= 'y7_t5_testresult'),
	path('year7/topic6/test/result/', views.checkresults, name= 'y7_t6_testresult'),
	path('year8/topic1/test/result/', views.checkresults, name= 'y8_t1_testresult'),
	path('year8/topic2/test/result/', views.checkresults, name= 'y8_t2_testresult'),
	path('year8/topic3/test/result/', views.checkresults, name= 'y8_t3_testresult'),
	path('year8/topic4/test/result/', views.checkresults, name= 'y8_t4_testresult'),
	path('year8/topic5/test/result/', views.checkresults, name= 'y8_t5_testresult'),
	path('year9/topic1/test/result/', views.checkresults, name= 'y9_t1_testresult'),
	path('year9/topic2/test/result/', views.checkresults, name= 'y9_t2_testresult'),
	path('year9/topic3/test/result/', views.checkresults, name= 'y9_t3_testresult'),
	path('year9/topic4/test/result/', views.checkresults, name= 'y9_t4_testresult'),
	path('year9/topic5/test/result/', views.checkresults, name= 'y9_t5_testresult'),
	path('year10/topic1/test/result/', views.checkresults, name= 'y10_t1_testresult'),
	path('year10/topic2/test/result/', views.checkresults, name= 'y10_t2_testresult'),
	path('year10/topic3/test/result/', views.checkresults, name= 'y10_t3_testresult'),
	path('year10/topic4/test/result/', views.checkresults, name= 'y10_t4_testresult'),
	path('year10/topic5/test/result/', views.checkresults, name= 'y10_t5_testresult'),
	path('year11/topic1/test/result/', views.checkresults, name= 'y11_t1_testresult'),
	path('year11/topic2/test/result/', views.checkresults, name= 'y11_t2_testresult'),
	path('year11/topic3/test/result/', views.checkresults, name= 'y11_t3_testresult'),
	path('year11/topic4/test/result/', views.checkresults, name= 'y11_t4_testresult'),
	path('year11/topic5/test/result/', views.checkresults, name= 'y11_t5_testresult'),
]

testpatterns = [
	path('year7/topic1/test/', views.testview, name= 'y7_t1_test'),
	path('year7/topic2/test/', views.testview, name= 'y7_t2_test'),
	path('year7/topic3/test/', views.testview, name= 'y7_t3_test'),
	path('year7/topic4/test/', views.testview, name= 'y7_t4_test'),
	path('year7/topic5/test/', views.testview, name= 'y7_t5_test'),
	path('year7/topic6/test/', views.testview, name= 'y7_t6_test'),
	path('year8/topic1/test/', views.testview, name= 'y8_t1_test'),
	path('year8/topic2/test/', views.testview, name= 'y8_t2_test'),
	path('year8/topic3/test/', views.testview, name= 'y8_t3_test'),
	path('year8/topic4/test/', views.testview, name= 'y8_t4_test'),
	path('year8/topic5/test/', views.testview, name= 'y8_t5_test'),
	path('year9/topic1/test/', views.testview, name= 'y9_t1_test'),
	path('year9/topic2/test/', views.testview, name= 'y9_t2_test'),
	path('year9/topic3/test/', views.testview, name= 'y9_t3_test'),
	path('year9/topic4/test/', views.testview, name= 'y9_t4_test'),
	path('year9/topic5/test/', views.testview, name= 'y9_t5_test'),
	path('year10/topic1/test/', views.testview, name= 'y10_t1_test'),
	path('year10/topic2/test/', views.testview, name= 'y10_t2_test'),
	path('year10/topic3/test/', views.testview, name= 'y10_t3_test'),
	path('year10/topic4/test/', views.testview, name= 'y10_t4_test'),
	path('year10/topic5/test/', views.testview, name= 'y10_t5_test'),
	path('year11/topic1/test/', views.testview, name= 'y11_t1_test'),
	path('year11/topic2/test/', views.testview, name= 'y11_t2_test'),
	path('year11/topic3/test/', views.testview, name= 'y11_t3_test'),
	path('year11/topic4/test/', views.testview, name= 'y11_t4_test'),
	path('year11/topic5/test/', views.testview, name= 'y11_t5_test'),
]


topicpatterns = [
	path('topic1/', views.selectview, name='topic_1'),
	path('topic2/', views.selectview, name='topic_2'),
	path('topic3/', views.selectview, name='topic_3'),
	path('topic4/', views.selectview, name='topic_4'),
	path('topic5/', views.selectview, name='topic_5'),
]

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='welsh/index.html'), name='index'),
    path('home/', views.home, name='home'),
    path('year7/', views.year7, name='year_7'),
	path('year8/', views.year8, name='year_8'),
	path('year9/', views.year9, name='year_9'),
	path('year10/', views.year10, name='year_10'),
	path('year11/', views.year11, name='year_11'),
    path('year7/', include(topicpatterns)),
    path('year8/', include(topicpatterns)),
    path('year9/', include(topicpatterns)),
    path('year10/', include(topicpatterns)),
    path('year11/', include(topicpatterns)),
    path('year7/topic6/', views.selectview, name='y7_topic_6'),
    path('', include(testpatterns)),
    path('', include(testresultpatterns))
]