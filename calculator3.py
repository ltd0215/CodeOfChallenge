#!/usr/bin/env python3

import sys
import csv


class Args(object):

	def __init__(self):
		self.args = sys.argv[1:]
		self.indexc = self.args.index('-c')
		self.indexd = self.args.index('-d')
		self.indexo = self.args.index('-o')
		self.configpath = self.args[self.indexc+1]
		self.userpath = self.args[self.indexd+1]
		self.gongzipath = self.args[self.indexo+1]

class Config(object):

	def __init__(self):
		self.config = self._read_config()

	def _read_config(self):
		config = {}
		with open(challenge3.configpath, 'r') as configfile:
			for lines in configfile:
				self.a = configfile.readline()
				self.a0 = self.a.split('=')[0].strip()
				self.a1 = self.a.split('=')[1].strip()
				config[self.a0] = self.a1

		return config
class UserData(object):

	def __init__(self):
		self.userdata = self._read_users_data()

	def _read_users_data(self):
		userdata = {}
		with open(challenge3.userpath, 'r') as userdatafile:
			for lines in userdatafile:
				self.a = userdatafile.readline()
				self.a0 = self.a.split(',')[0].strip()
				self.a1 = self.a.split(',')[1].strip()
				userdata[self.a0] = self.a1
		return userdata
class IncomeTaxCalculator(object):
	def  __init__(self):
		self.rate = 0
		for key in Config.config.keys():
			if key == 'JiShuL' or key == 'JiShuH':
				self.rate = self.rate
			else:
				self.rate += float(Config.config[key])
		tax = {}
		with open(challenge3.userpath, 'r') as userfile:
			for line in userfile:
				a = userfile.readline()
				a0 = a.split(',')[0].strip()
				a1 = float(a.split(',')[1].strip())
				Ying = a1 - self.rate * a1 - 3500
				if Ying <= 1500:
					tax[a0] = (a1 - self.rate * a1 - 3500) * 0.03 - 0
				elif Ying > 1500 and a1 <= 4500:
					tax[a0] = (a1 - self.rate * a1 - 3500) * 0.10 - 105
				elif Ying > 4500 and a1 <= 9000:
					tax[a0] = (a1 - self.rate * a1 - 3500) * 0.20 - 555
				elif Ying > 9000 and a1 <= 35000:
					tax[a0] = (a1 - self.rate * a1 - 3500) * 0.25 - 1005
				elif Ying > 35000 and a1 <= 55000:
					tax[a0] = (a1 - self.rate * a1 - 3500) * 0.30 - 2755
				elif Ying > 55000 and a1 <= 80000:
					tax[a0] = (a1 - self.rate * a1 - 3500) * 0.35 - 5505
				else:
					tax[a0] = (a1 - self.rate * a1 - 3500) * 0.45 - 13505
				if tax[a0] < 0:
					tax[a0] = 0
		self.tax = tax

		shebao = {}
		gongzi = {}
		with open(challenge3.userpath, 'r') as userfile:
			for line in userfile:
				a = userfile.readline()
				a0 = a.split(',')[0].strip()
				a1 = float(a.split(',')[1].strip())
				shebao[a0] = a1 * self.rate
				gongzi[a0] = a1 - self.tax[a0] - shebao[a0]

		self.shebao = shebao
		self.gongzi = gongzi

		result = []
		with open(challenge3.userpath, 'r') as userfile:
			for line in userfile:
				a = userfile.readline()
				a0 = a.split(',')[0].strip()
				a1 = float(a.split(',')[1].strip())
				usernum = a0
				presalary = format(a1, ".2f")
				baojin = format(self.shebao[usernum], ".2f")
				shui = format(self.tax[usernum], ".2f")
				aftersalary = format(self.gongzi[usernum], ".2f")
				result.append([usernum,presalary,baojin,shui,aftersalary])
		self.result = result
		# return self.result
	def export(self, default='csv'):
		result = self.result
		with open(challenge3.gongzipath, 'w') as f:
			writer = csv.writer(f)
			writer.writerows(result)

		
if __name__ == '__main__':

	challenge3 = Args()
	Config = Config()
	UserData = UserData()
	IncomeTaxCalculator = IncomeTaxCalculator()
	print(Config.config)
	print(UserData.userdata)
	# print(IncomeTaxCalculator.rate)
	print(Config.config.keys())	#gonghao 1 2
	print(IncomeTaxCalculator.tax)	#shui 4
	print(IncomeTaxCalculator.shebao)	#shebao 3
	print(IncomeTaxCalculator.gongzi)
	print(IncomeTaxCalculator.result)
	IncomeTaxCalculator.export()

