from multiprocessing import AuthenticationError
from django.shortcuts import render
from b2b.models import Agent
from b2b.serializers import AgentLoginSerializer, AgentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
# to get holiday details for home screen
class AgentSignUpView(APIView ):
    # permission_classes = [IsAuthenticated]
    def post(self, request,format=None):
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            agent = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgentLoginView(APIView ):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        agent = Agent.objects.filter(email_id = email).first()
        if agent is None:
            raise AuthenticationFailed('Agent not found')
        if not agent.password == password:
              raise AuthenticationFailed('Incorrect Password')
        else:
            data = {"loggedIn": True}
            serialist = AgentSerializer(agent,data=data,partial=True)
            if serialist.is_valid():
                serialist.save()
            return Response(serialist.data, status=status.HTTP_200_OK )
