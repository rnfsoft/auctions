from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .forms import SignUpForm
from .models import User
# Create your views here.

def home(request):
    return render(request, 'base.html', {'content': ''})

class SingUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'my_account.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

