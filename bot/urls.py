from django.conf.urls import url
from bot.views import index, say, clear

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^say$', say, name="say"),
    url(r'^clear$', clear, name="clear")
]
