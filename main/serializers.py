from rest_framework import serializers
from .models import (
    Appointments, Branch, BranchCompanyCaseAssignmentDetail, Campaign, CaseAssignmentDetail, CasePriorityMaster, CaseRegister, ClientInvoices, ClientQuotations, CommunicationChannels, CommunicationDetails, Communications, Company, PriceList, Products, ProjectTaskProgress, ProjectTasks, Projects, Services, TaskAssignmentDetail, User, UserProfile,UserPrivilege, Member, Department, Task, Document, Meeting, Note,
   Case, CaseFeedback, CallRecord, Chat, LeadRatingLabel, Lead, 
    Project, OpportunityStage, Organisation, Account, OpportunityCurrencyCode,
    OpportunityProduct, Contact, Product, Opportunity
)

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'department','branch']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'avatar', 'profilename', 'description']

class UserPrivilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPrivilege
        fields = ['user', 'can_add_user', 'can_edit_user', 'can_view_user', 'can_list_user']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'member_type']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['companyname', 'address', 'phone', 'email']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['branchname', 'address', 'phone', 'email']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [ 'departmentname', 'description']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assigned_user', 'created_at']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'file', 'uploaded_by', 'created_at']

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['created_by', 'participants', 'title', 'start_time', 'end_time', 'created_at']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content', 'created_by', 'created_at']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['title', 'status','assigned_user', 'department']

class CaseFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseFeedback
        fields = ['case', 'feedback_text']

class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = ['ticket_', 'owner']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['title']

class LeadRatingLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadRatingLabel
        fields = ['title']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['lead_rating', 'title', 'status','assigned_user', 'department',
                  'contact_person', 'opportunity', 'lead_source', 'created_at', 'updated_at', 'lead', 'branch', 'source']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product', 'productname', 'description']

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = [ 'servicename', 'description']

class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ['product', 'price']

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['campaignname', 'startdate', 'enddate']

class CommunicationChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationChannels
        fields = [ 'channelname', 'description']

class CommunicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communications
        fields = ['date', 'subject']

class BranchCompanyCaseAssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchCompanyCaseAssignmentDetail
        fields = [ 'branch',]

class CasePriorityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasePriorityMaster
        fields = [ 'priorityname', 'description']

class CaseRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseRegister
        fields = ['branch',]

class ClientInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInvoices
        fields = ['client', 'amount', 'date']

class ClientQuotationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientQuotations
        fields = ['quotation', 'client', 'amount', 'date']

class TaskAssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignmentDetail
        fields = ['user', 'task']

class ProjectTaskProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTaskProgress
        fields = ['task', 'progresspercentage', 'date']

class ProjectTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTasks
        fields = ['task', 'project', 'taskname', 'description']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['project', 'projectname', 'startdate', 'enddate']

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['user', 'date', 'time']

class CommunicationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationDetails
        fields = ['detail','detailtype', 'detailcontent']

class CaseAssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseAssignmentDetail
        fields = ['caseassignment', 'user']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title']

class OpportunityStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityStage
        fields = ['name', 'description', 'probability']

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name']

class OpportunityCurrencyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityCurrencyCode
        fields = ['code']

class OpportunityProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityProduct
        fields = ['opportunity', 'product', 'quantity', 'unit_price']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'created_by']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'product_code', 'category', 'valid_till', 'product_owner', 'description', 'organization', 'created_at']

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['opportunity_name', 'account', 'stage', 'currency', 'amount', 'product_name', 'contact_name', 'created_by',
                  'close_date', 'closed_by', 'remarks', 'description', 'assigned_to', 'created_at', 'organization']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['title', 'status','assigned_user', 'department']

class CaseFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseFeedback
        fields = ['feedback_text']

class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = ['ticket_id', 'owner']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['title']

class LeadRatingLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadRatingLabel
        fields = ['title']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['lead_rating', 'title', 'status','assigned_user', 'department',
                  'contact_person', 'opportunity', 'lead_source', 'created_at', 'updated_at','branch', 'source']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product', 'productname', 'description']

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['servicename', 'description']

class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ['product','price']

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [ 'campaignname', 'startdate', 'enddate']

class CommunicationChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationChannels
        fields = ['channelname', 'description']

class CommunicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communications
        fields = ['date', 'subject']

class BranchCompanyCaseAssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchCompanyCaseAssignmentDetail
        fields = ['branch', ]

class CasePriorityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasePriorityMaster
        fields = [ 'priorityname', 'description']

class CaseRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseRegister
        fields = ['branch',  ]

class ClientInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInvoices
        fields = ['client', 'amount', 'date']

class ClientQuotationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientQuotations
        fields = ['client', 'amount', 'date']

class TaskAssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignmentDetail
        fields = [ 'user',]

class ProjectTaskProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTaskProgress
        fields = ['progresspercentage', 'date']

class ProjectTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTasks
        fields =['taskname', 'description']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['projectname', 'startdate', 'enddate']



class CommunicationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationDetails
        fields = [ 
            'detailtype', 'detailcontent']

class CaseAssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseAssignmentDetail
        fields = [ 'user']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title']

class OpportunityStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityStage
        fields = ['name', 'description', 'probability']

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name']

class OpportunityCurrencyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityCurrencyCode
        fields = ['code']

class OpportunityProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityProduct
        fields = ['opportunity', 'product', 'quantity', 'unit_price']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'created_by']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'product_code', 'category', 'valid_till', 'product_owner', 'description', 'organization', 'created_at']

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['opportunity_name', 'account', 'stage', 'currency', 'amount', 'product_name', 'contact_name', 'created_by',
                  'close_date', 'closed_by', 'remarks', 'description', 'assigned_to', 'created_at', 'organization']




