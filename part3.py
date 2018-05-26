import re, sys, gzip, csv

def archive_name(*args):
    arch_file = str(sys.argv[1])
    print(arch_file)
    return arch_file

def open_archive(arch_file):
    with gzip.open(arch_file,mode='rt') as f:
        file_content = csv.reader(f,delimiter=',')
        file_sorted=[]
        next(file_content)
        for row in sorted((i for i in file_content),key=lambda x:int(x[0])):
            file_sorted.append(row)
        return file_sorted

def filter_archive(file_sorted):
    with open("failed_validation.csv", "w",newline='') as f_output_file:
        f_output_writer = csv.writer(f_output_file, delimiter=',')
        with open("suceeded_validation.csv","w",newline='') as s_output_file:
            s_output_writer=csv.writer(s_output_file, delimiter=',')
            for row in file_sorted:
                if regex_filter(str(row[1]))==None:
                    f_output_writer.writerow(row)
                else:
                    s_output_writer.writerow(row)

def regex_filter(row):
    result = re.fullmatch((r'(GIR\s0AA)|'\
           r'((([A-PR-UWYZ][0-9][0-9]?)|'\
           r'(([A-PR-UWYZ][A-HK-Y]'\
           r'(?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)))[0-9][0-9])|'\
	   r'([A-PR-UWYZ][A-HK-Y](?<!(AB|LL|SO))[0-9])|'\
	   r'(WC[0-9][A-Z])|'\
	   r'(([A-PR-UWYZ][0-9][A-HJKPSTUW])|'\
	   r'([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])))'\
	   r'\s[0-9][ABD-HJLNP-UW-Z]{2})'),row)
    return(result)

if __name__ == "__main__":
    open_archive(archive_name(sys.argv))



'''
def regex_filter(row):
    result =re.fullmatch((r'((GIR 0AA)|' \
           r'(((A[BL]|B[ABDFHLNRSTX]?|' \
              r'C[ABFHMORTVW]|D[ADEGHLNTY]|' \
              r'E[HNX]?|F[KY]|G[LUY]?|H[ADGPRSUX]|' \
              r'I[GMPV]|JE|K[ATWY]|L[ADELNSU]?|' \
              r'M[EKL]?|N[EGNPRW]?|O[LX]|' \
              r'P[AEHLOR]|R[GHM]|S[AEGKLMNOPRSTY]?|' \
              r'T[ADFNQRSW]|UB|W[ADFNRSV]|YO|ZE)[1-9]?[0-9]|' \
             r'((E|N|NW|SE|SW|W)1|EC[1-4]|WC[12])[A-HJKMNPR-Y]|' \
             r'(SW|W)([2-9]|[1-9][0-9])|' \
             r'EC[1-9][0-9]) [0-9][ABD-HJLNP-UW-Z]{2}))'),row)
'''
