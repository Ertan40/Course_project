from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


from coffeshop.accounts.forms import UserCreateForm

UserModel = get_user_model()

class IndexView(views.TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['permissions'] = self.request.user.has_perm('accounts.view_appuser')
    #     return context


class SignUpView(views.CreateView):
    template_name = 'accounts/signup-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignOutView(LogoutView):
    template_name = 'accounts/logout-page.html'



class UserDetailsView(views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_owner'] = self.request.user == self.object
    #     return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/user-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email')

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk', self.request.user.pk})


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')