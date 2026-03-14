from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_view(request):
    menu_items=[
        {'name': 'Pizza', 'price': 10, 'available': True, 'category': 'Main Course'},
        {'name': 'Burger', 'price': 8, 'available': False, 'category': 'Main Course'},
        {'name': 'Salad', 'price': 5, 'available': True, 'category': 'Appetizer'},
        {'name': 'Ice Cream', 'price': 4, 'available': True, 'category': 'Dessert'},
        {'name': 'Cola', 'price': 12, 'available': False, 'category': 'Drinks'},
        {'name': 'Water', 'price': 5, 'available': True, 'category': 'Drinks'},
    ]

    # getting the data from the forms in web app
    selected_category = request.GET.get('category')
    search_query = request.GET.get('search')

    if selected_category:
        menu_items = [item for item in menu_items if item['category'] == selected_category]

    if search_query:
        menu_items = [item for item in menu_items if search_query.lower() in item['name'].lower()]

    context = {
        "restaurant_name": "Alaa's Kitchen",
        "menu_items": menu_items,
        "selected_category": selected_category,
        "search_query": search_query,
    }
    return render(request, "menu/menu.html", context)    