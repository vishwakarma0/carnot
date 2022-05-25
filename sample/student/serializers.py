from collections import OrderedDict
from django.contrib.auth import get_user_model
from django.db.models import Q, Count, F, Max, Min
from rest_framework import serializers, pagination
from rest_framework.response import Response
from .models import *


class BookSerializer(serializers.ModelSerializer):
    """ Serializer for Student """
    class Meta:
        model = Book
        fields = ('id','title','author_name', 'number_of_pages')

class SchoolSerializer(serializers.ModelSerializer):
    """ Serializer for Student """
    class Meta:
        model = School
        fields = ('id','region_id','school', 'email','principal','phone', 'address')
     
     
class StudentSerializer(serializers.ModelSerializer):
    """ Serializer for Student """
    class Meta:
        model = Student
        fields = ('id','full_name','gender')
        
           
class StudentCreateSerializer(serializers.ModelSerializer):
    """ Serializer for Student """
    school = SchoolSerializer()
    books = BookSerializer()
    
    class Meta:
        model = Student
        fields = ('id','first_name','last_name','email','gender','school','books')
        
    def create(self, validated_data):
        school_data = validated_data.pop('school', None)
        books_data = validated_data.pop('books', None)
        school = School.objects.create(**school_data)
        books = Book.objects.create(**books_data)
        student = Student.objects.create(**validated_data, school=school,books=books )
        return student


class StudentInfoSerializer(serializers.ModelSerializer):
    """ Serializer for Student Info """
    school_name = serializers.SerializerMethodField(read_only=True)
    school_phone = serializers.SerializerMethodField(read_only=True)
    books_read = serializers.SerializerMethodField(read_only=True)
    pages_read = serializers.SerializerMethodField(read_only=True)

    def get_school_name(self, obj):
        if obj.school:
            print("obj.school",obj.school)
            return obj.school.school
        return None
    
    def get_school_phone(self, obj):
        if obj.school:
            return obj.school.phone
        return None
    
    def get_books_read(self, obj):
        if obj.books:
            return obj.books.title
        return None
    
    def get_pages_read(self, obj):
        if obj.books:
            return obj.books.number_of_pages
        return None
    
    class Meta:
        model = Student
        fields = ('id','full_name','email', 'gender','school_name','school_phone',
            'books_read','pages_read')
        
        
class  CustomPagination(pagination.PageNumberPagination):
    """ Pagination for Student """
    page_size = 10
    page_size_query_param = 'page_limit'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
        ]))

