from django.urls import path, include
from . import controller  # controller.py 파일을 import
from rest_framework.routers import DefaultRouter

from fruit_mart.order.controller.order_controller import OrderController

router = DefaultRouter()
router.register(r"fruit_mart", OrderController, basename='fruit_mart')

urlpatterns = [
    path('', controller.index, name='index'),  # 기본 경로에 대해 index 뷰로 매핑
    #path('inventory/', controller.get_inventory, name='get_inventory'),  # 현재 재고 확인
    #path('add-stock/', controller.add_stock, name='add_stock'),  # 입고 작업
    #path('sell/', controller.sell_item, name='sell_item'),  # 판매 작업
    #path('customer-actions/', controller.get_customer_actions, name='customer_actions'),  # 고객 행동 이력 조회
    path('buy-fruit/',OrderController.as_view({'get':'requestBuyFruit'}),
         name='과일구매'),
]
