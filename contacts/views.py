from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .models import Contact


def contact(request):
	if request.method == 'POST':
		listing_id = request.POST['listing_id']
		listing = request.POST['listing']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']

		# check if user made inquiry already
		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
			if has_contacted:
				messages.error(request, 'You have already made an inquiry for this listing')
				return redirect('listing', listing_id)

		contact = Contact(
			listing=listing,
			listing_id=listing_id,
			name=name,
			email=email,
			phone=phone,
			message=message,
			user_id=user_id,
		)

		contact.save()

		# Send email
		# Checkout using email templates.
		send_mail(
			'Property Listing Inquiry',
			f'There has been an inquiry for {listing}. Sign into the admin panel for more information.',
			settings.EMAIL_HOST_USER,
			[realtor_email, 'nathyadiah@gmail.com'],
			fail_silently=False
		)

		messages.success(request, 'Your request has been submitted, a realtor will get back to you soon.')

		return redirect('listing', listing_id)
