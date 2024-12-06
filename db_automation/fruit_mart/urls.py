from django.urls import path
from . import controller  # controller.py 파일을 import
from fruit_mart.mart.controller.mart_controller import MartController

urlpatterns = [
    path('', controller.index, name='index'),  # 기본 경로에 대해 index 뷰로 매핑
    path('inventory/', MartController.get_all_fruits, name='get_all_fruits'),  # 현재 재고 확인
    path('inventory/<str:fruit_name>/', MartController.get_fruit_by_name, name='get_fruit_by_name'),  # 단권 재고 조회
    path('add-stock/', MartController.create_or_update_fruit, name='create_or_update_fruit'),  # 입고 작업
    #path('sell/', controller.sell_item, name='sell_item'),  # 판매 작업
    #path('customer-actions/', controller.get_customer_actions, name='customer_actions'),  # 고객 행동 이력 조회
]
