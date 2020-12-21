from nest.summarize import Summary
import argparse

parser = argparse.ArgumentParser(description='name')
parser.add_argument('-a', dest='AAcid', type=str, help="AA")
args = parser.parse_args()

#AAdic= {"A":"Ala", "R":"Arg", "N": "Asn", "D": "Asp", "B":"Asx", "C": "Cys", "E":"Glu", "Q":"Gln", "Z":"Glx", "G":"Gly", "H":"His", "I":"Ile", "L":"Leu", "K":"Lys", "M":"Met", "F":"Phe", "P":"Pro", "S":"Ser", "T":"Thr", "W":"Trp", "Y":"Tyr", "V":"Val"}
AAdic= {"Ala":"A", "Arg":"R", "Asn":"N", "Asp":"D", "Asx":"B", "Cys":"C", "Glu":"E", "Gln":"Q", "Glx":"Z", "Gly":"G", "His":"H", "Ile":"I", "Leu":"L", "Lys":"K", "Met":"M", "Phe":"F", "Pro":"P", "Ser":"S", "Thr":"T", "Trp":"W", "Tyr":"Y", "Val":"V"}

if args.AAcid in AAdic:
    print(AAdic[args.AAcid])