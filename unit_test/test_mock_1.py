# test_mock_1.py
from unittest.mock import Mock, MagicMock

# 1. 기본 Mock 객체 생성
mock_obj = Mock()

# Mock은 어떤 속성이든, 어떤 메서드든 자동으로 생성!
print(mock_obj.any_attribute)        # <Mock ...>
print(mock_obj.any_method())         # <Mock ...>
print(mock_obj.deep.nested.call())   # <Mock ...>

# 2. 반환값 설정 : 없으면 값 반환하지 않음
mock_calculator = Mock()
mock_calculator.add.return_value = 10

result = mock_calculator.add(3, 7)  # 실제로 3+7을 계산하지 않음
print(result)  # 10 (설정한 값 반환)

# 3. 호출 확인
mock_calculator.add(3, 7)
mock_calculator.add.assert_called()           # 호출되었는지 확인
mock_calculator.add.assert_called_with(3, 7)  # 특정 인자로 호출되었는지 # 중요!!
# mock_calculator.add.assert_called_once()      # 정확히 1번 호출되었는지

# 4. MagicMock - 매직 메서드 지원
mock_list = MagicMock()
mock_list.__len__.return_value = 5
print(len(mock_list))  # 5

mock_list.__iter__.return_value = iter([1, 2, 3])
for item in mock_list:
    print(item)  # 1, 2, 3
