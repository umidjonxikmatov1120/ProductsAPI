from django.urls import path

from products.views import ProductsCreateView, ProductsUpdateView, ProductsRetrieveView, \
    ProductsDeleteView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('create/', ProductsCreateView.as_view()),
    path('update/<int:pk>/', ProductsUpdateView.as_view()),
    path('<int:pk>/', ProductsRetrieveView.as_view()),
    path('delete/<int:pk>/', ProductsDeleteView.as_view()),
]
