from django.urls import path

from inventory.views import product_views as views


urlpatterns = [
    path("", views.get_products, name="get_products"),
    path("<str:productId>/", views.get_product, name="get_product"),
    path(
        "spesifications/<str:productId>/",
        views.get_product_spesifications,
        name="get_product_spesifications",
    ),
    path(
        "ordering-informations/<str:productId>/",
        views.get_product_ordering_informations,
        name="get_product_ordering_informations",
    ),
]
