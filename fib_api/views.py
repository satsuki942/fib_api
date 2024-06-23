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
            try:
                transformed_param  = int(self.request.GET.get(REQEUST_PARAM_N))
                if transformed_param <= 0:
                    result = FibResult(400,'Bad Request: Parameter value is less than 1')
                else:
                    result = FibResult(200,fib(transformed_param))
            except ValueError:
                result = FibResult(400,'Bad Request: Given request parameter value is NaN, int value is required')
        else:
            result = FibResult(400,'Bad Request: Request parameter name is not appropriate')

        return Response(result.generate_json(), result.get_http_status())

# フィボナッチ数を計算する関数
def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        pp = 1
        p = 1
        for i in range(n-2):
            c = pp + p
            pp = p
            p = c
        return c
    else:
        raise ValueError('A value less than 1 was passed to fib()')

# リクエストに対する結果を表すクラス
class FibResult():
    def __init__(self, status, content):
        self.status = status
        self.content = content

    # selfの内容をjsonの形式で返す
    def generate_json(self):
        if self.status == 200:
            result_json = {
                "result":self.content
            }
        else:
            result_json = {
                "status":self.status,
                "message":self.content
            }
        return result_json
    
    # self.statusによって適切なHTTPステータスコードを返す
    def get_http_status(self):
        # 妥協した実装になっている
        dict = {200:status.HTTP_200_OK,400:status.HTTP_400_BAD_REQUEST}
        try:
            http_status = dict[self.status]
        except KeyError:
            raise KeyError('Undefined status code was declared')
        return http_status

