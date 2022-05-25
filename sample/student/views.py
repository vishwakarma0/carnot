from django.shortcuts import render
from rest_framework.decorators import action, api_view, permission_classes,renderer_classes
from rest_framework import generics, mixins, filters, status, viewsets
from rest_framework.response import Response
from rest_framework.renderers import AdminRenderer, BrowsableAPIRenderer, JSONRenderer
from .serializers import *
from .models import *


@api_view(['GET'])
def samp(request):
    """ sample to test working of rest api"""
    return Response({"sucess":"success"})


class StudentViewset(viewsets.GenericViewSet, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = Student.objects.select_related('school','books').all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    search_fields = ['id','first_name','last_name']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentInfoSerializer
        elif self.action == 'create_':
            return StudentCreateSerializer
        return StudentSerializer
    
    @action(detail=False, methods=['post'])
    def create_(self, request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

class StudentInfoViewset(viewsets.GenericViewSet, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    
    queryset = Student.objects.select_related('school','books').all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    renderer_classes = [AdminRenderer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','first_name','last_name']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentInfoSerializer
        elif self.action == 'create_':
            return StudentCreateSerializer
        return StudentSerializer
    
    @action(detail=False, methods=['post'])
    def create_(self, request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 