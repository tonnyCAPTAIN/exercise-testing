from django.urls import URLPattern, path
from .views import Quiz, RandomQuestion, QuizQuestion

app_name='quiz'



urlpatterns = [
	path('', Quiz.as_view(), name='quiz'),
	path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
	path('r/<str:topic>/', QuizQuestion.as_view(), name='questions')
]