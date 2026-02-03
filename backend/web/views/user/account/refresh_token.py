from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken as JWTRefreshToken
class RefreshToken(APIView):
    def post(self, request, *args, **kwargs):
        try :
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({
                    'result' : 'fresh token不存在'
                },status=401)
            refresh = RefreshToken(refresh_token)
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                refresh.set_jti()
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token)
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7,
                )
                return response
            return Response({
                'result': 'success',
                'access': str(refresh.access_token)
            })
        except :
            return Response({
                'result': 'refresh token 异常',
            },status=401)



# class RefreshTokenView(APIView):
#     def post(self, request, *args, **kwargs):
#         print("=== 调试信息 ===")
#         print(f"请求COOKIES: {request.COOKIES}")
#         print(f"refresh_token值: {request.COOKIES.get('refresh_token')}")
#
#         try:
#             refresh_token = request.COOKIES.get('refresh_token')
#             print(f"refresh_token长度: {len(refresh_token) if refresh_token else 0}")
#
#             if not refresh_token:
#                 print("没有找到refresh_token")
#                 return Response({
#                     'result': 'refresh token不存在'
#                 }, status=status.HTTP_401_UNAUTHORIZED)
#
#             # 测试token是否有效
#             print("尝试验证token...")
#             refresh = JWTRefreshToken(refresh_token)
#             print(f"Token验证成功，payload: {refresh.payload}")
#
#             return Response({
#                 'result': 'success',
#                 'access': str(refresh.access_token)
#             })
#
#         except Exception as e:
#             print(f"发生异常: {type(e).__name__}: {str(e)}")
#             import traceback
#             traceback.print_exc()
#
#             return Response({
#                 'result': '刷新token时发生错误',
#                 'error_type': type(e).__name__,
#                 'error_msg': str(e)
#             }, status=status.HTTP_400_BAD_REQUEST)