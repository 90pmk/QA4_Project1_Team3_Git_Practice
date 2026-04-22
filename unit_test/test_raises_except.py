# test_raises_except.py
import unittest

def divide(a, b):
    """나눗셈 함수 - 0으로 나누면 ValueError 발생"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b

def get_item(items, index):
    """리스트에서 아이템 가져오기 - 범위 초과 시 IndexError"""
    if index < 0 or index >= len(items):
        raise IndexError(f"인덱스 {index}는 범위를 벗어났습니다")
    return items[index]


class TestExceptionHandling(unittest.TestCase):
    
    def test_divide_by_zero_raises_ValueError(self):
        """방법 1: 컨텍스트 매니저 사용 (권장)"""
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_divide_by_zero_with_message(self):
        """방법 2: 예외 메시지까지 검증"""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        
        # 예외 메시지 확인
        self.assertIn("0으로 나눌 수 없습니다", str(context.exception))
    
    def test_index_out_of_range(self):
        """IndexError 테스트"""
        items = [1, 2, 3]
        
        with self.assertRaises(IndexError) as context:
            get_item(items, 10)
        
        self.assertIn("10", str(context.exception))
    
    def test_assertRaisesRegex_pattern_matching(self):
        """방법 3: 정규식으로 메시지 패턴 검증"""
        with self.assertRaisesRegex(ValueError, r"0으로.*나눌"):
            divide(10, 0)
    
    def test_no_exception_when_valid(self):
        """정상 케이스: 예외가 발생하지 않음"""
        result = divide(10, 2)
        self.assertEqual(result, 5.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
