from django.shortcuts import render
from django.views import generic
from .models import Sheet, Checklist
from .forms import SheetForm, ChecklistForm


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'latest_sheet_list'

    # Return in reverse order (Newest to oldest)
    def get_queryset(self):
        return Sheet.objects.order_by('-start_date')


"""class ResultsView(generic.DetailView):
    model = Sheet
    template_name = 'pages/results.html'
"""

class ResultsView(generic.DetailView):
    model = Sheet
    template_name = 'pages/results.html'
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

def sheet_entry_view(request):
    form = ChecklistForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "pages/entry.html", context)

class UpdateView(generic.UpdateView):
    model = Sheet
    template_name = 'pages/update.html'
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


def sheet_entry_view(request):
    form = SheetForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "pages/entry.html", context)
