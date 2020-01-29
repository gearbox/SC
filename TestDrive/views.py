from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from TestDrive.forms import ProfileForm, SCTypeForm  # , MessageForm, BaseMessageFormset
from TestDrive.models import SCType  # , Message

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

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


def index(request):
    return HttpResponse("Hello world. This is TestDrive App index.")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'TestDrive/signup.html'
