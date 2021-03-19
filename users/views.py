from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account screated for {username}!')
            return redirect('patterns-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})



#options for messages
#message.debug
#message.info
#.success
#.warning
#.error
