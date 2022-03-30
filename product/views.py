from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSer
from .models import Student
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class home_view(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        query=Student.objects.all()
        student1=query.first()
        serializer=StudentSer(query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer=StudentSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)