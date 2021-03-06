import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """edge case for when list is none"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_2(self):
        """general case"""
        int_list = [0,3,4,6,7]
        self.assertEqual(max_list_iter(int_list),7)

    def test_max_list_3(self):
        """general"""
        int_list = [3,5,2,4,6]
        self.assertEqual(max_list_iter(int_list),6)
   
    def test_max_list_4(self):
        """general"""
        int_list = [3,3,4,5,5]
        self.assertEqual(max_list_iter(int_list),5)

    def test_max_list_empty(self):
        """empty list edge case"""
        int_list = []
        self.assertEqual(max_list_iter(int_list),None)

    def test_max_list_zeros(self):
        """only 1 list value"""
        int_list = [1]
        self.assertEqual(max_list_iter(int_list),1)

#start of test reverse_rec
    #these are all general cases
    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_1(self):
        self.assertEqual(reverse_rec([1]),[1])

    def test_reverse_2(self):
        self.assertEqual(reverse_rec([0,1,2,3,1]),[1,3,2,1,0])

    def test_reverse_none(self):
        """this one is an edge case"""
        int_list=None
        with self.assertRaises(ValueError):
           reverse_rec(int_list)

#start of test_bin_search
    def test_bin_search(self):
        """general case for middle"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_none(self):
        """edge case for when list is None"""
        list_val=target=low=high=None
        with self.assertRaises(ValueError):
           bin_search(target,low,high,list_val)

    def test_bin_not_found(self):
        """target not found"""
        list_val = [0,3,5,7,8,10]
        low = 0
        high = 10
        target = 11
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)

    def test_bin_left(self):
        """general case for higher # """
        list_val = [1,2,3,4,5,6,7,8]
        low=1
        high= len(list_val)-1
        target=7
        self.assertEqual(bin_search(7, 1, len(list_val)-1, list_val), 7)

    def test_bin_right(self):
        """general case for lower #"""
        list_val=[0,1,2,3,4,5,6]
        low=0
        high= len(list_val)-1
        target=1
        self.assertEqual(bin_search(1,0,len(list_val)-1, list_val),1) 

if __name__ == "__main__":
        unittest.main()

    
