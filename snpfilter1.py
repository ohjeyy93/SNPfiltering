from nest.summarize import Summary
import argparse

parser = argparse.ArgumentParser(description='name')
parser.add_argument('-r', dest='ref', type=str, help="name of reference file")
parser.add_argument('-b', dest='bed', type=str, help="name of bed file")
parser.add_argument('-v', dest='voi', type=str, help="name of voi file")
parser.add_argument('-o', dest='out', type=str, help="name output direcotry")
args = parser.parse_args()

summary = Summary(args.ref, args.bed, args.voi, args.out)
#summary = Summary("ref/pfalciparum/mdr.fa", "ref/pfalciparum/mdr.bed", "ref/pfalciparum/Reportable_SNPs.csv", "test1")
#var_sum = summary.getVarStats("/mnt/c/Users/momo/Desktop/CDC/local/Mars_test6genes2/spread/SRR6463548/fixedPOSfinal_SRR6463548_filtered.vcfext.vcf")
#main_logger.info('Total variants : {0}; Verified calls : {1}; Exonic : {2}; Intronic : {3}; Synonymous : {4}; Non Synonymous : {5}; Transition : {6}; Transversion : {7}'.format(
#                        var_sum[0], var_sum[1], var_sum[2], var_sum[3], var_sum[4], var_sum[5], var_sum[6], var_sum[7]))
summary.getSummary()
#print(var_sum)
#f1 = open("something1.txt", "w")
#f1.write(var_sum[0], var_sum[1], var_sum[2], var_sum[3], var_sum[4], var_sum[5], var_sum[6], var_sum[7])
#f1.close