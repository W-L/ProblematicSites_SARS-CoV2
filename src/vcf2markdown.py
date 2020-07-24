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
                header += ["EXC", "GENE", "AA_POS", "AA_REF", "AA_ALT"]
            # all other lines that contain data
            elif len(line) != 0:
                data_line = line.rstrip('\n').split(sep='\t')
                new_data_line = [data_line[i] for i in keep_cols]
                # but skip the ones of the sequence ends
                if data_line[-1].split(";")[1].split("=")[1] != "seq_end":
                    new_data_line.append("<br>".join(data_line[-1].split(";")[1].split("=")[1].split(",")))
                    new_data_line.append(data_line[-1].split(";")[-4].split("=")[1])
                    new_data_line.append(data_line[-1].split(";")[-3].split("=")[1])
                    new_data_line.append(data_line[-1].split(";")[-2].split("=")[1])
                    new_data_line.append(data_line[-1].split(";")[-1].split("=")[1])
                    data.append(new_data_line)
                    #data.append([data_line[i] for i in range(len(header)-1)])
            else:
                break

    return header, data

def main():
    writer = MarkdownTableWriter()

    # name of the vcf file to parse and which columns to select from the file
    filename = "problematic_sites_sarsCov2.vcf"
    keep = [1, 3, 4, 6]
    # title of the table - printed as markdown header before the table
    writer.table_name = "Human-friendly version of the vcf file"

    header, data = readCustomVCF(fname=filename, keep_cols=keep)
    # the markdown table does not need a single line for every site at the ends of the sequence
    # so insert the beginning and append the ends
    data.insert(0, ["1-55", ".", ".", "mask","seq_end",".", ".",".","."])
    data.append(["29804-29903", ".", ".", "mask","seq_end",".",".",".","."])

    writer.headers = header
    writer.value_matrix = data

    writer.write_table()

if __name__ == "__main__":
    main()
