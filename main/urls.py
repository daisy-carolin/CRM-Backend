from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .models import*

urlpatterns = [
    path('user', views.UserView.as_view(), name='user_api'),
    path('user_update/<int:pk>/', views.UserChangeView.as_view(), name='user_update'),

    path('user_profile', views.UserProfileView.as_view(), name='user_profile_api'),
    path('user_profile_update/<int:pk>/', views.UserProfileChangeView.as_view(), name='user_profile_update'),

    path('department', views.DepartmentView.as_view(), name='department_api'),
    path('department_update/<int:pk>/', views.DepartmentChangeView.as_view(), name='department_update'),

    path('member', views.MemberView.as_view(), name='member_api'),
    path('member_update/<int:pk>/', views.MemberChangeView.as_view(), name='member_update'),

    path('user_privilege/', views.UserPrivilegeView.as_view(), name='user_privilege_api'),
    path('user_privilege_update/<int:pk>/', views.UserPrivilegeChangeView.as_view(), name='user_privilege_update'),

    path('appointments/', views.AppointmentsView.as_view(), name='appointment_api'),
    path('appointments_update/<int:pk>/', views.AppointmentsChangeView.as_view(), name='appointment_update'),

    path('branch/', views.BranchView.as_view(), name='branch_api'),
    path('branch_update/<int:pk>/', views.BranchChangeView.as_view(), name='branch_update'),

    path('branch_company_case_assignment_detail/', views.BranchCompanyCaseAssignmentDetailView.as_view(), name='branch_company_case_assignment_detail_api'),
    path('branch_company_case_assignment_detail_update/<int:pk>/', views.BranchCompanyCaseAssignmentDetailChangeView.as_view(), name='branch_company_case_assignment_detail_update'),

    path('campaign/', views.CampaignView.as_view(), name='campaign_api'),
    path('campaign_update/<int:pk>/', views.CampaignChangeView.as_view(), name='campaign_update'),

    path('case_assignment_detail/', views.CaseAssignmentDetailView.as_view(), name='case_assignment_detail_api'),
    path('case_assignment_detail_update/<int:pk>/', views.CaseAssignmentDetailChangeView.as_view(), name='case_assignment_detail_update'),

    path('case_priority_master/', views.CasePriorityMasterView.as_view(), name='case_priority_master_api'),
    path('case_priority_master_update/<int:pk>/', views.CasePriorityMasterChangeView.as_view(), name='case_priority_master_update'),

    path('case_register/', views.CaseRegisterView.as_view(), name='case_register_api'),
    path('case_register_update/<int:pk>/', views.CaseRegisterChangeView.as_view(), name='case_register_update'),

    path('client_invoices/', views.ClientInvoicesView.as_view(), name='client_invoices_api'),
    path('client_invoices_update/<int:pk>/', views.ClientInvoicesChangeView.as_view(), name='client_invoices_update'),

    path('client_quotations/', views.ClientQuotationsView.as_view(), name='client_quotations_api'),
    path('client_quotations_update/<int:pk>/', views.ClientQuotationsChangeView.as_view(), name='client_quotations_update'),

    path('communication_channels/', views.CommunicationChannelsView.as_view(), name='communication_channels_api'),
    path('communication_channels_update/<int:pk>/', views.CommunicationChannelsChangeView.as_view(), name='communication_channels_update'),

    path('communication_details/', views.CommunicationDetailsView.as_view(), name='communication_details_api'),
    path('communication_details_update/<int:pk>/', views.CommunicationDetailsChangeView.as_view(), name='communication_details_update'),

    path('communications/', views.CommunicationsView.as_view(), name='communications_api'),
    path('communications_update/<int:pk>/', views.CommunicationsChangeView.as_view(), name='communications_update'),

    path('company/', views.CompanyView.as_view(), name='company_api'),
    path('company_update/<int:pk>/', views.CompanyChangeView.as_view(), name='company_update'),

    path('price_list/', views.PriceListView.as_view(), name='price_list_api'),
    path('price_list_update/<int:pk>/', views.PriceListChangeView.as_view(), name='price_list_update'),

    path('products/', views.ProductView.as_view(), name='products_api'),
    path('products_update/<int:pk>/', views.ProductChangeView.as_view(), name='products_update'),

    path('project_task_progress/', views.ProjectTaskProgressView.as_view(), name='project_task_progress_api'),
    path('project_task_progress_update/<int:pk>/', views.ProjectTaskProgressChangeView.as_view(), name='project_task_progress_update'),

    path('project_tasks/', views.ProjectTasksView.as_view(), name='project_tasks_api'),
    path('project_tasks_update/<int:pk>/', views.ProjectTasksChangeView.as_view(), name='project_tasks_update'),

    path('projects/', views.ProjectsView.as_view(), name='projects_api'),
    path('projects_update/<int:pk>/', views.ProjectsChangeView.as_view(), name='projects_update'),

    path('services/', views.ServicesView.as_view(), name='services_api'),
    path('services_update/<int:pk>/', views.ServicesChangeView.as_view(), name='services_update'),

    path('task_assignment_detail/', views.TaskAssignmentDetailView.as_view(), name='task_assignment_detail_api'),
    path('task_assignment_detail_update/<int:pk>/', views.TaskAssignmentDetailChangeView.as_view(), name='task_assignment_detail_update'),

    path('user/', views.UserView.as_view(), name='user_api'),
    path('user_update/<int:pk>/', views.UserChangeView.as_view(), name='user_update'),

    path('user_profile/', views.UserProfileView.as_view(), name='user_profile_api'),
    path('user_profile_update/<int:pk>/', views.UserProfileChangeView.as_view(), name='user_profile_update'),

    path('user_privilege/', views.UserPrivilegeView.as_view(), name='user_privilege_api'),
    path('user_privilege_update/<int:pk>/', views.UserPrivilegeChangeView.as_view(), name='user_privilege_update'),

    path('member/', views.MemberView.as_view(), name='member_api'),
    path('member_update/<int:pk>/', views.MemberChangeView.as_view(), name='member_update'),

    path('department/', views.DepartmentView.as_view(), name='department_api'),
    path('department_update/<int:pk>/', views.DepartmentChangeView.as_view(), name='department_update'),

    path('task/', views.TaskView.as_view(), name='task_api'),
    path('task_update/<int:pk>/', views.TaskChangeView.as_view(), name='task_update'),

    path('document/', views.DocumentView.as_view(), name='document_api'),
    path('document_update/<int:pk>/', views.DocumentChangeView.as_view(), name='document_update'),

    path('meeting/', views.MeetingView.as_view(), name='meeting_api'),
    path('meeting_update/<int:pk>/', views.MeetingChangeView.as_view(), name='meeting_update'),

    path('note/', views.NoteView.as_view(), name='note_api'),
    path('note_update/<int:pk>/', views.NoteChangeView.as_view(), name='note_update'),

    path('case/', views.CaseView.as_view(), name='case_api'),
    path('case_update/<int:pk>/', views.CaseChangeView.as_view(), name='case_update'),

    path('case_feedback/', views.CaseFeedbackView.as_view(), name='case_feedback_api'),
    path('case_feedback_update/<int:pk>/', views.CaseFeedbackChangeView.as_view(), name='case_feedback_update'),

    path('call_record/', views.CallRecordView.as_view(), name='call_record_api'),
    path('call_record_update/<int:pk>/', views.CallRecordChangeView.as_view(), name='call_record_update'),

    path('chat/', views.ChatView.as_view(), name='chat_api'),
    path('chat_update/<int:pk>/', views.ChatChangeView.as_view(), name='chat_update'),

    path('lead_rating_label/', views.LeadRatingLabelView.as_view(), name='lead_rating_label_api'),
    path('lead_rating_label_update/<int:pk>/', views.LeadRatingLabelChangeView.as_view(), name='lead_rating_label_update'),

    path('lead/', views.LeadView.as_view(), name='lead_api'),
    path('lead_update/<int:pk>/', views.LeadChangeView.as_view(), name='lead_update'),

    path('project/', views.ProjectView.as_view(), name='project_api'),
    path('project_update/<int:pk>/', views.ProjectChangeView.as_view(), name='project_update'),

    path('opportunity_stage/', views.OpportunityStageView.as_view(), name='opportunity_stage_api'),
    path('opportunity_stage_update/<int:pk>/', views.OpportunityStageChangeView.as_view(), name='opportunity_stage_update'),

    path('organisation/', views.OrganisationView.as_view(), name='organisation_api'),
    path('organisation_update/<int:pk>/', views.OrganisationChangeView.as_view(), name='organisation_update'),

    path('account/', views.AccountView.as_view(), name='account_api'),
    path('account_update/<int:pk>/', views.AccountChangeView.as_view(), name='account_update'),

    path('opportunity_currency_code/', views.OpportunityCurrencyCodeView.as_view(), name='opportunity_currency_code_api'),
    path('opportunity_currency_code_update/<int:pk>/', views.OpportunityCurrencyCodeChangeView.as_view(), name='opportunity_currency_code_update'),

    path('opportunity_product/', views.OpportunityProductView.as_view(), name='opportunity_product_api'),
    path('opportunity_product_update/<int:pk>/', views.OpportunityProductChangeView.as_view(), name='opportunity_product_update'),

    path('contact/', views.ContactView.as_view(), name='contact_api'),
    path('contact_update/<int:pk>/', views.ContactChangeView.as_view(), name='contact_update'),

    path('product/', views.ProductView.as_view(), name='product_api'),
    path('product_update/<int:pk>/', views.ProductChangeView.as_view(), name='product_update'),

    path('opportunity/', views.OpportunityView.as_view(), name='opportunity_api'),
    path('opportunity_update/<int:pk>/', views.OpportunityChangeView.as_view(), name='opportunity_update'),
]


    
