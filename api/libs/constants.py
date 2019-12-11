# python import
import os

# django imports.
from api.settings import BASE_DIR



BAD_REQUEST = {
    "error_code": "ERR_4000",
    "detail": "Bad Request."
}

BAD_ACTION = {
    "error_code": "ERR_4005",
    "detail": "Bad Action."
}

OPERATION_NOT_ALLOWED = {
    "error_code": "ERR_4012",
    "code": "FT_4012",
    "detail": "Operation not allowed"
}

INVALID_KEY = {
    "error_code": "ERR_4013",
    "code": "FT_4013",
    "detail": "INVALID API KEY"
}

template_file = os.path.join(BASE_DIR, 'test_template.csv')
