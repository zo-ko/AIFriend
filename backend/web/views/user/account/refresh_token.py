# refresh_token.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken as JWTRefreshToken
from rest_framework_simplejwt.exceptions import TokenError
import logging

logger = logging.getLogger(__name__)


class RefreshTokenView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # 获取refresh token
            refresh_token = request.COOKIES.get('refresh_token')

            if not refresh_token:
                return Response({
                    'result': 'refresh token不存在'
                }, status=status.HTTP_401_UNAUTHORIZED)

            # 验证refresh token并生成新的access token
            refresh = JWTRefreshToken(refresh_token)

            return Response({
                'result': 'success',
                'access': str(refresh.access_token)
            })

        except TokenError as e:
            return Response({
                'result': 'refresh token无效或已过期',
                'detail': str(e)
            }, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            logger.error(f"刷新token错误: {str(e)}")
            return Response({
                'result': '刷新token时发生错误'
            }, status=status.HTTP_400_BAD_REQUEST)