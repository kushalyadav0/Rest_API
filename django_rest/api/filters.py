import django_filters
from blogs.models import Blog, Comments

class BlogFilter(django_filters.FilterSet):
    blog_title = django_filters.CharFilter(field_name = 'blog_title', lookup_expr ='iexact') # as we are using iexact, now this will accept case insensitive letteres as well
    blog_body = django_filters.CharFilter(field_name = 'blog_body', lookup_expr = 'iexact') # we will use lookup_expr as "icontains"as if we want to filter things that contains what we are writing in filter blog.
    # filtering in range of the given id 
    id = django_filters.RangeFilter(field_name = 'id')
    # we can use RangeFilter if we are filtering by the primary key 
    # to do the same with blog_id we need to go a bit advanced like defining function for minimum and maximum value of blog_id
    blog_id_min = django_filters.CharFilter(method = 'filter_by_blog_id_range')
    blog_id_max = django_filters.CharFilter(method = 'filter_by_blog_id_range')

    class Meta():
        model = Blog
        fields = ['blog_title', 'blog_body', 'blog_id_min', 'blog_id_max']

    def filter_by_blog_id_range(self, queryset, name, value):
        if name == 'blog_id_min':
            return queryset.filter(blog_id__gte=value) # here __gte represents values greater than value
        
        elif name == 'blog_id_max':
             return queryset.filter(blog_id__lte=value) # here __lte represents values less than value
        else:
            return queryset