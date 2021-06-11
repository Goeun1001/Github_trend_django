from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ScrollPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        total_pages = self.page.paginator.num_pages
        return Response({
            'count': self.page.paginator.count,
            'total_pages': total_pages,
            'results': data
        })