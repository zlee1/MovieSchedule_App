from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import urllib
from bs4 import BeautifulSoup
from .forms import TheaterSearchForm
from .models import Theater, Subscription

def home(request):
    return render(request, 'subscriptions/home.html')

def login(request):
    return render(request, 'subscriptions/login.html', context={'title': 'Login'})

@login_required
def manage(request):
    current_user = request.user

    if(request.method == 'POST'):
        form = TheaterSearchForm(request.POST)
        if(form.is_valid()):
            zip_code = form.cleaned_data.get('zip_code')

            return redirect('subscriptions-search', zip_code=zip_code)
    else:
        form = TheaterSearchForm()
    
    return render(request, 'subscriptions/manage.html', context={'title': 'Manage', 'form': form, 'subscriptions':current_user.subscription_set.order_by('theater')})

def theater_search(request, zip_code='00000'):

    theater_list = []

    if(zip_code != '00000'):
        url = f'https://www.fandango.com/{zip_code}_movietimes'

        zip_search = urllib.request.urlopen(url)
        zip_search_page = BeautifulSoup(zip_search.read().decode('utf8'), 'html.parser')

        zip_search.close()

        theaters = zip_search_page.find(id='nearby-theaters-select-list').find_all('option') # list of all theaters on page

        for theater in theaters[1:]:
            theater_dict = {}
            theater_dict['id'] = theater["value"].replace('/', '').replace('theater-page', '')[-5:] # end of url is theater id
            theater_dict['name'] = theater.text.strip()
            theater_dict['url'] = f'https://www.fandango.com{theater["value"]}'

            if(theater_dict not in theater_list):
                theater_list.append(theater_dict)

    
    form = TheaterSearchForm()

    if(request.method == 'POST'):
        if('zip_code' in request.POST.keys()):
            form = TheaterSearchForm(request.POST)
            if(form.is_valid()):
                return redirect('subscriptions-search', zip_code=request.POST.get('zip_code'))
        else:
            subscribed_theaters = []

            for id, _ in request.POST.items():
                for theater in theater_list:
                    if(id == theater['id']):

                        theater_obj = None

                        if(not Theater.objects.filter(id=id)):
                            theater_obj = Theater()
                            theater_obj.id = theater.get('id')
                            theater_obj.name = theater.get('name')
                            theater_obj.url = theater.get('url')
                            theater_obj.save()

                        sub_obj = Subscription()
                        sub_obj.theater = theater_obj if theater_obj is not None else Theater.objects.get(id=id)
                        sub_obj.user = request.user

                        if(not Subscription.objects.filter(theater=sub_obj.theater, user=sub_obj.user)):
                            sub_obj.save()
                            subscribed_theaters.append(theater['name'])

            if(subscribed_theaters):
                messages.success(request, f'Subscribed successfully!')
            
            return redirect('subscriptions-search', zip_code='00000')
            

    context = {'title': 'Search', 'form': form, 'zip_code': zip_code, 'theaters': theater_list}

    return render(request, 'subscriptions/theater_search.html', context=context)

def unsubscribe(request, theater_id='all'):
    if(theater_id != 'all'):
        theater = Theater.objects.filter(id=theater_id).first()
        request.user.subscription_set.get(theater=theater).delete()
        messages.success(request, f'Unsubscribed from {theater.name}')
        return redirect('subscriptions-manage')


    if(request.method == 'POST'):
        if(theater_id == 'all'):
            for subscription in request.user.subscription_set.all():
                subscription.delete()
        messages.success(request, 'Unsubscribed from all theaters')
        return redirect('subscriptions-manage')

    context = {'title': 'Unsubscribe', 'theater_id': theater_id}
    return render(request, 'subscriptions/unsubscribe.html', context=context)