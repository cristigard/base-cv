from django.shortcuts import render,redirect
from .models import CustomUser
from .admin import UserCreationForm
from .forms import UserUpdateForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form':form})


@login_required()
def profile(request):
	form = UserUpdateForm(instance = request.user)
	if request.method == "POST":
		form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = UserUpdateForm(instance = request.user)

	return render(request, 'users/profile.html', {'form':form})


# class UserLoginView(LoginView):
# 	template_name = 'users/login.html'
# 	fields = '__all__'
# 	redirect_authenticated_user = True 
# 	def get_success_url(self): # + redirect_authenticated_user = True -> send to other view if user is already auth and try to access login page
# 		return reverse_lazy('home')


def login_user_view(request):
	form = UserLoginForm()
	if request.method == "POST":
		form = UserLoginForm(request.POST)
		if form.is_valid():
			email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			user = authenticate(request, email=email, password=password)
			if user is not None:
				messages.success(request, f'Login successfully!')
				login(request, user)
				tk = request.user.tk
				return redirect('cv', tk)
			else:
				messages.warning(request, f'Username or password incorrect!')
				
	else:
		form = UserLoginForm()
	context = {'form': form}			
	return render(request, 'users/login.html', context)


class UserLogoutView(LogoutView):
	next_page = 'home'

class UserChangePassView(LoginRequiredMixin, PasswordChangeView):   
	template_name = 'users/password_change_form.html'
	success_url = reverse_lazy('password_change_done')

class UserChangePassDoneView(LoginRequiredMixin, PasswordChangeDoneView):
	template_name = 'users/password_change_done.html'

