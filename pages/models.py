import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Sheet(models.Model):
    """User info model"""

    name = models.CharField(max_length=30, unique=True)
    start_date = models.DateField()
    employment_type_choices = (
        ("FT","FT Employee"),("NT","Contractor / Intern"))
    employment_type = models.CharField(
        max_length=25,choices=employment_type_choices,default="FT")
    title = models.CharField(max_length=35)
    department_choices = ((
        "P","Product"),("C","Consumer"),("O","Operations"),("S","SG Enterprise"),("PO","People Ops"),("F","Finance"),
        ("BS","Business Systems"),("SC","Security & Compliance"))
    department = models.CharField(
        max_length=25,choices=department_choices)
    sub_department = models.CharField(max_length=25,null=True,blank=True)
    team = models.CharField(max_length=25,null=True,blank=True)
    sub_team = models.CharField(max_length=25,null=True,blank=True)
    reports_to = models.CharField(max_length=25,null=True,blank=True)
    location = models.CharField(max_length=25)
    personal_email = models.EmailField()
    address = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    manager = models.BooleanField(default=False)
    # - Not form fields
    pub_date = models.DateTimeField(
        'date published',auto_now_add=True, editable=False, null=False, blank=True)
    edit_date = models.DateTimeField(
        'date of last edit',auto_now=True, editable=False, null=False, blank=True)

    slug = models.SlugField(null=True,blank=True,unique=True)

    def __str__(self):
        return self.name

    # Test if updated recently
    def was_edited_recently(self):
        return self.edit_date >= timezone.now() - datetime.timedelta(days=1)

    # Redirect after saving a new entry - INT
    """def get_absolute_url(self):
        return u'/pages/%d' % (self.id)"""
    
    # Redirect after saving a new entry - SLUG
    def get_absolute_url(self):
        return reverse('pages', kwargs={'slug': (self.slug).replace('-','')})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name).replace('-','')
        return super().save(*args, **kwargs)    



class Checklist(models.Model):
    '''Generate checklist and store alongside user'''

    user = models.ForeignKey(Sheet,on_delete=models.CASCADE)
    jira_ticket_closed = models.BooleanField(default=True)
    reach_out_to_manager = models.BooleanField(default=False)
    device_choices = (("W","Windows"),("M16","Mac 16GB"),("M32","Mac 32GB"),("BYOD","BYOD"))
    device_type = models.CharField(null=True,blank=True,max_length=25,choices=device_choices)
    computer_shipped = models.BooleanField(default=False)
    
    confirm_in_gmail = models.BooleanField(default=False)
    reach_out_hiring_managers_with_email = models.BooleanField(default=False)
    reach_out_to_Lorraine_with_email_and_tracking_info= models.BooleanField(default=False)
    add_employee_id_to_google_profile = models.BooleanField(default=False)
    add_to_google_groups = models.BooleanField(default=False)

    add_to_active_directory = models.BooleanField(default=False)
    add_to_active_directory_developers = models.BooleanField(default=False)
    add_to_active_directory_infrastructure = models.BooleanField(default=False)
    
    invite_to_Atlassian = models.BooleanField(default=False)

    confirm_in_okta = models.BooleanField(default=False)
    add_to_okta_groups = models.BooleanField(default=False)

    invite_to_1Password = models.BooleanField(default=False)
    invite_to_Slack = models.BooleanField(default=False)
    invite_to_Looker = models.BooleanField(default=False)
    invite_to_CodeSignal = models.BooleanField(default=False)

    add_vmware_workspace = models.BooleanField(default=False)

    # SGE
    add_to_SGE_google_groups = models.BooleanField(default=False)
    add_to_Teamwork_Global = models.BooleanField(default=False)
    add_to_Salesforce_in_okta = models.BooleanField(default=False)
    send_username_to_Autumn_Young_for_Salesforce = models.BooleanField(default=False)
    add_to_TalkDesk = models.BooleanField(default=False)
    add_to_OpenAdmin = models.BooleanField(default=False)
    add_to_extra_Google_Groups = models.BooleanField(default=False)
    add_to_1Password_US_SGE_Group = models.BooleanField(default=False)
    add_to_microsoft_office_365 = models.BooleanField(default=False)
    
    # After user logs ins
    sign_in_Okta = models.BooleanField(default=False)
    user_index_flip_to_128 = models.BooleanField(default=False)

    ask_clx_sge_new_hire_to_allow_access_to_nro = models.BooleanField(default=False)
    create_nro_account = models.BooleanField(default=False)











    