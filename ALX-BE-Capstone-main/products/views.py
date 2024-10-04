from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# Custom pagination class for ProductViewSet
# Limits the number of products per page to 5
class ProductPagination(PageNumberPagination):
    page_size = 5

# ViewSet for managing Product model
# Provides CRUD operations for products, with authentication and filtering options
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Fetches all Product objects
    serializer_class = ProductSerializer  # Uses ProductSerializer for serialization
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read access to everyone, write access to authenticated users
    pagination_class = ProductPagination  # Applies custom pagination 
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]  # Enables searching and filtering

    # Filters for searching by category name, price range, and stock quantity
    filterset_fields = {
        'category__name': ['exact'],         # Filter by exact category name
        'price': ['gte', 'lte'],             # Filter by price (greater than or equal, less than or equal)
        'stock_quantity': ['gte']            # Filter by available stock (greater than or equal)
    }
    search_fields = ['name', 'description', 'category__name']  # Allows searching by name, description, or category name

# ViewSet for managing Category model
# Provides CRUD operations for categories
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Fetches all Category objects
    serializer_class = CategorySerializer  # Uses CategorySerializer for serialization
