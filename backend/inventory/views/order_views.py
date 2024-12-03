from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from tenant.utils import get_tenant
from inventory.models import OrderItem, Product
from django.db.models import Sum
from inventory.serializers import OrderSerializer,OrderItemSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order(request) -> Response:
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order_item(request) -> Response:
    orderItem = OrderItem.objects.filter(product = request.data["product"], user = request.user).first()
    serializer = OrderItemSerializer(data=request.data)
    product = Product.objects.filter(id=request.data["product"]).first()
   
    if(orderItem is not None):
        request.data["product"] = product
        request.data["qty"] = orderItem.qty + request.data["qty"]
        request.data["price"] = request.data["qty"] * product.sale_price
        updateSerializer = OrderItemSerializer(orderItem, data=request.data)
        updateSerializer.update(orderItem, request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    request.data["price"] = request.data["qty"] * product.sale_price
    request.data["name"] = product.name + "-" + request.user.email
    if serializer.is_valid():
        serializer.save(user=request.user)  # Set the user to the current logged-in user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_order_item_number(request) -> Response:
    orderItemNumber = OrderItem.objects.filter(user = request.user, isActive = True).aggregate(Sum('qty'))
    return Response(orderItemNumber['qty__sum'])

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_order_items(request) -> Response:
    products = OrderItem.objects.filter(user = request.user, isActive = True)
    serializer = OrderItemSerializer(products, many=True, context={"request": request})
    return Response(serializer.data)