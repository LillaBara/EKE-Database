from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import FormView
# from . forms import RegisterForm

# Create your views here.

def homepage(request):
    return HttpResponse('Intro page')

class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('hikes:hikes')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

#class RegisterView(FormView):
#    template_name = 'registration/register.html'
#    form_class = RegisterForm
#    redirect_authenticated_user = True
#    success_url = reverse_lazy('hikes:hikes')
#
#    def form_valid(self, form):
#        user = form.save()
#        if user:
#            login(self.request, user)
#        return super(RegisterView, self).form_valid(form)  # ne returneaza Reg cu formul valid si salveaza