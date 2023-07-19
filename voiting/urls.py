"""
URL configuration for voiting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from webapp.views import VotingListView, VotingDetailView, VotingCharactersView, UpCharacterVoice, ListWinners

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/votinglist/', VotingListView.as_view()),
    path('api/v1/votinglist/<int:pk>/', VotingDetailView.as_view()),
    path('api/v1/votinglist/<int:pk>/characters/', VotingCharactersView.as_view()),
    path('api/v1/votinglist/<int:id_voting>/characters/<int:id_character>/', UpCharacterVoice.as_view()),
    path('api/v1/votinglist/winners/', ListWinners.as_view()),
]
