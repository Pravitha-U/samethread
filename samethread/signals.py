import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SampleModel

@receiver(post_save, sender=SampleModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal Thread ID: {}".format(threading.get_ident()))  # Print thread ID