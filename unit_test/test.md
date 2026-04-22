# 전체
python3 -m unittest discover

# 모듈
python3 -m unittest [모듈 이름]

# 모듈 내 특정 클래스
python3 -m unittest [모듈 이름].클래스 이름
python3 -m unittest test_calculator.TestA

# 모듈 내 특정 메서드
python3 -m unittest test_calculator.TestA.test_a