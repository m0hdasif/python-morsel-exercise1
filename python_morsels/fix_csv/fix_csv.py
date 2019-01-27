import argparse
import csv

parser = argparse.ArgumentParser(description='Fix a CSV file.')
parser.add_argument('--in-delimiter', dest='delim', help='delimiter in the input file.')
parser.add_argument('--in-quote', dest='quote', help='quote in the input file')
parser.add_argument('in-file', help='file name of the CSV to fix')
parser.add_argument('out-file', help='file to save the fixed CSV')

args = parser.parse_args()

with open(getattr(args, 'in-file'), 'r', newline='') as in_csv:
    read_args = {}
    if args.delim:
        read_args['delimiter'] = args.delim
    if args.quote:
        read_args['quotechar'] = args.quote
    if not args.delim and not args.quote:
        read_args['dialect'] = csv.Sniffer().sniff(in_csv.read())
        in_csv.seek(0)
    reader = csv.reader(in_csv, **read_args)
    with open(getattr(args, 'out-file'), 'w', newline='') as out_csv:
        csv.writer(out_csv).writerows(reader)
