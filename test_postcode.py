import unittest
import part1
import part3

class ValidateRegex(unittest.TestCase):
    def setUp(self):
        self.postcode_fail_list = ["$%± ()()","XX XXX","A1 9A","LS44PL",
                              "Q1A 9AA","V1A 9AA","X1A 9BB","LI10 3QP",
                              "LJ10 3QP","LZ10 3QP","A9Q 9AA","AA9C 9AA",
                              "FY10 4PL","SO1 4QQ"]
        self.postcode_pass_list = ["EC1A 1BB","W1A 0AX",
                              "M1 1AE","B33 8TH","CR2 6XH","DN55 1PT",
                              "GIR 0AA","SO10 9AA","FY9 9AA","WC1A 9AA"]

    def test_regex_fail_list(self):
        for i in self.postcode_fail_list:
            self.assertIsNone(part1.regexmatch(str(i)), "fail list")

    def test_regex_pass_list(self):
        for j in self.postcode_pass_list:
            self.assertIsNot(part1.regexmatch(str(j)),"None")

class FunctionTest(unittest.TestCase):
    def test_sorting_records_and_archive_extraction(self):
        result=part3.open_archive("import_data.csv.gz")
        first_in_sorted_list=result[0]
        test_first=['1']
        self.assertTrue(first_in_sorted_list,test_first)
        last_in_sorted_list=result[-1]
        test_last=len(result)
        self.assertTrue(last_in_sorted_list,test_last)

if __name__ == '__main__':
    unittest.main(verbosity=2)
