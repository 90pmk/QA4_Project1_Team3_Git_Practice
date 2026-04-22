# test_p74.py
import unittest

class MockDatabase:
    """실제 DB 대신 쓰는 가짜 DB 클래스"""

    def connect(self):
        print("  DB 연결됨")

    def disconnect(self):
        print("  DB 연결 해제됨")

    def begin_transaction(self):
        print("  트랜잭션 시작")

    def rollback(self):
        print("  트랜잭션 롤백")


class TestDatabaseOps(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n🔧 setUpClass: 데이터베이스 연결")
        cls.db = MockDatabase()
        cls.db.connect()

    @classmethod
    def tearDownClass(cls):
        print("\n🔧 tearDownClass: 데이터베이스 연결 해제")
        cls.db.disconnect()

    def setUp(self):
        print("\n📋 setUp: 트랜잭션 시작")
        self.db.begin_transaction()

    def tearDown(self):
        print("📋 tearDown: 트랜잭션 롤백")
        self.db.rollback()

    def test_insert(self):
        print("테스트: INSERT")
        self.assertIsNotNone(self.db)

    def test_select(self):
        print("테스트: SELECT")
        self.assertIsNotNone(self.db)

    def test_update(self):
        print("테스트: UPDATE")
        self.assertIsNotNone(self.db)


if __name__ == '__main__':
    unittest.main(verbosity=2)