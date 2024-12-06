from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fruit_mart.order.serializer.serializer import OrderSerializer
from fruit_mart.order.service.service_repository_impl import OrderServiceImpl



# Create your views here.
class OrderController(viewsets.ViewSet):
    orderService = OrderServiceImpl.getInstance()



    def sell_item(self,request):
        requestCustomer = request.data.get('customer')
        requestNumber = request.data.get('number')
        requestFruit = request.data.get('fruit')

        try:
            order = self.orderService.buyFruit(requestCustomer,requestFruit,requestNumber)
            orderData = {
                'id': order.id,
                'customer': order.requestCustomer,
                'fruit': order.requestFruit,
                'number': order.requestNumber
            }
            return Response(orderData, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    # def requestFindDice(self, request):
    #     requestGetData = request.GET
    #     requestDiceId = requestGetData.get('id')
    #
    #     foundDice = self.diceService.findDice(requestDiceId)
    #
    #     return Response(
    #         model_to_dict(foundDice),
    #         status=status.HTTP_200_OK)
