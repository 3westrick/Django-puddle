from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation, ConvMessage
from item.models import Item
from .forms import ConversationMessageForm


# Create your views here.

def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.user == request.user:
        return redirect("dashboard:index")
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        return redirect('conversation:conv', pk=conversations.first().id)
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.user = request.user
            conversation_message.save()
            return redirect('item:show', pk=item_pk)
    form = ConversationMessageForm()
    return render(request, 'conversation/new.html', {'form': form})


def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'conversation/inbox.html', {'conversations': conversations})


def show(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.user = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:conv', pk=pk)
    form = ConversationMessageForm()
    return render(request, 'conversation/show.html', {'conversation': conversation, 'form': form})
