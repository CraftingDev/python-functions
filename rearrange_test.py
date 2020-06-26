#!/usr/bin/env python

from rearrange import rearrange_name
from rearrange import find_email

import unittest
import sys
import csv


class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange_name(testcase), expected)

	def test_double_name(self):
		testcase = "Hopper, Crace M."
		expected = "Crace M. Hopper"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_one_name(self):
		testcase = "Voltaire"
		expected = "Voltaire"
		self.assertEqual(rearrange_name(testcase), expected)


unittest.main()


class EmailsTest(unittest.TestCase):
	def test_basic(self):
		testcase = [None, "Bree", "Campbell"]
		expected = "breee@abc.edu"
		self.assertEqual(find_email(testcase), expected)

	def test_one_name(self):
		testcase = [None, "John"]
		expected = "Missing parameters"
		self.assertEqual(find_email(testcase), expected)

	def test_two_name(self):
		testcase = [None, "Roy", "Cooper"]
		expected = "No email address found"
		self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
	unittest.main()
