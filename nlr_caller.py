gene_list = open("domains_gene.list")
gene_list = gene_list.read()
gene_list = gene_list.split("\n")
domains = open("domains.txt")
domains = domains.read()
domains = domains.split()
no_genes = len(gene_list) - 1
n="\n"
i=0
while i < no_genes :
    gene = gene_list[i]
    domains_start_pos = domains.index(gene)
    domains_end_pos = len(domains) - 1 - domains[::-1].index(gene) + 3
    domains_per_gene = domains[domains_start_pos:domains_end_pos]
#one_domain
    if "TIR" in domains_per_gene and "NBARC" not in domains_per_gene and "RPW8" not in domains_per_gene and "CC" not in domains_per_gene and "LRR" not in domains_per_gene:
        tir_only_output = open("_TIR_only.txt","a")
        tir_only_output.write(gene + n)
        tir_only_output.close()
    elif "TIR" not in domains_per_gene and "NBARC" not in domains_per_gene and "RPW8" in domains_per_gene and "LRR" not in domains_per_gene:
        rpw8_only_output = open("_RPW8_only.txt","a")
        rpw8_only_output.write(gene + n)
        rpw8_only_output.close()
    elif "TIR" not in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" not in domains_per_gene and "CC" not in domains_per_gene and "LRR" not in domains_per_gene:
        nbarc_only_output = open("_NBARC_only.txt","a")
        nbarc_only_output.write(gene + n)
        nbarc_only_output.close()
#two domains
    #CN
    elif "TIR" not in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" not in domains_per_gene and "CC" in domains_per_gene and "LRR" not in domains_per_gene:
        cc_st = int(domains_per_gene[domains_per_gene.index("CC") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        if nbarc_st > cc_st:
            cn_output = open("_CN.txt","a")
            cn_output.write(gene + n)
            cn_output.close()
        else:
            pass
    #TN
    elif "TIR" in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" not in domains_per_gene and "CC" not in domains_per_gene and "LRR" not in domains_per_gene:
        tir_st = int(domains_per_gene[domains_per_gene.index("TIR") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        if nbarc_st > tir_st:
            tn_output = open("_TN.txt","a")
            tn_output.write(gene + n)
            tn_output.close()
        else:
            pass
    #RN
    elif "TIR" not in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" in domains_per_gene and "LRR" not in domains_per_gene:
        rpw8_st = int(domains_per_gene[domains_per_gene.index("RPW8") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        if nbarc_st > rpw8_st:
            rn_output = open("_RN.txt","a")
            rn_output.write(gene + n)
            rn_output.close()
        else:
            pass
    #NL
    elif "TIR" not in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" not in domains_per_gene and "CC" not in domains_per_gene and "LRR" in domains_per_gene:
        lrr_st = int(domains_per_gene[domains_per_gene.index("LRR") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        if lrr_st > nbarc_st:
            nl_output = open("_NL.txt","a")
            nl_output.write(gene + n)
            nl_output.close()
        else:
            pass
#three domains
    #CNL
    elif "TIR" not in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" not in domains_per_gene and "CC" in domains_per_gene and "LRR" in domains_per_gene:
        lrr_st = int(domains_per_gene[domains_per_gene.index("LRR") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        cc_st = int(domains_per_gene[domains_per_gene.index("CC") + 1])
        if lrr_st > nbarc_st and nbarc_st > cc_st:
            cnl_output = open("_CNL.txt","a")
            cnl_output.write(gene + n)
            cnl_output.close()
        else:
            pass
    #TNL
    elif "TIR" in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" not in domains_per_gene and "CC" not in domains_per_gene and "LRR" in domains_per_gene:
        lrr_st = int(domains_per_gene[domains_per_gene.index("LRR") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        tir_st = int(domains_per_gene[domains_per_gene.index("TIR") + 1])
        if lrr_st > nbarc_st and nbarc_st > tir_st:
            tnl_output = open("_TNL.txt","a")
            tnl_output.write(gene + n)
            tnl_output.close()
        else:
            pass    
    #RNL
    elif "TIR" not in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" in domains_per_gene and "LRR" in domains_per_gene:
        lrr_st = int(domains_per_gene[domains_per_gene.index("LRR") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        rpw8_st = int(domains_per_gene[domains_per_gene.index("RPW8") + 1])
        if lrr_st > nbarc_st and nbarc_st > rpw8_st:
            rnl_output = open("_RNL.txt","a")
            rnl_output.write(gene + n)
            rnl_output.close()
        else:
            pass
#four domains
    #CTNL and TCNL
    elif "TIR" in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" not in domains_per_gene and "LRR" in domains_per_gene and "CC" in domains_per_gene:
        lrr_st = int(domains_per_gene[domains_per_gene.index("LRR") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        tir_st = int(domains_per_gene[domains_per_gene.index("TIR") + 1])
        cc_st = int(domains_per_gene[domains_per_gene.index("CC") + 1])
        if lrr_st > nbarc_st and nbarc_st > tir_st and tir_st > cc_st:
            ctnl_output = open("_CTNL.txt","a")
            ctnl_output.write(gene + n)
            ctnl_output.close()
        elif lrr_st > nbarc_st and nbarc_st > cc_st and cc_st > tir_st:
            tcnl_output = open("_TCNL.txt","a")
            tcnl_output.write(gene + n)
            tcnl_output.close()            
            
        else:
            pass
    #RTNL and TRNL
    elif "TIR" in domains_per_gene and "NBARC" in domains_per_gene and "RPW8" in domains_per_gene and "LRR" in domains_per_gene:
        lrr_st = int(domains_per_gene[domains_per_gene.index("LRR") + 1])
        nbarc_st = int(domains_per_gene[domains_per_gene.index("NBARC") + 1])
        tir_st = int(domains_per_gene[domains_per_gene.index("TIR") + 1])
        rpw8_st = int(domains_per_gene[domains_per_gene.index("RPW8") + 1])
        if lrr_st > nbarc_st and nbarc_st > tir_st and tir_st > rpw8_st:
            rtnl_output = open("_RTNL.txt","a")
            rtnl_output.write(gene + n)
            rtnl_output.close()
        elif lrr_st > nbarc_st and nbarc_st > rpw8_st and rpw8_st > tir_st:
            trnl_output = open("_TRNL.txt","a")
            trnl_output.write(gene + n)
            trnl_output.close()            
        else:
            pass
    else:        
        pass
    i=i+1
    
