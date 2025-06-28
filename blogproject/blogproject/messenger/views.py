from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messenger/inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/send_message.html', {'form': form})