from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from.models import Project, Pledge #Update
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
from rest_framework.views import exception_handler


# custom exception handling to fix bug {"detail": "Method 'DELETE' not allowed."}
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get standard error response
    response = exception_handler(exc, context)

    # now add the HTTP status code to the response
    if response is not None: 
        response.data['status_code'] = response.status_code 

    return response

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            # Getting data from the database
            # NameOfYourModel.objects.get
            # NameOfYourModel.objects.filter
            project = Project.objects.get(pk=pk)

            # Running code in permission_classes
            self.check_object_permissions(self.request,project)
            return project
        # No matching id in the database
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project, 
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk):
        project = self.get_object(pk)

        # Django Model method
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PledgeList(APIView):
    permission_classes = [permissions.AllowAny]

    def get (self, request):
        pledges = Pledge.objects.all()
        print(list(pledges))
        # Serializer here is turning a list of models into JSON for the response payload
        serializer = PledgeSerializer(pledges, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        # Serializer here is turning the request JSON into a model
        # "supporter" is NOT allowed to be in the HTTP Request data
        # print(request.data)
        serializer = PledgeSerializer(data=request.data)
        # Check that a valid model can be created
        if serializer.is_valid():
            # Where the model actually gets saved into the database
            # request.user <= Authentication Token, find matching user
            serializer.save(supporter=request.user if request.user.is_authenticated else None)
            return Response(
                # serializer.data is JSON
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            # serializer.errors is JSON
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
# create PledgeDetailView

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]

    def get_object(self, pk):
        try:
            pledges = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request,pledges)
            return pledges
        except Pledge.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        pledges = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledges)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pledges = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance=pledges, 
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk):
        pledges = self.get_object(pk)

        # Django Model method
        pledges.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create updates views
# class UpdateList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, project_pk):
#         updates = Update.objects.filter(project_id=project_pk)
#         serializer = UpdateSerializer(updates, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, project_pk):
#         project = Project.objects.get(pk=project_pk)
#         serializer = UpdateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(project=project)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

class ProjectPledgeList(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, project_pk):
        project = get_object_or_404(Project, pk=project_pk)
        pledges = Pledge.objects.filter(project=project)
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

