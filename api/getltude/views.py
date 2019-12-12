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
	model = AdressLtude # model assignation

	# serialser dictionary
	serializers_dict = {
		'getltudes' : AddresLtudeAddSerializer,
		'listltudes': AddresLtudeGetSerializer,
		'getltude': AddresLtudeGetSerializer
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

	def compute_ltude(self,address,key):
		try:
			l,k = ltude_obj.get_ltudes(address,key)# finding longitude and latitude
			response_data = {"address":address,'latitude':l,'longitude':k}
			return response_data
		except:
			raise BadRequestException(BAD_REQUEST)


	@action(methods=['post'], detail=False)
	def getltudes(self,request):
		'''
		This api will receive the key and file as parameter
		it will read the received file skip first row(header)
		gets the longitude and latitude from locationiq api and insert into table
		'''
		try:
			data = request.data
			csvfile = request.FILES['input_file'] # uploaded file receiving
			address_list = read_file.read_uploads(csvfile)[1:]# reading the file
			for i in address_list:
				response_data = self.compute_ltude(i,data["key"])# finding longitude and latitude
				serializer = self.get_serializer(data = response_data)
				if serializer.is_valid():
					serializer.save()
			return Response({"Status":"Filed uploaded successfully and computed output"},status=status.HTTP_201_CREATED)
		except NetworkException:
			raise NetworkException(INVALID_KEY)
		except:
			raise BadRequestException(BAD_REQUEST)


	@action(methods=['post'], detail=False)
	def getltude(self,request):
		'''
		This api will receive the key and file as parameter
		serach the corresponding address in table and returns it if not exists
		then gets the longitude and latitude from locationiq api and insert into table
		'''
		try:
			address = request.GET["address"]
			key = request.GET["key"]
			data = self.get_queryset().get(address = address)
			serializer = self.get_serializer(data)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except self.model.DoesNotExist:
				response_data = self.compute_ltude(address,key)
				serializer = self.get_serializer(data = response_data)
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data, status=status.HTTP_201_CREATED)
				else:
					raise BadRequestException(BAD_REQUEST)
		except:
			raise BadRequestException(BAD_REQUEST)

	@action(methods=['get'], detail=False)
	def listltudes(self,request):
		'''
		This api will response the list of all data
		'''
		try:
			data = self.get_serializer(self.get_queryset(), many=True).data 
			return Response(data, status=status.HTTP_200_OK)
		except:
			raise BadRequestException(BAD_REQUEST)

	@action(methods=['delete'], detail=False)
	def cleardata(self, request):
		'''
		clear the existing table.
		'''
		self.get_queryset().delete()
		return Response(({"status":"deleted all existed data"}),
			status=status.HTTP_200_OK)


	@action(methods=['get'], detail=False)
	def get_template_file(self, request):
		'''
		This api will gives the example template file
		'''
		file = template_file
		FilePointer = open(file,"r")
		response = HttpResponse(FilePointer,content_type='application/csv')
		response['Content-Disposition'] = 'attachment; filename=address_template.csv'
		return response


	@action(methods=['get'], detail=False)
	def get_address(self, request):
		'''
		this api will download the existing data from table
		'''
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="adress_ltude.csv"'
		writer = csv.writer(response, delimiter=',')

		writer.writerow(['Address','latitude','longitude']) 
		for i in self.get_queryset():
			writer.writerow([i.address,i.latitude,i.longitude])
		return response



	


