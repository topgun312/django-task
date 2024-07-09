from django.urls import include, path
from dogs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"breeds", views.BreedList, basename="breed_list")
router.register(r"breeds", views.BreedDetail, basename="breed_detail")
router.register(r"dog_model", views.DogModelView)
router.register(r"breed_model", views.BreedModelView)


urlpatterns = [
    path("dogs/", views.DogList.as_view(), name="dog_list"),
    path("dogs/<int:pk>/", views.DogDetail.as_view(), name="dog_detail"),
    path("dogs_new/", views.DogListNew.as_view(), name="dog_new_list"),
    path("dogs_new/<int:pk>/", views.DogDetailNew.as_view(), name="dog_new_detail"),
    path("", include(router.urls)),
]
