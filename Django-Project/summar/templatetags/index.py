from django import template
register = template.Library()

@register.filter
def index(List, i):
    #print("Original List",List)
    print("i",i)
    #print(List[i])
    return List[int(i)]
