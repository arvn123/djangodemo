from shop.models import Category

def menu_links(request):
    c=Category.objects.all()
    return {'links':c}  #we can use this globally across all webpages inside our app
