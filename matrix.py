import time
import sys

HELP = """
    ls            list files in the current folder
    ls <folder>   list files in the given folder
    cd <folder>   change into given folder
    cd ..         leave the current folder
    rm <file>
"""
def message(msg):
    msg = msg + "\n"
    for char in msg:
        sys.stdout.write('%s' % char)
        sys.stdout.flush()
        time.sleep(0.2)


def intro():
	with open("intro.txt") as f:
		lines = f.readlines()
		for line in lines:
			message(line)
		print HELP
		raw_input("Press Enter to continue...")

def main():
	intro()

if __name__ == "__main__":
	main()
