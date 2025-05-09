# for custom paginations

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response

# custom pagination for companies view
class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page-num'
    max_page_size = 1
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results':data
        })