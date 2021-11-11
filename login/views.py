from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, PasswordForm, RegisterForm

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import Http404

UserModel = get_user_model()

class LoginView(TemplateView):
    template_name = 'login/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request,self.template_name,{'form': form})

    def post(self,request):
        form = LoginForm(request.POST)

        print(request.POST.get('email'),request.POST.get('passw'))

        if form.is_valid():
            email = request.POST.get('email')
            passw = request.POST.get('passw')

            try:
                user = authenticate(username=email, password=passw)
                if user:
                    if user.is_active:
                        login(request, user)
                        return redirect('/')
            except Exception as e:
                print('Login Views Error:',e)


        args = {'form': form,}
        return render(request, self.template_name, args,)



class PasswordView(TemplateView):
    template_name = 'login/password.html'

    def get(self, request):
        form = PasswordForm()
        return render(request,self.template_name,{'form': form})

    def post(self,request):
        form = PasswordForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')

        args = {'form': form,}
        return render(request, self.template_name, args,)



class RegisterView(TemplateView):
    template_name = 'login/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request,self.template_name,{'form': form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            passw = request.POST.get('passw')
            user = authenticate(username=email, password=passw)

            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('login/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request,'login/email.html')

        return render(request, self.template_name, {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('/')
    else:
        raise Http404("Invalid link")




