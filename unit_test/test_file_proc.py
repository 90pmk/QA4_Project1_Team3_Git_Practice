# test_file_proc.py
import unittest
import tempfile
import os

class FileProcessor:
    """파일 처리 클래스"""
    def __init__(self, filepath):
        self.filepath = filepath
    
    def write(self, content):
        with open(self.filepath, 'w') as f:
            f.write(content)
    
    def read(self):
        with open(self.filepath, 'r') as f:
            return f.read()
    
    def append(self, content):
        with open(self.filepath, 'a') as f:
            f.write(content)


class TestFileProcessor(unittest.TestCase):
    
    def setUp(self):
        """각 테스트 전에 임시 파일 생성"""
        # 임시 파일 생성
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w', 
            delete=False,  # 자동 삭제 비활성화 (우리가 직접 관리)
            suffix='.txt'
        )
        self.temp_file.close()
        self.filepath = self.temp_file.name
        self.processor = FileProcessor(self.filepath)
        print(f"\n📁 setUp: 임시 파일 생성 - {self.filepath}")
    
    def tearDown(self):
        """각 테스트 후에 임시 파일 삭제"""
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
            print(f"🗑️ tearDown: 임시 파일 삭제 - {self.filepath}")
    
    def test_write_and_read(self):
        """파일 쓰기/읽기 테스트"""
        self.processor.write("Hello, World!")
        content = self.processor.read()
        self.assertEqual(content, "Hello, World!")
    
    def test_append(self):
        """파일 추가 쓰기 테스트"""
        self.processor.write("First line\n")
        self.processor.append("Second line")
        content = self.processor.read()
        self.assertIn("First line", content)
        self.assertIn("Second line", content)


if __name__ == '__main__':
    unittest.main(verbosity=2)
