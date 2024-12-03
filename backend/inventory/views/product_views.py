from inventory.models import Product, ProductOrderingInformations, ProductSpesifications
from tenant.utils import get_tenant
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from inventory.serializers import (
    ProductOrderingInformationsSerializer,
    ProductSerializer,
    ProductSpesificationsSerializer,
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_products(request) -> Response:
    tenant = get_tenant(request)
    products = Product.objects.filter(tenant=tenant)
    serializer = ProductSerializer(products, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_product(request, productId) -> Response:
    tenant = get_tenant(request)
    product = Product.objects.filter(id=productId, tenant=tenant).first()
    serializer = ProductSerializer(product, many=False, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_product_spesifications(request, productId) -> Response:
    try:
        # Assuming productId is the actual ID of the product
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    productSpesifications = ProductSpesifications.objects.filter(product=product)
    serializer = ProductSpesificationsSerializer(
        productSpesifications, many=True, context={"request": productId}
    )
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_product_ordering_informations(request, productId) -> Response:
    try:
        # Assuming productId is the actual ID of the product
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    productOrderingInformations = ProductOrderingInformations.objects.filter(
        product=product
    )
    serializer = ProductOrderingInformationsSerializer(
        productOrderingInformations, many=True, context={"request": productId}
    )
    return Response(serializer.data)
