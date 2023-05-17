from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import VitalSigns
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import VitalSignsSerializer
from django.views.generic import View
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



@method_decorator(csrf_exempt, name='dispatch')
class VitalSignsUpload(View):
    def post(self, request, *args, **kwargs):
        # extract data from the request
        data = request.POST
        temperature = data.get('temperature')
        heart_rate = data.get('heart_rate')
        blood_pressure = data.get('blood_pressure')

        # perform basic data validation
        if not all([temperature, heart_rate, blood_pressure]):
            return HttpResponseBadRequest('Missing required parameters')

        # create a new VitalSigns object and save it to the database
        vital_signs = VitalSigns(
            temperature=temperature,
            heart_rate=heart_rate,
            blood_pressure=blood_pressure
        )
        vital_signs.save()

        # return a success response
        return HttpResponse('Vital signs data uploaded successfully')


@api_view(['POST'])
def upload_data(request):
    serializer = VitalSignsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class VitalSignsList(generics.ListCreateAPIView):
    queryset = VitalSigns.objects.all()
    serializer_class = VitalSignsSerializer

class VitalSignsDetail(RetrieveUpdateDestroyAPIView):
    queryset = VitalSigns.objects.all()
    serializer_class = VitalSignsSerializer
    lookup_field = 'id'

class VitalSignsDelete(LoginRequiredMixin, DeleteView):
    model = VitalSigns
    success_url = reverse_lazy('vital-signs-list')