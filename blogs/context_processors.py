from .models import Category 
from .models import SocialLink, MyWeb

# Nav Bar categories passing through 
def get_categories(request): 
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)

def get_my_web(request):
    my_web = MyWeb.objects.all()
    return dict(my_web=my_web)