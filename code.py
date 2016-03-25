#credit http://unix.stackexchange.com/questions/39039/get-text-file-word-occurrence-count-of-all-words-print-output-sorted
import os
import sys

def word_count(filename):
	"""
	Using Unix Command line, count the word occurence in filename and display only top 10 values.

	@param filename: valid full path directory of the file.
	"""

	#filename = "/Users/kieykouch/Desktop/william2.txt"

	command = "cat "+filename+" | tr [:space:] '\\n' |" +' grep -v "^\s*$" | sort | uniq -c | sort -bnr | head -10'
	#this command seperated into:
	# cat: read the file
	# tr: stripe newline and space
	# grep: stripe emptyline
	# sort: sort
	# uniq -c: count occurences
	# sort -bnr: sort in numberic reverse order
	os.system(command)


if __name__ == '__main__' and len(sys.argv) == 2:
	print ("Reading file "+ str(sys.argv[1]))
	word_count(sys.argv[1])
	
