from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from TestDrive.forms import MessageForm, TypeForm, BaseMessageFormset
from TestDrive.models import Message, SCType


# Create your views here.

'''
@login_required
def test_profile_settings(request):
    """
    Allows a user to update their own profile.
    """
    # user = request.user
    # sc_type = SCType.number
    sc_type = request.

    # Create the formset, specifying the form and formset we want to use.
    message_form_set = formset_factory(MessageForm, formset=BaseMessageFormset)

    # Get our existing data for this user.  This is used as initial data.
    # user_messages = Message.objects.filter(user=user).order_by('message')
    type_messages = Message.objects.filter(sc_type=sc_type).order_by('sc_type')
    messages_data = [{'message': message.message, 'language': message.language} for message in type_messages]

    if request.method == 'POST':
        type_form = TypeForm(request.POST, sc_type=sc_type)
        message_formset = message_form_set(request.POST)

        if type_form.is_valid() and message_formset.is_valid():
            # Save user info
            sc_type. = profile_form.cleaned_data.get('first_name')
            user.last_name = profile_form.cleaned_data.get('last_name')
            user.save()

            # Now save the data for each form in the formset
            new_links = []

            for link_form in link_formset:
                anchor = link_form.cleaned_data.get('anchor')
                url = link_form.cleaned_data.get('url')

                if anchor and url:
                    new_links.append(UserLink(user=user, anchor=anchor, url=url))

            try:
                with transaction.atomic():
                    # Replace the old with the new
                    UserLink.objects.filter(user=user).delete()
                    UserLink.objects.bulk_create(new_links)

                    # And notify our users that it worked
                    messages.success(request, 'You have updated your profile.')

            except IntegrityError:  # If the transaction failed
                messages.error(request, 'There was an error saving your profile.')
                return redirect(reverse('profile-settings'))

    else:
        profile_form = ProfileForm(user=user)
        message_formset = message_form_set(initial=link_data)

    context = {
        'profile_form': profile_form,
        'link_formset': link_formset,
    }

    return render(request, 'our_template.html', context)
'''


def index(request):
    return HttpResponse("Hello world. This is TestDrive App index.")
