from django.core.paginator import Paginator

def paginate_objects(request, queryset, per_page=9):
    queryset = queryset.order_by('id')
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
