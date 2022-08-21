from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.
def StudentDetail(request, pk):
    row1 = Student.objects.get(id=pk)
    serializer = StudentSerializer(row1)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)
def StudentDetails(request):
    rows = Student.objects.all()
    serializer = StudentSerializer(rows,many = True)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe = False)