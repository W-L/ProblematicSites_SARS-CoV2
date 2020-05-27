from pytablewriter import MarkdownTableWriter

def readCustomVCF(fname, keep_cols):
    data = []
    with open(fname, 'r') as vcf:
        for line in vcf:
            # skip the header specification part
            if line.startswith('##'):
                continue
            # get the header line but only keep the ones for the md table
            elif line.startswith('#C'):
                header_line = line.rstrip('\n').split('\t')
                header = [header_line[i] for i in keep_cols]
            # all other lines that contain data
            elif len(line) != 0:
                data_line = line.rstrip('\n').split(sep='\t')
                # but skip the ones of the sequence ends
                if "seq_end" not in data_line:
                    data.append([data_line[i] for i in keep_cols])
            else:
                break

    return header, data

def main():
    writer = MarkdownTableWriter()

    # name of the vcf file to parse and which columns to select from the file
    filename = "problematic_sites_sarsCov2.vcf"
    keep = [1, 3, 4, 8, 10, 11, 12, 13]
    # title of the table - printed as markdown header before the table
    writer.table_name = "Human-friendly version of the vcf file"

    header, data = readCustomVCF(fname=filename, keep_cols=keep)
    # the markdown table does not need a single line for every site at the ends of the sequence
    # so insert the beginning and append the ends
    data.insert(0, ["1-55", ".", ".", "seq_end",".", "."])
    data.append(["29804-29903", ".", ".", "seq_end",".", "."])

    writer.headers = header
    writer.value_matrix = data

    writer.write_table()

if __name__ == "__main__":
    main()
