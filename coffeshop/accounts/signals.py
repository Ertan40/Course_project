from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

UserModel = get_user_model()



@receiver(signal=post_save, sender=UserModel)
def send_greeting_email_after_registration(instance, created, **kwargs):
    if not created:
        return

    user_email = instance.email

    send_mail(
        subject='Your registration is successful!',
        message="Welcome to SugarAngel CoffeeShop "
                "We're delighted to have you here. "
                "Please check our Catalogue and let's us know which desert is your favourite"
                "Have a lovely day :)",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user_email, ),
    )