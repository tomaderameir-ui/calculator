import unittest
import tkinter as tk
from calculator_gui import CalculatorApp

class TestCalculatorGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_addition_ui(self):
        """اختبار عملية الجمع عبر محاكاة الضغط على الأزرار"""
        self.app.on_click('5')
        self.app.on_click('+')
        self.app.on_click('3')
        self.app.on_click('=')
        self.assertEqual(self.display_text(), "8")

    def test_clear_button(self):
        """اختبار زر المسح"""
        self.app.on_click('9')
        self.app.on_click('C')
        self.assertEqual(self.display_text(), "")

    def display_text(self):
        return self.app.display.get()

if __name__ == "__main__":
    unittest.main()
