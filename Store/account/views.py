from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('flowers')


class RegisterPage(FormView):
    template_name = 'account/Register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super(RegisterPage, self).get(*args, **kwargs)
