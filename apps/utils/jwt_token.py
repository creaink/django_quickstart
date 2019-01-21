# -*- coding: utf-8 -*-
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings
from jwt import ExpiredSignature, DecodeError

def generate_jwt_token(user):
	"""generate a valid jwt token for user
	Args:
		user: user model instance
	Return:
		a JWT like token string
	"""
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

	payload = jwt_payload_handler(user)
	token = jwt_encode_handler(payload)
	return token

def jwt_credentials(client, user):
	"""use for test case jwt credentials
	Args:
		client: APIClient instance
		user: user model instance
	Usage:
		user_client = APIClient(enforce_csrf_checks=True)
		user = User.objects.create_user(...)
		jwt_credentials(user_client, user)
		user_client.force_authenticate(user=user)
	"""
	if not isinstance(client, APIClient):
		raise Exception("client should be instance of APIClient")
	client.credentials(Authorization='{0} {1}'.format(api_settings.JWT_AUTH_HEADER_PREFIX,
														generate_jwt_token(user)))

def validate_jwt_token(token):
	"""validate jwt token
	Args:
		token: a JWT like token string
	Return:
		True or False
	"""
	jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
	try:
		jwt_decode_handler(token)
	except ExpiredSignature:
		# 'Signature has expired.'
		return False
	except DecodeError:
		# 'Error decoding signature.'
		return False
	return True
