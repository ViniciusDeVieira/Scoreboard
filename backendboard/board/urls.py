from django.urls import path
from .views import *
urlpatterns= [
    path("teams/", Teamlist.as_view(), name="team-list"),
    path("locaties/", Locatielist.as_view(), name="locatie-List"),
    path("teams/admin/", Teamslistadmin.as_view(), name="teams-list-admin"),
    path("locaties/admin/", Locatielistadmin.as_view(), name="locatie-list-admin"),
    path("teams/admin/<int:pk>/", TeamDetailadmin.as_view(), name="team-detail-admin"),
    path("locaties/admin/<int:pk>/", LocatieDetailadmin.as_view(), name="locatie-detail-admin"),

    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]