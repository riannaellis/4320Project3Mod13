import unittest
import Project3
import datetime

class TestProject3(unittest.TestCase):

    def test_validate_symbol(self):
        self.assertEqual(Project3.validate_symbol("GOOGL"), True)
        self.assertEqual(Project3.validate_symbol("G"), True)
        self.assertEqual(Project3.validate_symbol("ABCDEFG"), True)
        self.assertEqual(Project3.validate_symbol("Google"), False)
        self.assertEqual(Project3.validate_symbol("123"), False)
        self.assertEqual(Project3.validate_symbol(""), False)
        self.assertEqual(Project3.validate_symbol("GOOGL11"), False)
        self.assertEqual(Project3.validate_symbol("ABCDEFGH"), False)
 
    def test_validate_chart_type(self):
        self.assertEqual(Project3.validate_chart_type("1"), 'line')
        self.assertEqual(Project3.validate_chart_type("2"), 'bar')
        self.assertEqual(Project3.validate_chart_type("3"), 'none')
        self.assertEqual(Project3.validate_chart_type("0"), 'none')
        self.assertEqual(Project3.validate_chart_type("Abc"), 'none')

    def test_validate_time_series_choice(self):
        self.assertEqual(Project3.validate_time_series_choice("1"), 1)
        self.assertEqual(Project3.validate_time_series_choice("2"), 2)
        self.assertEqual(Project3.validate_time_series_choice("3"), 3)
        self.assertEqual(Project3.validate_time_series_choice("4"), 4)
        self.assertEqual(Project3.validate_time_series_choice("5"), 0)
        self.assertEqual(Project3.validate_time_series_choice("ABC"), 0)

    def test_validate_start_date(self):
        self.assertEqual(Project3.validate_start_date("2020-03-03"), datetime.datetime(2020, 3, 3))
        self.assertEqual(Project3.validate_start_date("03-03-2020"), "none")
        self.assertEqual(Project3.validate_start_date("03/03/2020"), "none")
        self.assertEqual(Project3.validate_start_date("ABC"), "none")

    def test_validate_end_date(self):
        self.assertEqual(Project3.validate_end_date("2020-03-03"), datetime.datetime(2020, 3, 3))
        self.assertEqual(Project3.validate_end_date("03-03-2020"), "none")
        self.assertEqual(Project3.validate_end_date("03/03/2020"), "none")
        self.assertEqual(Project3.validate_end_date("ABC"), "none")

if __name__ == "__main__":
    unittest.main()