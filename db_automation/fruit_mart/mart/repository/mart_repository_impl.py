from fruit_mart.mart.entity.mart import Mart
from fruit_mart.mart.repository.mart_repository import MartRepository

class MartRepositoryImpl(MartRepository):
    def find_by_fruit_name(self, fruit_name):
        mart = Mart.objects.filter(fruit_name=fruit_name).first()
        return mart

    def find_all(self):
        return Mart.objects.all()

    def save(self, mart):
        # 이미 존재하는 과일인지 확인
        existing_mart = Mart.objects.filter(fruit_name=mart.fruit_name).first()

        if existing_mart:
            # 과일이 있으면 수량 업데이트
            existing_mart.fruit_number = mart.fruit_number
            existing_mart.save()
            return existing_mart
        else:
            # 과일이 없으면 네임, 수량 새로 업데이트
            mart.save()
            return mart








