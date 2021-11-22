from django import forms
from .models import Sheet, Checklist

class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = [
            'name',
            'start_date',
            'employment_type',
            'title',
            'department',
            'sub_department',
            'team',
            'sub_team',
            'reports_to',
            'location',
            'personal_email',
            'address',
            'email',
            'manager',
            
        ]
    # Ensures validity of null ImageField
    def __init__(self, *args, **kwargs):
        super(SheetForm, self).__init__(*args, **kwargs)

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = [
            'jira_ticket_closed',
            'reach_out_to_manager',
            'device_type',
            'computer_shipped',
            
            'confirm_in_gmail',
            'reach_out_hiring_managers_with_email',
            'reach_out_to_Lorraine_with_email_and_tracking_info',
            'add_employee_id_to_google_profile',
            'add_to_google_groups',

            'add_to_active_directory',
            'add_to_active_directory_developers',
            'add_to_active_directory_infrastructure',
            
            'invite_to_Atlassian',

            'confirm_in_okta',
            'add_to_okta_groups',

            'invite_to_1Password',
            'invite_to_Slack',
            'invite_to_Looker',
            'invite_to_CodeSignal',

            'add_vmware_workspace',

            # SGE
            'add_to_SGE_google_groups',
            'add_to_Teamwork_Global',
            'add_to_Salesforce_in_okta',
            'send_username_to_Autumn_Young_for_Salesforce',
            'add_to_TalkDesk',
            'add_to_OpenAdmin',
            'add_to_extra_Google_Groups',
            'add_to_1Password_US_SGE_Group',
            'add_to_microsoft_office_365',
            
            # After user logs ins
            'sign_in_Okta',
            'user_index_flip_to_128',

            'ask_clx_sge_new_hire_to_allow_access_to_nro',
            'create_nro_account',
        ]
    # Ensures validity of null ImageField
    def __init__(self, *args, **kwargs):
        super(ChecklistForm, self).__init__(*args, **kwargs)