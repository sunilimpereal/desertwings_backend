
from b2b.views import AgentLoginView, AgentSignUpView
from django.urls import path,include
urlpatterns = [
    path ('agent/signup', AgentSignUpView.as_view(),name='agent signup'),
    path ('agent/login', AgentLoginView.as_view(),name='agent login'),

]
