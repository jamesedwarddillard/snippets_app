"""
App for storing and retrieving snippets of text
"""

import logging
import csv
import argparse
import sys

#Set the log output file and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name,snippet,filename):
	"""Store a snippet with an associated name in the CSV file"""
	logging.info("Writing {}:{} to {}".format(name,snippet,filename))
	logging.debug("Opening file")
	with open(filename, "a") as f:
		writer = csv.writer(f)
		logging.debug("Writting snippet to file".format(name, snippet))
		writer.writerow([name, snippet])
	logging.debug("Write successful")
	return name, snippet

def make_parser():
	""" Construct the command line parser """
	logging.info("Constructing the parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description=description)

	subparser = parser.add_subparsers(help="Available commands")

	#Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparser.add_parser("put", help="Store a snippet")
	put_parser.add_argument("name", help="The name of a snippet")
	put_parser.add_argument("snippet", help="The snippet of text to be stored")
	put_parser.add_argument("filename", default="snippets.csv", nargs ="?", help="The snippet filename")
	put_parser.set_defaults(command="put")

	return parser

def main():
	""" Main function """
	logging.info("Starting snippets")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])

if __name__ == '__main__':
	main()