from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import*
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from .models import (
    Appointments, Branch, BranchCompanyCaseAssignmentDetail, Campaign, CaseAssignmentDetail, CasePriorityMaster, CaseRegister, ClientInvoices, ClientQuotations, CommunicationChannels, CommunicationDetails, Communications, Company, PriceList, Products, ProjectTaskProgress, ProjectTasks, Projects, Services, TaskAssignmentDetail, User, UserProfile,UserPrivilege, Member, Department, Task, Document, Meeting, Note,
    Case, CaseFeedback, CallRecord, Chat, LeadRatingLabel, Lead, 
    Project, OpportunityStage, Organisation, Account, OpportunityCurrencyCode,
    OpportunityProduct, Contact, Product, Opportunity
)

from .serializers import (
                Appointments,
                Branch,
                BranchCompanyCaseAssignmentDetail,
                Campaign, CaseAssignmentDetail,
                CasePriorityMaster, 
                CaseRegister,
                ClientInvoices, 
                ClientQuotations, 
                CommunicationChannels, 
                CommunicationDetails, 
                Communications, 
                Company, 
                PriceList, 
                Products, 
                ProjectTaskProgress, 
                ProjectTasks, 
                Projects, 
                Services, 
                TaskAssignmentDetail, 
                User, 
                UserProfile,
                UserPrivilege, 
                Member, 
                Department, 
                Task, 
                Document, 
                Meeting, 
                Note,
                Case, 
                CaseFeedback, 
                CallRecord, 
                Chat, 
                LeadRatingLabel, 
                Lead, 
                Project, 
                OpportunityStage, 
                Organisation, 
                Account, 
                OpportunityCurrencyCode,
                OpportunityProduct, 
                Contact, 
                Product, 
                Opportunity
)

from drf_yasg.utils import swagger_auto_schema


from .serializers import *

from django.contrib.auth.hashers import make_password


class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    @swagger_auto_schema(responses={200: UserSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        user= User.objects.all()
        serializer = UserSerializer( user, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserProfileView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserProfileSerializer

    @swagger_auto_schema(responses={200: UserProfileSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        user_profile= UserProfile.objects.all()
        serializer = UserProfileSerializer( user_profile, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=UserProfileSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = UserProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserProfileSerializer

    @swagger_auto_schema(responses={200: UserProfileSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user_profile)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserProfileSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, pk=pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MemberView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberSerializer

    @swagger_auto_schema(responses={200: MemberSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
       member= Member.objects.all()
       serializer = MemberSerializer(member, many=True)
       return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=MemberSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = MemberSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberSerializer

    @swagger_auto_schema(responses={200: MemberSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        member = get_object_or_404(Member, pk=pk)
        serializer = MemberSerializer(member)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MemberSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
       member = get_object_or_404(Member, pk=pk)
       serializer = MemberSerializer(member, data=request.data)
       if serializer.is_valid():
             serializer.save()
             return Response(data=serializer.data, status=status.HTTP_200_OK)
       else:
             Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
       member = get_object_or_404(Member, pk=pk)
       member.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)



class DepartmentView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartmentSerializer

    @swagger_auto_schema(responses={200: DepartmentSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        department= Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=DepartmentSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = DepartmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartmentSerializer

    @swagger_auto_schema(responses={200: DepartmentSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=DepartmentSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
       department = get_object_or_404(Department, pk=pk)
       department.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserPrivilegeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserPrivilegeSerializer

    @swagger_auto_schema(responses={200: UserPrivilegeSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        user_privileges = UserPrivilege.objects.all()
        serializer = UserPrivilegeSerializer(user_privileges, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserPrivilegeSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = UserPrivilegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserPrivilegeChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserPrivilegeSerializer

    @swagger_auto_schema(responses={200: UserPrivilegeSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        user_privilege = get_object_or_404(UserPrivilege, pk=pk)
        serializer = UserPrivilegeSerializer(user_privilege)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserPrivilegeSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        user_privilege = get_object_or_404(UserPrivilege, pk=pk)
        serializer = UserPrivilegeSerializer(user_privilege, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        user_privilege = get_object_or_404(UserPrivilege, pk=pk)
        user_privilege.delete()
        return Response(data={"message": "User privilege deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class AppointmentsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AppointmentsSerializer

    @swagger_auto_schema(responses={200: AppointmentsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Appointments.objects.all()
        serializer = AppointmentsSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=AppointmentsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AppointmentsSerializer

    @swagger_auto_schema(responses={200: AppointmentsSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Appointments, pk=pk)
        serializer = AppointmentsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AppointmentsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Appointments, pk=pk)
        serializer = AppointmentsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Appointments, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BranchView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchSerializer

    @swagger_auto_schema(responses={200: BranchSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Branch.objects.all()
        serializer = BranchSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=BranchSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchSerializer

    @swagger_auto_schema(responses={200: BranchSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Branch, pk=pk)
        serializer = BranchSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BranchSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Branch, pk=pk)
        serializer = BranchSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Branch, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BranchCompanyCaseAssignmentDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchCompanyCaseAssignmentDetailSerializer

    @swagger_auto_schema(responses={200: BranchCompanyCaseAssignmentDetailSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = BranchCompanyCaseAssignmentDetail.objects.all()
        serializer = BranchCompanyCaseAssignmentDetailSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=BranchCompanyCaseAssignmentDetailSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = BranchCompanyCaseAssignmentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchCompanyCaseAssignmentDetailChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchCompanyCaseAssignmentDetailSerializer

    @swagger_auto_schema(responses={200: BranchCompanyCaseAssignmentDetailSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(BranchCompanyCaseAssignmentDetail, pk=pk)
        serializer = BranchCompanyCaseAssignmentDetailSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BranchCompanyCaseAssignmentDetailSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(BranchCompanyCaseAssignmentDetail, pk=pk)
        serializer = BranchCompanyCaseAssignmentDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(BranchCompanyCaseAssignmentDetail, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CampaignView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CampaignSerializer

    @swagger_auto_schema(responses={200: CampaignSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Campaign.objects.all()
        serializer = CampaignSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CampaignSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CampaignSerializer

    @swagger_auto_schema(responses={200: CampaignSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Campaign, pk=pk)
        serializer = CampaignSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CampaignSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Campaign, pk=pk)
        serializer = CampaignSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Campaign, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class CaseAssignmentDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseAssignmentDetailSerializer

    @swagger_auto_schema(responses={200: CaseAssignmentDetailSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CaseAssignmentDetail.objects.all()
        serializer = CaseAssignmentDetailSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CaseAssignmentDetailSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CaseAssignmentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseAssignmentDetailChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseAssignmentDetailSerializer

    @swagger_auto_schema(responses={200: CaseAssignmentDetailSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseAssignmentDetail, pk=pk)
        serializer = CaseAssignmentDetailSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CaseAssignmentDetailSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseAssignmentDetail, pk=pk)
        serializer = CaseAssignmentDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseAssignmentDetail, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CasePriorityMasterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CasePriorityMasterSerializer

    @swagger_auto_schema(responses={200: CasePriorityMasterSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CasePriorityMaster.objects.all()
        serializer = CasePriorityMasterSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CasePriorityMasterSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CasePriorityMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CasePriorityMasterChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CasePriorityMasterSerializer

    @swagger_auto_schema(responses={200: CasePriorityMasterSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CasePriorityMaster, pk=pk)
        serializer = CasePriorityMasterSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CasePriorityMasterSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CasePriorityMaster, pk=pk)
        serializer = CasePriorityMasterSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CasePriorityMaster, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CaseRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseRegisterSerializer

    @swagger_auto_schema(responses={200: CaseRegisterSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CaseRegister.objects.all()
        serializer = CaseRegisterSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CaseRegisterSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CaseRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseRegisterChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseRegisterSerializer

    @swagger_auto_schema(responses={200: CaseRegisterSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseRegister, pk=pk)
        serializer = CaseRegisterSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CaseRegisterSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseRegister, pk=pk)
        serializer = CaseRegisterSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseRegister, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ClientInvoicesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientInvoicesSerializer

    @swagger_auto_schema(responses={200: ClientInvoicesSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = ClientInvoices.objects.all()
        serializer = ClientInvoicesSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ClientInvoicesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ClientInvoicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientInvoicesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientInvoicesSerializer

    @swagger_auto_schema(responses={200: ClientInvoicesSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ClientInvoices, pk=pk)
        serializer = ClientInvoicesSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ClientInvoicesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ClientInvoices, pk=pk)
        serializer = ClientInvoicesSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ClientInvoices, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ClientQuotationsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientQuotationsSerializer

    @swagger_auto_schema(responses={200: ClientQuotationsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = ClientQuotations.objects.all()
        serializer = ClientQuotationsSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ClientQuotationsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ClientQuotationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientQuotationsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientQuotationsSerializer

    @swagger_auto_schema(responses={200: ClientQuotationsSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ClientQuotations, pk=pk)
        serializer = ClientQuotationsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ClientQuotationsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ClientQuotations, pk=pk)
        serializer = ClientQuotationsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ClientQuotations, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommunicationChannelsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommunicationChannelsSerializer

    @swagger_auto_schema(responses={200: CommunicationChannelsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CommunicationChannels.objects.all()
        serializer = CommunicationChannelsSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CommunicationChannelsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CommunicationChannelsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunicationChannelsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommunicationChannelsSerializer

    @swagger_auto_schema(responses={200: CommunicationChannelsSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CommunicationChannels, pk=pk)
        serializer = CommunicationChannelsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CommunicationChannelsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CommunicationChannels, pk=pk)
        serializer = CommunicationChannelsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CommunicationChannels, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CommunicationDetailsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommunicationDetailsSerializer

    @swagger_auto_schema(responses={200: CommunicationDetailsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CommunicationDetails.objects.all()
        serializer = CommunicationDetailsSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CommunicationDetailsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CommunicationDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunicationDetailsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommunicationDetailsSerializer

    @swagger_auto_schema(responses={200: CommunicationDetailsSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CommunicationDetails, pk=pk)
        serializer = CommunicationDetailsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CommunicationDetailsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CommunicationDetails, pk=pk)
        serializer = CommunicationDetailsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CommunicationDetails, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommunicationsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommunicationsSerializer

    @swagger_auto_schema(responses={200: CommunicationsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Communications.objects.all()
        serializer = CommunicationsSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CommunicationsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CommunicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunicationsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommunicationsSerializer

    @swagger_auto_schema(responses={200: CommunicationsSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Communications, pk=pk)
        serializer = CommunicationsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CommunicationsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Communications, pk=pk)
        serializer = CommunicationsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Communications, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanySerializer

    @swagger_auto_schema(responses={200: CompanySerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Company.objects.all()
        serializer = CompanySerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CompanySerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanySerializer

    @swagger_auto_schema(responses={200: CompanySerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CompanySerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Company, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PriceListView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PriceListSerializer

    @swagger_auto_schema(responses={200: PriceListSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = PriceList.objects.all()
        serializer = PriceListSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=PriceListSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = PriceListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PriceListChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PriceListSerializer

    @swagger_auto_schema(responses={200: PriceListSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(PriceList, pk=pk)
        serializer = PriceListSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PriceListSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(PriceList, pk=pk)
        serializer = PriceListSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(PriceList, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ProductsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductsSerializer

    @swagger_auto_schema(responses={200: ProductsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Products.objects.all()
        serializer = ProductsSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ProductsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductsSerializer

    @swagger_auto_schema(responses={200: ProductsSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProductsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Products, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectTaskProgressView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectTaskProgressSerializer

    @swagger_auto_schema(responses={200: ProjectTaskProgressSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = ProjectTaskProgress.objects.all()
        serializer = ProjectTaskProgressSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ProjectTaskProgressSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ProjectTaskProgressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectTaskProgressChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectTaskProgressSerializer

    @swagger_auto_schema(responses={200: ProjectTaskProgressSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ProjectTaskProgress, pk=pk)
        serializer = ProjectTaskProgressSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProjectTaskProgressSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ProjectTaskProgress, pk=pk)
        serializer = ProjectTaskProgressSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ProjectTaskProgress, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProjectTasksView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectTasksSerializer

    @swagger_auto_schema(responses={200: ProjectTasksSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = ProjectTasks.objects.all()
        serializer = ProjectTasksSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ProjectTasksSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ProjectTasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectTasksChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectTasksSerializer

    @swagger_auto_schema(responses={200: ProjectTasksSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ProjectTasks, pk=pk)
        serializer = ProjectTasksSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProjectTasksSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ProjectTasks, pk=pk)
        serializer = ProjectTasksSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(ProjectTasks, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectsSerializer

    @swagger_auto_schema(responses={200: ProjectsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Projects.objects.all()
        serializer = ProjectsSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ProjectsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectsSerializer

    @swagger_auto_schema(responses={200: ProjectsSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Projects, pk=pk)
        serializer = ProjectsSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProjectsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Projects, pk=pk)
        serializer = ProjectsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Projects, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ServicesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ServicesSerializer

    @swagger_auto_schema(responses={200: ServicesSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Services.objects.all()
        serializer = ServicesSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ServicesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ServicesSerializer

    @swagger_auto_schema(responses={200: ServicesSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Services, pk=pk)
        serializer = ServicesSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ServicesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Services, pk=pk)
        serializer = ServicesSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Services, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskAssignmentDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskAssignmentDetailSerializer

    @swagger_auto_schema(responses={200: TaskAssignmentDetailSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = TaskAssignmentDetail.objects.all()
        serializer = TaskAssignmentDetailSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=TaskAssignmentDetailSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = TaskAssignmentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskAssignmentDetailChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskAssignmentDetailSerializer

    @swagger_auto_schema(responses={200: TaskAssignmentDetailSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(TaskAssignmentDetail, pk=pk)
        serializer = TaskAssignmentDetailSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TaskAssignmentDetailSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(TaskAssignmentDetail, pk=pk)
        serializer = TaskAssignmentDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(TaskAssignmentDetail, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaskView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

    @swagger_auto_schema(responses={200: TaskSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Task.objects.all()
        serializer = TaskSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

    @swagger_auto_schema(responses={200: TaskSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TaskSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Task, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DocumentSerializer

    @swagger_auto_schema(responses={200: DocumentSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Document.objects.all()
        serializer = DocumentSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=DocumentSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DocumentSerializer

    @swagger_auto_schema(responses={200: DocumentSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=DocumentSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Document, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class MeetingView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MeetingSerializer

    @swagger_auto_schema(responses={200: MeetingSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Meeting.objects.all()
        serializer = MeetingSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=MeetingSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MeetingSerializer

    @swagger_auto_schema(responses={200: MeetingSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Meeting, pk=pk)
        serializer = MeetingSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MeetingSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Meeting, pk=pk)
        serializer = MeetingSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Meeting, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NoteSerializer

    @swagger_auto_schema(responses={200: NoteSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Note.objects.all()
        serializer = NoteSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=NoteSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NoteSerializer

    @swagger_auto_schema(responses={200: NoteSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=NoteSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Note, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CaseView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseSerializer

    @swagger_auto_schema(responses={200: CaseSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Case.objects.all()
        serializer = CaseSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CaseSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseSerializer

    @swagger_auto_schema(responses={200: CaseSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Case, pk=pk)
        serializer = CaseSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CaseSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Case, pk=pk)
        serializer = CaseSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Case, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CaseFeedbackView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseFeedbackSerializer

    @swagger_auto_schema(responses={200: CaseFeedbackSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CaseFeedback.objects.all()
        serializer = CaseFeedbackSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CaseFeedbackSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CaseFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseFeedbackChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseFeedbackSerializer

    @swagger_auto_schema(responses={200: CaseFeedbackSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseFeedback, pk=pk)
        serializer = CaseFeedbackSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CaseFeedbackSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseFeedback, pk=pk)
        serializer = CaseFeedbackSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseFeedback, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CallRecordView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CallRecordSerializer

    @swagger_auto_schema(responses={200: CallRecordSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CallRecord.objects.all()
        serializer = CallRecordSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CallRecordSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CallRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CallRecordChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CallRecordSerializer

    @swagger_auto_schema(responses={200: CallRecordSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CallRecord, pk=pk)
        serializer = CallRecordSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CallRecordSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CallRecord, pk=pk)
        serializer = CallRecordSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CallRecord, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChatView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ChatSerializer

    @swagger_auto_schema(responses={200: ChatSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Chat.objects.all()
        serializer = ChatSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ChatSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ChatSerializer

    @swagger_auto_schema(responses={200: ChatSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Chat, pk=pk)
        serializer = ChatSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ChatSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Chat, pk=pk)
        serializer = ChatSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Chat, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class LeadRatingLabelView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LeadRatingLabelSerializer

    @swagger_auto_schema(responses={200: LeadRatingLabelSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = LeadRatingLabel.objects.all()
        serializer = LeadRatingLabelSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LeadRatingLabelSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LeadRatingLabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeadRatingLabelChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LeadRatingLabelSerializer

    @swagger_auto_schema(responses={200: LeadRatingLabelSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(LeadRatingLabel, pk=pk)
        serializer = LeadRatingLabelSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LeadRatingLabelSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(LeadRatingLabel, pk=pk)
        serializer = LeadRatingLabelSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(LeadRatingLabel, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LeadView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LeadSerializer

    @swagger_auto_schema(responses={200: LeadSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Lead.objects.all()
        serializer = LeadSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LeadSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeadChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LeadSerializer

    @swagger_auto_schema(responses={200: LeadSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Lead, pk=pk)
        serializer = LeadSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LeadSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Lead, pk=pk)
        serializer = LeadSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Lead, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ProjectView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

    @swagger_auto_schema(responses={200: ProjectSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Project.objects.all()
        serializer = ProjectSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ProjectSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

    @swagger_auto_schema(responses={200: ProjectSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProjectSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Project, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OpportunityStageView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunityStageSerializer

    @swagger_auto_schema(responses={200: OpportunityStageSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = OpportunityStage.objects.all()
        serializer = OpportunityStageSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OpportunityStageSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = OpportunityStageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpportunityStageChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunityStageSerializer

    @swagger_auto_schema(responses={200: OpportunityStageSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityStage, pk=pk)
        serializer = OpportunityStageSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OpportunityStageSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityStage, pk=pk)
        serializer = OpportunityStageSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityStage, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class OrganisationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganisationSerializer

    @swagger_auto_schema(responses={200: OrganisationSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Organisation.objects.all()
        serializer = OrganisationSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OrganisationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganisationChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganisationSerializer

    @swagger_auto_schema(responses={200: OrganisationSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Organisation, pk=pk)
        serializer = OrganisationSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OrganisationSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Organisation, pk=pk)
        serializer = OrganisationSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Organisation, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializer

    @swagger_auto_schema(responses={200: AccountSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Account.objects.all()
        serializer = AccountSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=AccountSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializer

    @swagger_auto_schema(responses={200: AccountSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AccountSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Account, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ContactView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer

    @swagger_auto_schema(responses={200: ContactSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Contact.objects.all()
        serializer = ContactSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ContactSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer

    @swagger_auto_schema(responses={200: ContactSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Contact, pk=pk)
        serializer = ContactSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ContactSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Contact, pk=pk)
        serializer = ContactSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Contact, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    @swagger_auto_schema(responses={200: ProductSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Product.objects.all()
        serializer = ProductSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    @swagger_auto_schema(responses={200: ProductSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProductSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Product, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OpportunityView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunitySerializer

    @swagger_auto_schema(responses={200: OpportunitySerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Opportunity.objects.all()
        serializer = OpportunitySerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OpportunitySerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = OpportunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpportunityChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunitySerializer

    @swagger_auto_schema(responses={200: OpportunitySerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Opportunity, pk=pk)
        serializer = OpportunitySerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OpportunitySerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Opportunity, pk=pk)
        serializer = OpportunitySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Opportunity, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CaseView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseSerializer

    @swagger_auto_schema(responses={200: CaseSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = Case.objects.all()
        serializer = CaseSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CaseSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseSerializer

    @swagger_auto_schema(responses={200: CaseSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Case, pk=pk)
        serializer = CaseSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CaseSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Case, pk=pk)
        serializer = CaseSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(Case, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CaseFeedbackView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseFeedbackSerializer

    @swagger_auto_schema(responses={200: CaseFeedbackSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = CaseFeedback.objects.all()
        serializer = CaseFeedbackSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CaseFeedbackSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = CaseFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseFeedbackChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CaseFeedbackSerializer

    @swagger_auto_schema(responses={200: CaseFeedbackSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseFeedback, pk=pk)
        serializer = CaseFeedbackSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CaseFeedbackSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseFeedback, pk=pk)
        serializer = CaseFeedbackSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(CaseFeedback, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OpportunityCurrencyCodeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunityCurrencyCodeSerializer

    @swagger_auto_schema(responses={200: OpportunityCurrencyCodeSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = OpportunityCurrencyCode.objects.all()
        serializer = OpportunityCurrencyCodeSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OpportunityCurrencyCodeSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = OpportunityCurrencyCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpportunityCurrencyCodeChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunityCurrencyCodeSerializer

    @swagger_auto_schema(responses={200: OpportunityCurrencyCodeSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityCurrencyCode, pk=pk)
        serializer = OpportunityCurrencyCodeSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OpportunityCurrencyCodeSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityCurrencyCode, pk=pk)
        serializer = OpportunityCurrencyCodeSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityCurrencyCode, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OpportunityProductView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunityProductSerializer

    @swagger_auto_schema(responses={200: OpportunityProductSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        instances = OpportunityProduct.objects.all()
        serializer = OpportunityProductSerializer(instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OpportunityProductSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = OpportunityProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpportunityProductChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpportunityProductSerializer

    @swagger_auto_schema(responses={200: OpportunityProductSerializer})
    def get(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityProduct, pk=pk)
        serializer = OpportunityProductSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OpportunityProductSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityProduct, pk=pk)
        serializer = OpportunityProductSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        instance = get_object_or_404(OpportunityProduct, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
