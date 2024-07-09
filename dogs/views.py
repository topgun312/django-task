from django.http import Http404
from dogs.models import Breed, Dog
from dogs.serializers import BreedSerializer, DogSerializer
from rest_framework import mixins, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class DogList(APIView):
    """
    Класс - представление для отображения списка собак и их создания с APIView
    """

    serializer_class = DogSerializer
    model = Dog

    def get(self, request, format=None):
        dogs = self.model.objects.all()
        serializer = self.serializer_class(dogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        valid_data = serializer.is_valid(raise_exception=True)
        if valid_data:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    """
    Класс - представление для отображения детальной страницы собаки, редактирования и удаления записи с APIView
    """

    serializer_class = DogSerializer
    model = Dog

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = self.serializer_class(dog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = self.serializer_class(dog, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dog = self.get_object(pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    """
    Класс - представление для отображения списка пород и их создания с mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet
    """

    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """
    Класс - представление для отображения детальной страницы породы, редактирования и удаления записи с mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet
    """

    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class DogListNew(ListCreateAPIView):
    """
    Класс - представление для отображения списка собак и их создания с ListCreateAPIView
    """

    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDetailNew(RetrieveUpdateDestroyAPIView):
    """
    Класс - представление для отображения детальной страницы собаки, редактирования и удаления записи с RetrieveUpdateDestroyAPIView
    """

    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogModelView(ModelViewSet):
    """
    Класс - представление выполнения всех операций с моделью собаки с ModelViewSet
    """

    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class BreedModelView(ModelViewSet):
    """
    Класс - представление выполнения всех операций с моделью породы с ModelViewSet
    """

    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
