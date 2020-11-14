from django.contrib.auth import authenticate, login, logout

def login(request):
  user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

  if user is not None:
    login(request, user)
    # Redirect to a success page.
  else:
     # Return an 'invalid login' error message.
    pass

def logout(request):
    logout(request)
    # Redirect to a success page.
