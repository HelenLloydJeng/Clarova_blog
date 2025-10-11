from django.urls import path
from .views import SignUpView, profile, like_post, dislike_post 

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('post/<int:pk>/dislike/', dislike_post, name='dislike_post'),
]