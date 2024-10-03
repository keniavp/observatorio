from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView

from Seguridad.models import ExtendUser


# Create your views here.
class LoginView(FormView):
    template_name = 'Seguridad/Login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        form.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        return form

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
            return self.form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('/login/')


class UserListView(ListView):
    template_name = "Seguridad/Usuarios/User_List.html"
    model = ExtendUser

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Usuarios'
        context['router'] = "usuarios"
        context['year'] = datetime.today().year
        return context
