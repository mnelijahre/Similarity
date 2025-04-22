from alignment import Alignment
from sys import argv
def read_fasta(input_stream):
    id_ = ""
    seq = ""
    seq_count = 0

    for line in input_stream:
        line = line.strip()
        if line.startswith('>'):  # ID
            if seq_count > 1:
                print("Ignoring extra sequence:", line)
            else:
                id_ = line[1:]
            seq_count += 1
        elif line and seq_count <= 1:
            seq += line

    return id_, seq


if __name__ == "__main__2":
    align = Alignment()
    align.initialize("AGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACG", "GAGAATAAACTAGTATTCTTCTGGTCCCCACAGACTCAGAGAGAACCCGCCACCATGTTCGTGTTCCTGGTGCTGCTGCC")
    print("===")
    print(align.distance())


if __name__ == "__main__":
    align = Alignment()
    
    #filename1, filename2 = "uk-variant", "SA-variant"
    filename1 = argv[1]
    filename2 = argv[2]
    if len(argv)>3 :
        max_length = int(argv[3])
    else:
        max_length = 300000
    try:
        with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
            id1, seq1 = read_fasta(file1)
            id2, seq2 = read_fasta(file2)
    except FileNotFoundError:
        print("Error: Could not open FASTA file.")
        exit(1)

    align.initialize(seq1[:max_length], seq2[:max_length])
    print("\n    FILE 1:", filename1)
    print("SEQUENCE 1:", id1)
    print("            length=", min(max_length,len(seq1)), "bases\n")
    print("    FILE 2:", filename2)
    print("SEQUENCE 2:", id2)
    print("            length=", min(max_length,len(seq2)), "bases\n")
    print(" ALIGNMENT:", align.distance())
