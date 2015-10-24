#! /usr/bin/env python

import re
import sys
import argparse

from .transliterator import transliterator

__name__       = "Hindi-Urdu-Transliterator"
__doc__        = "Hindi to Urdu transliterator and vice-versa"
__author__     = ["Riyaz Ahmad", "Irshad Ahmad"]
__version__    = "0.1"
__license__    = "MIT"
__maintainer__ = "Irshad Ahmad"
__email__      = "irshad.bhat@research.iiit.ac.in"
__status__     = "Beta"
__all__        = ["transliterator", "ssf_reader", "parab2dev", "dev2parab", "main"]

def main():
    format_list = ["text", "ssf", "conll", "bio","tnt"]
    format_help  = "select output format [text|ssf|conll|bio|tnt]"
    ssf_help = "specify ssf-type [inter|intra] in case file format (--f) is ssf"
    # parse command line arguments 
    parser = argparse.ArgumentParser(prog="hutrans", description="Hindi-to-Urdu and Urdu-to-Hindi Transliterator")
    parser.add_argument('--v', action="version", version="%(prog)s 0.1")
    parser.add_argument('--s', metavar='source', dest="source", choices=["hindi","urdu"], default="hindi", help="source script [hindi|urdu]")
    parser.add_argument('--i', metavar='input', dest="INFILE", type=argparse.FileType('r'), default=sys.stdin, help="<input-file>")
    parser.add_argument('--f', metavar='format', dest="format_", choices=format_list, default="text", help="%s" %format_help)
    parser.add_argument('--t', metavar='ssf-type', dest="ssf_type", choices=["inter","intra"], default=None, help=ssf_help)
    parser.add_argument('--o', metavar='output', dest="OUTFILE", type=argparse.FileType('w'), default=sys.stdout, help="<output-file>")

    args = parser.parse_args()
    if args.format_ == 'ssf' and not args.ssf_type:
        sys.stderr.write(parser.format_usage())
        sys.stderr.write("hutrans: error: argument --t: not specified\n")
        sys.exit(0)

    # initialize transliterator object
    trn = transliterator(args.format_, args.source, args.ssf_type)
            
    # transliterate text
    if args.format_ == "ssf":
        sentences = re.finditer("(<Sentence id=.*?>)(.*?)</Sentence>", args.INFILE.read(), re.S)
        sentences = ((g.group(1), g.group(2)) for g in sentences)
        for sid, sentence in sentences:
            sentence = sentence.strip()
            args.OUTFILE.write('%s\n' %sid)
            consen = trn.convert(sentence)
            args.OUTFILE.write('%s' %consen)
            args.OUTFILE.write("</Sentence>\n\n")
    else:
        for line in args.INFILE:
            tline = trn.convert(line)
	    if args.format_ == "text":
		args.OUTFILE.write("%s\n" %(tline))
	    else:
		args.OUTFILE.write(tline)
    
    # close files 
    args.INFILE.close()
    args.OUTFILE.close()
