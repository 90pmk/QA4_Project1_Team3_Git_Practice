# test_shopping_cart.py
import unittest

class ShoppingCart:
    """장바구니 클래스"""
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
    
    def get_total(self):
        return sum(item["price"] for item in self.items)
    
    def clear(self):
        self.items = []


class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        """각 테스트 전에 새로운 장바구니 생성"""
        print(f"\n🛒 setUp: 새 장바구니 생성")
        self.cart = ShoppingCart()
        # 기본 상품 추가 (공통 테스트 데이터)
        self.cart.add_item("사과", 1000)
        self.cart.add_item("바나나", 1500)
    
    def test_initial_items(self):
        """초기 상품 개수 확인"""
        print("  테스트: 초기 상품 개수")
        self.assertEqual(len(self.cart.items), 2)
    
    def test_add_item(self):
        """상품 추가 테스트"""
        print("  테스트: 상품 추가")
        self.cart.add_item("오렌지", 2000)
        self.assertEqual(len(self.cart.items), 3)
    
    def test_get_total(self):
        """총액 계산 테스트"""
        print("  테스트: 총액 계산")
        self.assertEqual(self.cart.get_total(), 2500)  # 1000 + 1500
    
    def test_clear_cart(self):
        """장바구니 비우기 테스트"""
        print("  테스트: 장바구니 비우기")
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
