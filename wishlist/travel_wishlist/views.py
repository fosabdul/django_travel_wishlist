from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm 

def place_list(request):

  
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()     
        if form.is_valid():      
            place.save()        # Saves to the database 
            return redirect('place_list')    # redirects to GET view with name place_list - which is this same view 


 
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', { 'places': places, 'new_place_form': new_place_form })


def places_visited(request):
    visited = Place.objects.filter(visited=True) 
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })

"""See a list of places that have been visited
• Be able to check off a place that has been
visited
"""
def place_was_visited(request, place_pk): 
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True #Verify the page displays only visited=True places
        place.save()
    
    return redirect('place_list')

"""Place.objects is a Manager. A manager lets
you run queries against the table and
returns QuerySet objects. A QuerySet
represents a set of objects from the
database"""
    