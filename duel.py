####################################################################
##duel.py was based off of the duel.rb program from a talk by _why##
####################################################################

import os
import sys
import random
import time

class Fighters(object):
	def __init__(self):
		self.text = """
  ~O    O~
  <|\@-@\/|>
   |    |
  $/ \  / $\\
"""
		self.text= self.text[1:-1]
		self.insults = ["You smell of elderberries!",
				"I've fought mudcrabs fiercer than you!",
				"Prepare to die, knave!",
				"My swords shills are highly ventilated!",
				"Dance I say, dance!",
				"Engarde!",
				"I will defeat you! Believe it!",
				"Your fly is undone!",
				"Die you dubius donut!",
				"You are an unsightly strumpet!",
				"You can not best me!",
				"You've met your match!"]
		self.insult_count = 0
		self.cur_insult = random.choice(self.insults)
		self.text_spacer = ""
		self.insulter = True
	def move(self, increment):
		new_text = []
		if increment > 0:
			self.text_spacer += " " * increment
		else:
			self.text_spacer = self.text_spacer[:increment]
		for line in self.text.split("\n"):
			if increment > 0:line = (" " * increment) + line
			elif increment < 0: line = line[abs(increment):]
			else: return -1
			new_text.append(line)
		new_text = "\n".join(new_text)
		self.text = new_text
	def parry(self):
		marker1 = self.text.index("@")
		value1 = self.text[marker1 + 1]
		marker2 = self.text[marker1 + 1:].index("@") + len(self.text[:marker1 + 1])
		value2 = self.text[marker2 + 1]
		new_text = list(self.text)
		if value1 == r"/":
			new_text[marker1 + 1] = r"|"
		elif value1 == r"|":
			new_text[marker1 + 1] = r"-"
		else:
			new_text[marker1 + 1] = r"/"
		if value2 == "\\":
			new_text[marker2 + 1] = r"|"
		elif value2 == r"|":
			new_text[marker2 + 1] = r"-"
		else:
			new_text[marker2 + 1] = "\\"
		
		self.text = "".join(new_text)		

		marker1 = self.text.index("$")
		value1 = self.text[marker1 + 1]
		marker2 = self.text[marker1 + 1:].index("$")  + len(self.text[:marker1 + 1])
		value2 = self.text[marker2 + 1]
		new_text = list(self.text)
		if value1 == r"/":
			new_text[marker1 + 1] = r"|"
		else:
			new_text[marker1 + 1] = r"/"
		if value2 == "\\":
			new_text[marker2 + 1] = r"|"
		else:
			new_text[marker2 + 1] = "\\"
			

		self.text = "".join(new_text)
		
	def draw(self):
		if sys.platform[:3] == "win":
			os.system("cls")
		else:
			os.system("clear")
		if self.insult_count > 15:
			self.cur_insult = random.choice(self.insults)
			self.insulter = not self.insulter
			self.insult_count = 0
		self.insult_count += 1
		print self.text_spacer + self.cur_insult
		if self.insulter == True:
			print self.text_spacer + "    /"
		else:
			print self.text_spacer + "       \\"
		draw_text = list(self.text)
		for i in range(2):
			draw_text.remove("@")
			draw_text.remove("$")
		draw_text = reduce(lambda a, b: a + b, draw_text)
		for line in draw_text.split("\n"):
			print line

if __name__ == "__main__":
	fighters = Fighters()
	move_flag = True
	move_count = False
	while True:
		time.sleep(0.1)
		fighters.draw()
		fighters.parry()
		if move_count > 35:
			move_count = 0
			move_flag = not move_flag
		if move_flag:
			fighters.move(1)
		else:
			fighters.move(-1)
		move_count += 1


	
