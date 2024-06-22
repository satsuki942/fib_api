from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class FibNView(APIView):    
    def get(self,request):
        REQEUST_PARAM_N = 'n'
        # リクエストパラメータの鍵が存在するかの検査
        if REQEUST_PARAM_N in self.request.GET:
            transformed_param = self.transform_to_int(self.request.GET.get(REQEUST_PARAM_N))
            # リクエストパラメータがintであるかを検査
            if type(transformed_param) == ValueError:
                result = ErrorFib(400,'Bad Request: Given request parameter value is NaN, int value is required')
                http_status = status.HTTP_400_BAD_REQUEST
            else:
                result = fib(transformed_param)
                http_status = status.HTTP_200_OK
        else:
            result = ErrorFib(400,'Bad Request: Request parameter name is not appropriate')
            http_status = status.HTTP_400_BAD_REQUEST

        return Response(self.generate_json_fib(result), http_status)

    # helper function          
    def transform_to_int(self, s):
        try:
            n = int(s)
            return n
        except ValueError as e:
            return e
    
    def generate_json_fib(self, value):
        match value:
            case ErrorFib():
                return value.generate_json()
            case int():
                return {'result':value}
            case _:
                pass

# フィボナッチ数を計算する関数
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        pp = 1
        p = 1
        for i in range(n-2):
            c = pp + p
            pp = p
            p = c
        return c

class ErrorFib():
    def __init__(self, status, message):
        self.status = status
        self.message = message

    def generate_json(self):
        result_json = {
            "status":self.status,
            "message":self.message
        }
        return result_json
