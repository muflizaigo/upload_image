from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UploadedImageSerializer

class UploadImageView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_image = serializer.save()
            image_url = request.build_absolute_uri(uploaded_image.image.url)
            return Response({'image_url': image_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
