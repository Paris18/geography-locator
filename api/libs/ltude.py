#python imports.
import requests
import json
import logging

# django imports.
from django.conf import settings

# app level imports.
from .exceptions import (
	NetworkException,
	BadRequestException,
	)
from .constants import(
	INVALID_KEY,
	)


logger = logging.getLogger(__name__)


# def getlatlon(address, key, url=URL):
# 	"""
# 	This function is used to get the latitude and longitude address.
# 	"""
# 	PARAMS = {}
# 	PARAMS['key'] = key
# 	PARAMS['q'] = address

# 	try: 
# 		response = requests.get(url=url, params=PARAMS)
# 		if response.status_code == 200:
# 			data = response.json()
# 			lat = data[0]['lat'] 
# 			lon = data[0]['lon']
# 			return lat, lon

# 	except Exception as e:
# 		print(str(e))
# 		raise NetworkException(errors=str(e))
		
# 	return 0, 0


class Ltude:
	def __init__(self):
		self.request_session = requests.Session()
		self.url = settings.LOCATIONIQ_URL


	def service_dispacher(self, url, params, httpMethod):
		if httpMethod == "GET":
			response = self.request_session.get(url=url, params=params)
		elif httpMethod == "POST":
			response = self.request_session.post(url=url, data=json.dumps(params))
		if response.status_code == 401:
			raise NetworkException
		return response

	def get_ltudes(self,address,key):
		try:
			params = {'key':key,'q':address}
			response = self.service_dispacher(self.url,params,"GET")
			if response.status_code == 404:
				return 0,0
			data = response.json()[0]
			return data['lat'],data['lon']
		except:
			logger.error("request failed", exc_info=True)


# Ltude_obj = Ltude()
# print(Ltude_obj.get_ltudes("bastwad Belagavi",'984aabebe49559'))










