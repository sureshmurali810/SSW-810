import unittest
from HW08_Suresh_Murali import date_arithmetic, file_reader, FileAnalyzer


class TestModuleGeneratorFile(unittest.TestCase):
    def test_date_arithmetic(self):
        """to verify that date_arithmetic works properly"""
        self.assertEqual(date_arithmetic(), ('03/01/20', '03/02/19', 303))
        self.assertEqual(date_arithmetic(), ('03/01/2020', '03/02/2019', 1303))

    def test_file_reading_gen(self):
        """to verify that file_reading_gen works properly"""
        directory = 'C:\Users\Suresh Murali\Documents\Portfolio\python 810\HW08\student_major.txt'
        self.assertEqual([x for x in file_reader(directory, 3, "|", False)], [('123', 'Jin He', 'Computer Science'),
('234', 'Nanda Koka', 'Software Engineering'),
('345', 'Benji Cai', 'Software Engineering')])
        self.assertEqual([x for x in file_reader("student_major.txt", 3, "|", False)], [('123', 'Jin He', 'Computer Science'),
('234', 'Nanda Koka', 'Software Engineering'),
('345', 'Benji Cai', 'Software')])

    def test_file_analyzing_summary(self):
        """to verify that file_analyzer works properly"""
        directory = 'C:\Users\Suresh Murali\Documents\Portfolio\python 810\HW08'   # Here you can change the directory
        analyzer = FileAnalyzer(directory)
        # print(analyzer.files_summary)
        self.assertEqual(analyzer.files_summary, {'HW08_Suresh_Murali.py': {'Characters': 5187, 'Lines': 146, 'Classes': 1, 'Functions': 5},
        'HW08_Test_Suresh_Murali.py': {'Characters': 1612, 'Lines': 33, 'Classes': 1, 'Functions': 3}})

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
