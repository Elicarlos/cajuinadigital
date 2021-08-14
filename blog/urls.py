from blog import views


urlpatterns = [
    path('', views.index, name="home")
]