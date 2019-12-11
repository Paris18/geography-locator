#python imports.
import csv

#django/rest_framework imports.
from django.shortcuts import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet


# Project Level Import
from libs import ltude_obj
from libs.exceptions import(
	ParseException,
	ResourceConflictException,
	NetworkException,
	BadRequestException,
)
from libs.constants import(
	BAD_ACTION,
	BAD_REQUEST,
	INVALID_KEY,
	template_file,
)
from libs.readfiles import read_file


#app level imports.
from .serializers import (
	AddresLtudeGetSerializer,
	AddresLtudeAddSerializer,
)
from .models import (
	AdressLtude,
)




class LtudeViewSet(GenericViewSet):
	"""
	"""
	model = AdressLtude

	serializers_dict = {
		'getltudes' : AddresLtudeAddSerializer,
		'listltudes': AddresLtudeGetSerializer
		}

	def get_queryset(self, filterdata=None):
		self.queryset = self.model.objects.all()
		if filterdata:
			self.queryset = self.queryset.filter(**filterdata)
		return self.queryset

	def get_serializer_class(self):
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise ParseException(BAD_ACTION, errors=key)

	@action(methods=['post'], detail=False)
	def getltudes(self,request):
		try:
			data = request.data
			csvfile = request.FILES['input_file'] # uploaded file receiving
			address_list = read_file.read_uploads(csvfile)[1:]
			for i in address_list:
				l,k = ltude_obj.get_ltudes(i,data["key"])
				response_data = {"address":i,'latitude':l,'longitude':k}
				serializer = self.get_serializer(data = response_data)
				if serializer.is_valid():
					serializer.save()
			return Response({"Status":"Filed uploaded successfully and computed output"})
		except NetworkException:
			raise NetworkException(INVALID_KEY)
		except:
			raise BadRequestException(BAD_REQUEST)

	@action(methods=['get'], detail=False)
	def listltudes(self,request):
		try:
			data = self.get_serializer(self.get_queryset(), many=True).data 
			return Response(data, status=status.HTTP_200_OK)
		except:
			raise BadRequestException(BAD_REQUEST)

	@action(methods=['delete'], detail=False)
	def cleardata(self, request):
		"""
		delete all the records from table.
		"""
		self.get_queryset().delete()
		return Response(({"status":"deleted all existed data"}),
			status=status.HTTP_200_OK)


	@action(methods=['get'], detail=False)
	def get_template_file(self, request):
		"""
		use to download csv file.
		"""
		file = template_file
		FilePointer = open(file,"r")
		response = HttpResponse(FilePointer,content_type='application/csv')
		response['Content-Disposition'] = 'attachment; filename=address_template.csv'
		return response



	


