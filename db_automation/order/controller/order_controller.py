from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fruit_mart.order.serializer.serializer import OrderSerializer
from fruit_mart.order.service.service_repository_impl import OrderServiceImpl


# Create your views here.
class OrderController(viewsets.ViewSet):
    orderService = OrderServiceImpl.getInstance()

    def requestBuyFruit(self, request):
        requestGetData = request.GET
        requestId=requestGetData.get('id')
        requestCustomer = requestGetData.get('customer')
        requestNumber = requestGetData.get('number')
        requestFruit = requestGetData.get('fruit')

        buyFruit = self.orderService.buyFruit(
            requestCustomer,requestNumber,requestFruit)

        return Response(buyFruit, status=status.HTTP_200_OK)

    # def requestFindDice(self, request):
    #     requestGetData = request.GET
    #     requestDiceId = requestGetData.get('id')
    #
    #     foundDice = self.diceService.findDice(requestDiceId)
    #
    #     return Response(
    #         model_to_dict(foundDice),
    #         status=status.HTTP_200_OK)
