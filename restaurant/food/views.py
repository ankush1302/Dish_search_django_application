from django.shortcuts import render
from django.db.models import Q
from .models import Restaurant
import ast

def dish(request):
    query = request.GET.get('q')
    item_names = []
    error_message = ''

    if query:
        try:
            restaurants = Restaurant.objects.filter(
                Q(items__icontains=query)
            )

            for restaurant in restaurants:
                items_dict = ast.literal_eval(restaurant.items)
                for item_name in items_dict.keys():
                    #print(item_name)
                    if query.lower() in item_name.lower():
                     #   print('Yes')
                        item_names.append(item_name)
                        
            print(item_names)

        except Exception as e:
            error_message = str(e)

    context = {
        'query_provided': query,
        'item_names': item_names,
        'error_message': error_message
    }

    return render(request, 'food/search.html', context)
