from django.shortcuts import render, redirect
from bot.models import Message
import cleverbot

cb = cleverbot.Cleverbot("CC62ho-5twjh0shkV6pqs85zvoA")

# Create your views here.
def index(request):
    messages = Message.objects.all()
    return render(request, "index.html", context={"messages": messages})

def say(request):
    if request.method == "POST":
        msg = request.POST["message"]
        message = Message.objects.create(body=msg, is_bot=False)
        message.save()
        reply = cb.say(message)
        bot_msg = Message.objects.create(body=reply, is_bot=True)
        bot_msg.save()
    return redirect("/")

def clear(request):
    Message.objects.all().delete()
    return redirect("/")
