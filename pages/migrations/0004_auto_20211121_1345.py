# Generated by Django 3.2.9 on 2021-11-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20211121_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='add_employee_id_to_google_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_1Password_US_SGE_Group',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_OpenAdmin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_SGE_google_groups',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_Salesforce_in_okta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_TalkDesk',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_Teamwork_Global',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_active_directory',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_active_directory_developers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_active_directory_infrastructure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_extra_Google_Groups',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_google_groups',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_microsoft_office_365',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_to_okta_groups',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='add_vmware_workspace',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='ask_clx_sge_new_hire_to_allow_access_to_nro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='computer_shipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='confirm_in_gmail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='confirm_in_okta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='create_nro_account',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='device_type',
            field=models.CharField(blank=True, choices=[('W', 'Windows'), ('M16', 'Mac 16GB'), ('M32', 'Mac 32GB'), ('BYOD', 'BYOD')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='invite_to_1Password',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='invite_to_Atlassian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='invite_to_CodeSignal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='invite_to_Looker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='invite_to_Slack',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='jira_ticket_closed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='reach_out_hiring_managers_with_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='reach_out_to_Lorraine_with_email_and_tracking_info',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='reach_out_to_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='send_username_to_Autumn_Young_for_Salesforce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='sign_in_Okta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='user_index_flip_to_128',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='manager',
            field=models.BooleanField(default=False),
        ),
    ]