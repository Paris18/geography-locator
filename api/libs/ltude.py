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












