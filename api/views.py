from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    @action(detail=True, methods=["get"])
    def employies(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emplys=Employee.objects.filter(company=company)
            emply_serializer=EmployeeSerializer(emplys, many=True, context={'request':request})

            return Response(emply_serializer.data)
        except Exception as e:
            return Response({
                'message':"Companies not found! Error"
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


# class EmployeeViewSet(APIView):
#     def get(self,request):
#         queryset=Employee.objects.all()
#         serializer=CompanySerializer(queryset, many=True)
#         return Response(
#             {
#                 "request":request,
#                 "serializer":serializer.data})