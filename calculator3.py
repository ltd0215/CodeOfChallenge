#!/usr/bin/env python3

import sys
import csv


class Args(object):

	def __init__(self):
		self.args = sys.argv[1:]

	# buchong


class Config(object):

	def __init__(self):
		self.config = self._read_config()

	def _read_config(self):
		config = {}
	# buchong


class UserData(object):

	def __init__(self):
		self.userdata = self._read_users_data()

	def _read_users_data(self):
		userdata = []
	# buchong

class IncomeTaxCalculator(object):

	def calc_for_all_userdata(self):

	#buchong

	def export(self, default='csv'):
		writer = csv.writer(f)
		writer.writerows(result)

if __name__ == '__main__':

	#buchong
