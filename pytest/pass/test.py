
def get_discount_price(price, discount_percent):
    ### 할인된 가격을 계산합니다 ###
    discount = price * discount_percent / 100
    return price - discount

# test_discount_aaa : AAA 패턴으로 테스트
#     - 10,000원 상품, 20% 할인 -> 8,000원 확인
# test_dicount_gwt : GWT 패턴으로 테스트
#     - 5,000원 상품, 10% 할인 -> 4,500원 확인