from django.contrib import admin
from .models import Trace, Channel, Message, Frame

admin.site.register(Trace)
admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(Frame)

