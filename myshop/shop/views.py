from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .models import Products, Cart
from .permissions import IsOwner
from .serializer import ProductsSerializer, CartSerializer


class ProductsAPIViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner, ]


class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class ProductsSearchView(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            return Products.objects.filter(name__icontains=query)
        return Products.objects.all()


class ProductsSortView(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        sort_by = self.request.query_params.get('sort', None)

        if sort_by:
            if sort_by in ['name', 'price', 'count']:
                return queryset.order_by(sort_by)
            elif sort_by.startswith('-') and sort_by[1:] in ['name', 'price', 'count']:
                return queryset.order_by(sort_by)

        return queryset
