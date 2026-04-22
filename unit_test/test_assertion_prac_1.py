import unittest

def add(a, b):
    return a + b

def is_adult(age):
    return age >= 18

def get_greeting(name):
    if not name:
        return None
    return f"Hello, {name}!"


class TestBasicAssertions(unittest.TestCase):
    
    def test_assertEqual_with_numbers(self):
        """숫자 비교: assertEqual"""
        result = add(2, 3)
        self.assertEqual(result, 5)  # 2 + 3 = 5
    
    def test_assertEqual_with_strings(self):
        """문자열 비교: assertEqual"""
        result = get_greeting("Alice")
        self.assertEqual(result, "Hello, Alice!")
    
    def test_assertTrue_and_assertFalse(self):
        """불리언 검증: assertTrue, assertFalse"""
        self.assertTrue(is_adult(20))   # 20세는 성인
        self.assertFalse(is_adult(15))  # 15세는 미성년
    
    def test_assertIsNone(self):
        """None 검증: assertIsNone"""
        result = get_greeting("")  # 빈 문자열 → None 반환
        self.assertIsNone(result)
        # 위 아래 코드의 결과는 같다.
        # self.assertEqual(result, None)
    
    def test_assertIs_same_object(self):
        """동일 객체 검증: assertIs"""
        list1 = [1, 2, 3]
        list2 = list1  # 같은 객체 참조
        list3 = [1, 2, 3]  # 같은 값, 다른 객체
        
        self.assertIs(list1, list2)      # 같은 객체
        self.assertIsNot(list1, list3)   # 다른 객체
        self.assertEqual(list1, list3)   # 값은 같음


if __name__ == '__main__':
    unittest.main(verbosity=2)
