from django.shortcuts import redirect, render


def register(request):
	if request.method == 'POST':
		# Register user
		return redirect('login')

	return render(request, 'accounts/register.html')

def login(request):
	if request.method == 'POST':
		# Login user
		return redirect('index')

	return render(request, 'accounts/login.html')


def logout(request):
	return redirect('index')

def dashboard(request):
	return render(request, 'accounts/dashboard.html')
