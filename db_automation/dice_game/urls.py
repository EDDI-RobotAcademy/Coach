from django.urls import path
from rest_framework.routers import DefaultRouter
from dice_game.controller.controller import gameRecordController

# Create a router for the controller
router = DefaultRouter()
router.register(r'game-record', gameRecordController, basename='game-record')

# Additional URL patterns if needed
urlpatterns = [
    # Map additional methods explicitly if required
    path('save/', gameRecordController.as_view({'get': 'save_game_record', 'post': 'save_game_record'}), name='save_game_record'),
    path('check-winner/', gameRecordController.as_view({'get': 'getSumDice'}), name='getSumDice'),
    path('all/', gameRecordController.as_view({'get': 'get_all_records'}), name='get_all_records'),
    path('record-by-game/', gameRecordController.as_view({'get': 'get_records_by_gameId'}), name='get_records_by_gameId'),
]

# Append router-generated URLs
urlpatterns += router.urls
