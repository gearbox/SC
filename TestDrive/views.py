from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from TestDrive.forms import ProfileForm, SCTypeForm  # , MessageForm, BaseMessageFormset
from TestDrive.models import SCType  # , Message

# Create your views here.


@login_required
def test_profile_settings(request):
    """
    Allows a user to update their own profile.
    """
    user = request.user

    # Create the formset, specifying the form and formset we want to use.
    # sc_type_form_set = formset_factory(SCTypeForm, formset=BaseMessageFormset)
    sc_type_form_set = formset_factory(SCTypeForm)

    # Get our existing link data for this user.  This is used as initial data.
    user_sctypes = SCType.objects.filter(user=user).order_by('number')
    sctype_data = [{'name': sctype.name, 'number': sctype.number, 'description': sctype.description}
                   for sctype in user_sctypes]

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, user=user)
        sctype_formset = sc_type_form_set(request.POST)

        if profile_form.is_valid() and sctype_formset.is_valid():
            # Save user info
            user.first_name = profile_form.cleaned_data.get('first_name')
            user.last_name = profile_form.cleaned_data.get('last_name')
            user.save()

            # Now save the data for each form in the formset
            new_sctypes = []

            for sctype_form in sctype_formset:
                name = sctype_form.cleaned_data.get('name')
                number = sctype_form.cleaned_data.get('number')
                description = sctype_form.cleaned_data.get('description')

                if name and number:
                    new_sctypes.append(SCType(user=user, name=name, number=number, description=description))

            try:
                with transaction.atomic():
                    # Replace the old with the new
                    SCType.objects.filter(user=user).delete()
                    SCType.objects.bulk_create(new_sctypes)

                    # And notify our users that it worked
                    messages.success(request, 'You have updated your profile.')

            except IntegrityError:  # If the transaction failed
                messages.error(request, 'There was an error saving your profile.')
                return redirect(reverse('profile-settings'))

    else:
        profile_form = ProfileForm(user=user)
        sctype_formset = sc_type_form_set(initial=sctype_data)

    context = {
        'profile_form': profile_form,
        'sctype_formset': sctype_formset,
    }

    return render(request, 'TestDrive/edit_profile.html', context)


'''
@login_required
def test_profile_settings(request):
    """
    Allows a user to update their own profile.
    """
    # user = request.user
    # sctype = SCType.number
    sctype = request.

    # Create the formset, specifying the form and formset we want to use.
    message_form_set = formset_factory(MessageForm, formset=BaseMessageFormset)

    # Get our existing data for this user.  This is used as initial data.
    # user_messages = Message.objects.filter(user=user).order_by('message')
    type_messages = Message.objects.filter(sctype=sctype).order_by('sctype')
    messages_data = [{'message': message.message, 'language': message.language} for message in type_messages]

    if request.method == 'POST':
        type_form = SCTypeForm(request.POST, sctype=sctype)
        message_formset = message_form_set(request.POST)

        if type_form.is_valid() and message_formset.is_valid():
            # Save user info
            sctype. = profile_form.cleaned_data.get('first_name')
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
