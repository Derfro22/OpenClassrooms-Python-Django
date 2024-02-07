
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm, ListingForm

def band_list(request):
    bands = Band.objects.all()
    return render(request,
    'listings/band_list.html',
    {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
    'listings/band_detail.html',
    {'band': band}) 

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:   
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_edit(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,
    'listings/band_edit.html',
    {'form': form})

def band_delete(request, band_id):

    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request,
    'listings/band_delete.html',
    {'band': band})

def listings_list(request):
    listings = Listing.objects.all()
    return render(request,
    'listings/listings_list.html',
    {'listings': listings})

def listings_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request,
    'listings/listings_detail.html',
    {'listing': listing})

def listings_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request,
            'listings/listings_create.html',
            {'form': form})

def listings_edit(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request,
    'listings/listings_edit.html',
    {'form': form})

def listings_delete(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')
    return render(request,
    'listings/listings_delete.html',
    {'listing': listing})    

def about(request):
    return render(request,
    'listings/about.html')

def contact(request):  

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request,
    'listings/contact.html',
    {'form': form})

def email_sent(request):
    return render(request,
    'listings/email_sent.html')