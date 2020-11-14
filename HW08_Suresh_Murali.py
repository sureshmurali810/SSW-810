# Homework 08
# SSW 810
# Suresh Murali
# 10452425

from datetime import datetime, timedelta
import os
from prettytable import PrettyTable
from pipenv.vendor.vistir.compat import FileNotFoundError
from pkg_resources import NotADirectoryError

""" Part 1 """


def date_arithmetic():

    # 1.1 What is the date three days after Feb 27, 2020?

    date1 = "Feb 27, 2020"
    dt1 = datetime.strptime(date1, '%b %d, %Y')
    three_days_after_02272020 = dt1 + datetime.timedelta(days=3)

    # 1.2 What is the date three days after Feb 27, 2019?

    date2 = "Feb 27, 2019  "
    dt2 = datetime.strptime(date2, '%b %d, %Y')
    three_days_after_02272019 = dt2 + datetime.timedelta(days=3)

    # 1.3 How many days passed between Feb 1, 2019 and Sep 30, 2019?

    date3 = "Feb 1, 2019"
    date4 = "Sep 30, 2019"
    dt3 = datetime.strptime(date3, '%b %d, %Y')
    dt4 = datetime.strptime(date4, '%b %d, %Y')
    days_passed_02012019_09302019 = dt4 - dt3

    return three_days_after_02272020.strftime('%Y-%m-%d'),
    three_days_after_02272019.strftime('%Y-%m-%d'),
    days_passed_02012019_09302019


"""
Part 2
"""


def file_reader(path, fields, sep, header):

    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print("Can't open the file", path)
    else:
        line_count = 0
        with fp:
            for line in fp:
                line_count += 1
                try:
                    sep_line = tuple(line.strip('\n').split(sep))
                    if len(sep_line) != fields:
                        # verify whether the separated
                        # fields consistent with expected
                        raise ValueError

                except ValueError:
                    print("{} has {} fields on line {},but expected {} fields."
                    .format(path, len(sep_line), line_count, fields))

                else:
                    if header == True:
                        header = False
                        continue
                    else:
                        yield sep_line


"""
Part 3
"""


class FileAnalyzer:
    """Class which consist of 3 functions solely for file analyzing purpose"""
    def __init__(self, directory):
        """ Initializes the variable or fucntion"""
        self.directory = directory
        self.files_summary = {}
        self.analyze_files()

    def analyze_files(self):
        """ To Analyze the file and create a counts of character and so on."""
        try:
            d_open = os.listdir(self.directory)
            os.chdir(self.directory)
        except NotADirectoryError:
            raise("Directory not Found.")
        else:
            for file_name in d_open:
                if file_name.endswith(".py"):
                    try:
                        fp = open(file_name, 'r')
                    except FileNotFoundError:
                        raise("Error File not Found.")
                    else:
                        with fp:
                            line_count = 0
                            ch_count = 0
                            func_count = 0
                            class_count = 0
                            for line in fp:
                                line_count = line_count + 1
                                ch_count = ch_count + len(line)
                                s_line = line.strip()
                                if s_line.startswith("def") and s_line.endswith("):"):
                                    func_count = func_count + 1
                                if s_line.startswith("class ") and s_line.endswith(": "):
                                    class_count = class_count + 1
                            self.files_summary[file_name] = {"Characters": ch_count,
                            "Lines": line_count,
                            "Classes": class_count, "Functions": func_count}
            self.prettytable()
            print(self.files_summary)


def prettytable(self):
        """ To Create a PrettyTable."""
        pt = PrettyTable(
         field_names=
          ['FileName', 'Characters', 'Lines', 'Classes', 'Functions'])
        # print(self.files_summary)
        for key, value in self.files_summary.items():
            pt.add_row([key, value['Characters'], value['Lines'],
            value['Classes'], value['Functions']])

        return(pt)

def main():
    directory = 'C:\Users\Suresh Murali\Documents\Portfolio\python 810\HW08'
    x = FileAnalyzer(directory)
    print(x.prettytable())


if __name__ == '__main__':
    main()
directory = 'C:\Users\Suresh Murali\Documents\Portfolio\python 810\HW08'
# directory can be changed here
FileAnalyzer(directory)
