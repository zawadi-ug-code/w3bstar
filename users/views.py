from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout, login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
	"""Log da user out."""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	"""register a new user."""
	if request.method != 'POST':
		# display a blank registration form.
		form = UserCreationForm()
	else:
		# process completed form.
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Log da user in and then redirect da homepage.
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context)