from rest_framework import status
from rest_framework.exceptions import (
    APIException,
    ParseError,
    ValidationError,
)

# logger
import logging
logger = logging.getLogger(__name__)


class ResourceConflictException(APIException):
    pass

class ParseException(ParseError):
    def __init__(self, detail=None, code=None, errors=None):
        if errors:
            logger.info(errors)
        return super(ParseException, self).__init__(detail, code)

class BadRequestException(ValidationError):
    def __init__(self, detail=None, code=None, errors=None):
        if errors:
            logger.info(errors)
        return super(BadRequestException, self).__init__(detail, code)
    pass

class NetworkException(APIException):
    def __init__(self, detail=None, code=None, errors=None):
        if errors:
            logger.info(errors)
        return super(NetworkException, self).__init__(detail, code)
    pass