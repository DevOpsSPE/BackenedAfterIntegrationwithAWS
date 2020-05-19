from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import File,Interview, Login, CommentsPYQ, CommentsExp
from .serializers import FileSerializer, interviewSerializer, loginSerializer, CommentsPYQSerializer, CommentsExpSerializer


class loginData(APIView):
    def get(self, request):
        login = Login.objects.all()
        serializer = loginSerializer(login, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        login_serializer = loginSerializer(data=request.data)
        if login_serializer.is_valid():
            login_serializer.save()
            return Response(login_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginDataId(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, rollNumber):
        try:
            return Login.objects.get(rollNumber=rollNumber)
        except Login.DoesNotExist:
            raise Http404

    def get(self, request, rollNumber, format=None):
        Login = self.get_object(rollNumber)
        serializer = loginSerializer(Login)
        return Response(serializer.data)

    def patch(self, request, rollNumber):
        Login = self.get_object(rollNumber)
        serializer = loginSerializer(Login, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class interviewData(APIView):
    def get(self, request):
        product1 = Interview.objects.all()
        serializer = interviewSerializer(product1, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        file_serializer = interviewSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class interviewDataId(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Interview.objects.get(id=id)
        except product.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = interviewSerializer(product)
        return Response(serializer.data)
    def patch(self, request, id):
        File = self.get_object(id)
        serializer = interviewSerializer(File, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class getData(APIView):


    def get(self, request, *args, **kwargs):
        allFiles = File.objects.all()
        for key in request.data.keys():
            value = request.data.get(key)

from .models import File
from .serializers import serializers

from .serializers import FileSerializer

class getData(APIView):

    def get(self, request, *args, **kwargs):
        allFiles = File.objects.all()

        for key in request.GET.keys():
            value = request.GET.get(key)
            if (key == 'resourceType'):
                allFiles = allFiles.filter(resourceType=value)
            elif (key == 'semester'):
                allFiles = allFiles.filter(semester=value)
            elif (key == 'subject'):
                allFiles = allFiles.filter(subject=value)
            elif (key == 'year'):
                allFiles = allFiles.filter(year=value)
            elif (key == 'id'):
                allFiles = allFiles.filter(id=value)
        
        serializer = FileSerializer(allFiles, many=True)
        return Response(serializer.data)

class patchData(APIView):
    def get_object(self, id):
        try:
            return File.objects.get(id=id)
        except File.DoesNotExist:
            raise Http404

    def patch(self, request, id):
        File = self.get_object(id)
        serializer = FileSerializer(File, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    def get(self, request, id, format=None):
        File = self.get_object(id)
        serializer = FileSerializer(File)
        return Response(serializer.data)

class postData(APIView):
    def post(self, request, *args, **kwargs):        
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):        
        file_serializer = FileSerializer(data=request.data)
        
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deleteData(APIView):
    def get_object(self, id):
        try:
            return File.objects.get(id=id)
        except File.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        File = self.get_object(id)
        File.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class getPostCommentsPYQ(APIView):
    def get(self, request, id):
        allComments = CommentsPYQ.objects.all().filter(pyq=id)

        commentsPYQSerializer = CommentsPYQSerializer(allComments, many=True)
        return Response(commentsPYQSerializer.data)

    def post(self, request, id):
        request.data["pyq"]=id
        commentsPYQSerializer = CommentsPYQSerializer(data=request.data)
        
        if commentsPYQSerializer.is_valid():
            commentsPYQSerializer.save()
            return Response(commentsPYQSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(commentsPYQSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getPostCommentsExp(APIView):
    def get(self, request, id):
        allComments = CommentsExp.objects.all().filter(exp=id)

        commentsExpSerializer = CommentsExpSerializer(allComments, many=True)
        return Response(commentsExpSerializer.data)

    def post(self, request, id):
        request.data["pyq"]=id
        commentsExpSerializer = CommentsExpSerializer(data=request.data)
        
        if commentsExpSerializer.is_valid():
            commentsExpSerializer.save()
            return Response(commentsExpSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(commentsExpSerializer.errors, status=status.HTTP_400_BAD_REQUEST)            