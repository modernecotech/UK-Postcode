import re, sys, gzip, csv

def archive_name(*args):
    arch_file = str(sys.argv[1])
    print(arch_file)
    return arch_file

def open_archive(arch_file):
    with gzip.open(arch_file,mode='rt') as f:
        print(f)
        file_content = csv.reader(f,delimiter=',')
        with open("failed_validation.csv", "w",newline='') as output_file:
            output_writer = csv.writer(output_file, delimiter=',')
            for row in file_content:
                if regex_filter(str(row[1]))==None:
                    output_writer.writerow(row)
                
        
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
