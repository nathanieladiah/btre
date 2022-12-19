from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# def register(request):
# 	if request.method == 'POST':
# 		# Register user
# 		# Get form values
# 		first_name = request.POST['first_name']
# 		last_name = request.POST['last_name']
# 		username = request.POST['username']
# 		email = request.POST['email']
# 		password = request.POST['password']
# 		password2 = request.POST['password2']

# 		# Check if passwords match
# 		if password == password2:
# 			# Check username
# 			if User.objects.filter(username=username).exists():
# 				messages.error(request, 'Username already exists')
# 				return redirect('register')

# 			else:
# 				if User.objects.filter(email=email).exists():
# 					messages.error(request, 'Email already exists')
# 					return redirect('register')
				
# 				else:
# 					# looks good
# 					user = User.objects.create_user(
# 						username=username,
# 						password=password,
# 						email=email,
# 						first_name=first_name,
# 						last_name=last_name,
# 					)

# 					# Login after register

# 					# auth.login(request, user)
# 					# messages.success(request, 'You are now logged in')
# 					# return redirect('index')

# 					# Redirect user to login page
# 					user.save()
# 					messages.success(request, 'You are now registered and can log in')
# 					return redirect('login')
# 		else:
# 			messages.error(request, 'Passwords do not match')
# 			return redirect('register')

# 	return render(request, 'accounts/register.html')

def register(request):
	if request.method == 'POST':
		# Get Form values
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		# Check passwords
		if password != password2:
			messages.error(request, 'Passwords do not match')
			return redirect('register')
		
		# Check username
		if User.objects.filter(username=username).exists():
			messages.error(request, 'Username already exists')
			return redirect('register')

		# Check email
		if User.objects.filter(email=email).exists():
			messages.error(request, 'Email already exists')
			return redirect('register')

		# Looks good
		user = User.objects.create_user(
			username=username,
			password=password,
			email=email,
			first_name=first_name,
			last_name=last_name,
		)

		# Redirect to login page
		user.save()
		messages.success(request, 'You are registered and may now login')
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
