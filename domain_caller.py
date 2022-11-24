list_genes = open ("gene.list")
list_genes = list_genes.read()
list_genes = list_genes.split("\n")
ips = open ("ips_temp_short.tsv")
ips = ips.read()
ips = ips.replace("Leucine rich repeat 4", "IPS_LRR")
ips = ips.replace("Leucine-rich repeat 2", "IPS_LRR")
ips = ips.replace("Leucine-rich repeat 3", "IPS_LRR")
ips = ips.replace("Leucine-rich repeat domain superfamily", "IPS_LRR")
ips = ips.replace("Leucine-rich repeat-containing N-terminal, plant type", "IPS_LRR")
ips = ips.replace("Leucine-rich repeat", "IPS_LRR")
ips = ips.replace("Coil", "IPS_CC")
ips = ips.replace("Toll/interleukin-1 receptor homology (TIR) domain superfamily", "IPS_TIR")
ips = ips.replace("Toll/interleukin-1 receptor homology (TIR) domain", "IPS_TIR")
ips = ips.replace("NB-ARC domain", "IPS_NBARC")
ips = ips.replace("Powdery mildew resistance protein, RPW8 domain", "IPS_RPW8")
ips = ips.split()
no_genes = len(list_genes) - 1
n="\n"
t="\t"
m=0
while m < no_genes:
    gene_name=list_genes[m]
    gene_pos_start = ips.index(gene_name)
    gene_pos_end = len(ips) - 1 - ips[::-1].index(gene_name) + 4
    ips_for_gene = ips[gene_pos_start:gene_pos_end]
    if "IPS_LRR" or "IPS_CC" or "IPS_TIR" or "IPS_NBARC" or "IPS_RPW8" in ips_for_gene:
        if "IPS_CC" in ips_for_gene:
            IPS_CC_pos = ips_for_gene.index("IPS_CC")
            IPS_CC_start = ips_for_gene[IPS_CC_pos + 1]
            IPS_CC_end = ips_for_gene[IPS_CC_pos + 2]
            output=open("domains.txt", "a")
            output.write (gene_name + t + "CC" + t + IPS_CC_start + t + IPS_CC_end + n)
        else:
             pass
        
        if "IPS_TIR" in ips_for_gene:
            IPS_TIR_pos = len(ips_for_gene) - 1 - ips_for_gene[::-1].index("IPS_TIR")
            IPS_TIR_start = ips_for_gene[IPS_TIR_pos - 2]
            IPS_TIR_end = ips_for_gene[IPS_TIR_pos - 1]
            output=open("domains.txt", "a")
            output.write (gene_name + t + "TIR" + t + IPS_TIR_start + t + IPS_TIR_end + n)
        else:
             pass
        if "IPS_RPW8" in ips_for_gene:
            IPS_RPW8_pos = len(ips_for_gene) - 1 - ips_for_gene[::-1].index("IPS_RPW8")
            IPS_RPW8_start = ips_for_gene[IPS_RPW8_pos - 2]
            IPS_RPW8_end = ips_for_gene[IPS_RPW8_pos - 1]
            output=open("domains.txt", "a")
            output.write (gene_name + t + "RPW8" + t + IPS_RPW8_start + t + IPS_RPW8_end + n)
        else:
             pass
        if "IPS_NBARC" in ips_for_gene:
            IPS_NBARC_pos = ips_for_gene.index("IPS_NBARC")
            IPS_NBARC_start = ips_for_gene[IPS_NBARC_pos + 1]
            IPS_NBARC_end = ips_for_gene[IPS_NBARC_pos + 2]
            output=open("domains.txt", "a")   
            output.write (gene_name + t + "NBARC" + t + IPS_NBARC_start + t + IPS_NBARC_end + n)
        else:
            pass
        if "IPS_LRR" in ips_for_gene:
            IPS_LRR_pos = len(ips_for_gene) - 1 - ips_for_gene[::-1].index("IPS_LRR")
            IPS_LRR_start = ips_for_gene[IPS_LRR_pos - 2]
            IPS_LRR_end = ips_for_gene[IPS_LRR_pos - 1]
            output=open("domains.txt", "a")
            output.write (gene_name + t + "LRR" + t + IPS_LRR_start + t + IPS_LRR_end + n)
        else:
            pass            
    else:
        pass
    m=m+1
output.close()

