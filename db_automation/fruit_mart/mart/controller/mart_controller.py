from rest_framework import viewsets, status
from rest_framework.response import Response

from fruit_mart.mart.service.mart_service_impl import MartServiceImpl
from fruit_mart.mart.repository.mart_repository_impl import MartRepositoryImpl

class MartController(viewsets.ViewSet):
    repository = MartRepositoryImpl()
    mart_service = MartServiceImpl(repository)

    def create_or_update_fruit(self, request):
        fruit_name = request.data.get('fruit_name')
        fruit_number = request.data.get('fruit_number')

        try:
            mart = self.mart_service.update_fruit_stock(fruit_name, fruit_number)
            mart_data = {
                'id': mart.id,
                'fruit_name': mart.fruit_name,
                'fruit_number': mart.fruit_number
            }
            return Response(mart_data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_fruit_by_name(self, request):
        fruit_name = request.GET.get('fruit_name')

        if not fruit_name:
            return Response({'message': '과일을 입력하세요.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': '재고가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    def get_all_fruits(self, request):
        fruits = self.mart_service.get_all_fruits()
        fruit_data = [
            {
                'id': fruit.id,
                'fruit_name': fruit.fruit_name,
                'fruit_number': fruit.fruit_number
            } for fruit in fruits
        ]
        return Response(fruit_data, status=status.HTTP_200_OK)