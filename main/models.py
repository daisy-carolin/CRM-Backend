from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE,default='')
    profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name="user_profile",default='')
    password = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return str(self.name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    profilename = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
class UserPrivilege(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    can_add_user = models.BooleanField(default=False)
    can_edit_user = models.BooleanField(default=False)
    can_view_user = models.BooleanField(default=False)
    can_list_user = models.BooleanField(default=False)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_type = models.CharField(max_length=20)

    def __str__(self):
        return str(self.member_type)

class Company(models.Model):
    companyname = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
      return str(self.email)


class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branchname = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return str(self.email)


class Department(models.Model):
    departmentname = models.CharField(max_length=255 ,null = True, blank = True)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return str(self.departmentname)

    

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Meeting(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_meetings')
    participants = models.ManyToManyField(User, related_name='attended_meetings')
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)



class Case(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

class CaseFeedback(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    def __str__(self):
        return str(self.case)

class CallRecord(models.Model):
    ticket_id= models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticket_id)
    

class Chat(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)
    
class LeadRatingLabel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class Lead(models.Model):
    lead_rating = models.ForeignKey(LeadRatingLabel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    contact_person = models.ForeignKey('Contact', on_delete=models.CASCADE, null=True, blank=True)
    opportunity = models.ForeignKey('Opportunity', on_delete=models.CASCADE, null=True, blank=True)
    lead_source = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE ,default='')
    source = models.CharField(max_length=255,null=True, blank=True)
  
    def __str__(self):
        return str(self.title)

class Products(models.Model):
    productname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.description)
    

class Services(models.Model):
    servicename = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.description)
    

class PriceList(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.price)
    
class Campaign(models.Model):
    campaignname = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return str(self.campaignname)

class CommunicationChannels(models.Model):
    channelname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self. description)


class Communications(models.Model):
    channel = models.ForeignKey(CommunicationChannels, on_delete=models.CASCADE)
    date = models.DateField()
    subject = models.CharField(max_length=255)

    def __str__(self):
        return str(self.channel)
    

class BranchCompanyCaseAssignmentDetail(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE ,default='')
    company= models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.company)

class CasePriorityMaster(models.Model):
    priorityname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.description)


class CaseRegister(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE ,default='')
    company= models.ForeignKey(Company, on_delete=models.CASCADE)
    priority= models.ForeignKey(CasePriorityMaster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.branch)

class ClientInvoices(models.Model):
    client= models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return str(self.client)

class ClientQuotations(models.Model):
    client= models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return str(self.client)
    

class TaskAssignmentDetail(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,default='')
    task = models.ForeignKey('ProjectTasks', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class ProjectTaskProgress(models.Model):
    task= models.ForeignKey('ProjectTasks', on_delete=models.CASCADE)
    progresspercentage = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.task)
    

class ProjectTasks(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)
    taskname = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.task)
    

class Projects(models.Model):
    projectname = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return str(self.enddate)

 
class Appointments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.date)

class CommunicationDetails(models.Model):
    communication = models.ForeignKey(Communications, on_delete=models.CASCADE)
    detailtype = models.CharField(max_length=255)
    detailcontent = models.TextField()

    def __str__(self):
        return str(self.detail)


class CaseAssignmentDetail(models.Model):
    case = models.ForeignKey(CaseRegister, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')

    def __str__(self):
        return str(self.user)
    

class Project(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class OpportunityStage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    probability = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)
    
    
class Organisation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
    
class Account(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
class OpportunityCurrencyCode(models.Model):
    code = models.CharField(max_length=3)  # Example: USD, EUR, etc.

    def __str__(self):
        return str(self.code)



class OpportunityProduct(models.Model):
    opportunity = models.ForeignKey('Opportunity', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.email)

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    valid_till = models.DateField(blank=True, null=True)
    product_owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    organization = models.ForeignKey(Organisation, related_name="products", on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Opportunity(models.Model):
    opportunity_name = models.CharField(max_length=100, default="", blank=True, null=True)
    account = models.ForeignKey(Account,related_name="opportunities", on_delete=models.SET_NULL, default=None, blank=True, null=True)
    stage = models.ForeignKey(OpportunityStage,related_name="opportunities", on_delete=models.SET_NULL, default=None, blank=True, null=True)
    currency= models.ForeignKey(OpportunityCurrencyCode,related_name="opportunities", on_delete=models.SET_NULL, default=None, blank=True, null=True)
    amount = models.DecimalField( decimal_places=2, max_digits=12, blank=True, null=True)
    product_name = models.ForeignKey(Product, related_name="opportunities",null=True, blank=True, on_delete=models.SET_NULL)
    contact_name = models.ForeignKey(Contact, related_name="opportunities",null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name="opportunity_created_by", on_delete=models.SET_NULL,blank=True, null=True)
    close_date = models.DateField(null=False, blank=False)
    closed_by = models.ForeignKey(User,related_name="opportunity_closed_by", on_delete=models.SET_NULL, blank=True, null=True)
    remarks = models.TextField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    assigned_to = models.ManyToManyField(User,blank=True,related_name="opportunity_assigned_user")
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organisation,related_name="opportunities", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.opportunity_name)
