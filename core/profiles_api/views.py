from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):  # ignore # noqa #A002
        """Returns a list of APIView feature"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)', 'Is similar to a traditional Django View',
            'Gives you the most control over your application logic', 'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
