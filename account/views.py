from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, get_user_model, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


User = get_user_model()


# Create your views here.




def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect(reverse('home:home'))

    return render(request, 'account/login.html',
                  {'form': form, 'menu': "login"}
                  )


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_staff:
            qs = SubCategory.objects.all().values('title', 'price', 'categories__id', 'categories__title',
                                                  'icon__icon_tag').filter(categories__active=True).order_by(
                'categories__id')
            context = {
                'menu': "servicemenu",
                'qs': qs,

            }
        return render(request, self.template_name, context)

    def get_queryset(self, *args, **kwargs):

        user = self.request.user
        if user.is_staff:
            qs = super(Profile, self).get_queryset(*args, **kwargs).order_by('title').order_by('-active')
            return qs


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')
