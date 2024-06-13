import logging

from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apioptigest.models import Students, Sector, CheckMailCode
from apioptigest.serializers import StudentsSerializer, SectorSerializer


# Students
class StudentsAPIView(APIView):
    def get(self, request):
        etudiants = Students.objects.all()
        serializer = StudentsSerializer(etudiants, many=True)
        return Response(serializer.data)

    def post(self, request):
        logging.info('Requête reçue: %s', request.body.decode('utf-8'))

        serializer = StudentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginPIView(APIView):

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        try:
            student = Students.objects.get(email=email)
            if check_password(password, student.pass_field):

                token = student.auth_token.key

                return Response({'token': token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        except Students.DoesNotExist:
            return Response({'error': 'L\'utilisateur n\'existe pas'}, status=status.HTTP_401_UNAUTHORIZED)


# Sector
class SectorAPIView(APIView):
    def get(self, request):
        sectors = Sector.objects.all()
        serializer = SectorSerializer(sectors, many=True)
        return Response(serializer.data)

    def post(self, request):
        sector = SectorSerializer(data=request.data)

        if sector.is_valid():
            sector.save()
            return Response(sector.data, status=status.HTTP_201_CREATED)
        return Response(sector.errors, status=status.HTTP_400_BAD_REQUEST)
