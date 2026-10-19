

import os
from contextlib import redirect_stdout
# Dictonary containing the base pairs and their corresponding amino acids for DNA coding strand
Amino_acids_DNA = {
     "TTT": "Phe",
     "TTC": "Phe",
     "TTA": "Leu",
     "TTG": "Leu",
     "CTT": "Leu",
     "CTC": "Leu",
     "CTA": "Leu",
     "CTG": "Leu",
     "ATT": "Ile",
     "ATC": "Ile",
     "ATA": "Ile",
     "ATG": "Met",
     "GTT": "Val",
     "GTC": "Val",
     "GTA": "Val",
     "GTG": "Val",
     "TCT": "Ser",
     "TCC": "Ser",
     "TCA": "Ser",
     "TCG": "Ser",
     "CCT": "Pro",
     "CCC": "Pro",
     "CCA": "Pro",
     "CCG": "Pro",
     "ACT": "Thr",
     "ACC": "Thr",
     "ACA": "Thr",
     "ACG": "Thr",
     "GCT": "Ala",
     "GCC": "Ala",
     "GCA": "Ala",
     "GCG": "Ala",
     "TAT": "Tyr",
     "TAC": "Tyr",
     "TAA": "STOP",
     "TAG": "STOP",
     "CAT": "His",
     "CAC": "His",
     "CAA": "Gln",
     "CAG": "Gln",
     "AAT": "Asn",
     "AAC": "Asn",
     "AAA": "Lys",
     "AAG": "Lys",
     "GAT": "Asp",
     "GAC": "Asp",
     "GAA": "Glu",
     "GAG": "Glu",
     "TGT": "Cys",
     "TGC": "Cys",
     "TGA": "STOP",
     "TGG": "Trp",
     "CGT": "Arg",
     "CGC": "Arg",
     "CGA": "Arg",
     "CGG": "Arg",
     "AGT": "Ser",
     "AGC": "Ser",
     "AGA": "Arg",
     "AGG": "Arg",
     "GGT": "Gly",
     "GGC": "Gly",
     "GGA": "Gly",
     "GGG": "Gly"
}


# Dictionary containing the base pairs and their corrosponding amino acids for RNA strand
Amino_acids_RNA = {
    "UUU": "Phe",
    "UUC": "Phe",
    "UUA": "Leu",
    "UUG": "Leu",
    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",
    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",
    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",
    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",
    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",
    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",
    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",
    "UAU": "Tyr",
    "UAC": "Tyr",
    "UAA": "STOP",
    "UAG": "STOP",
    "CAU": "His",
    "CAC": "His",
    "CAA": "Gln",
    "CAG": "Gln",
    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",
    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",
    "UGU": "Cys",
    "UGC": "Cys",
    "UGA": "STOP",
    "UGG": "Trp",
    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",
    "AGU": "Ser",
    "AGC": "Ser",
    "AGA": "Arg",
    "AGG": "Arg",
    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly",
}


# function to read a fasta file and return the sequence as a string with no whitespaces or header lines
def read_fasta_file(filename):
    sequence = ""# define sequence as nothing

    with open(filename, 'r') as file: # open the file in read mode
        
        for line in file:# go through each line in the file
        
            line = line.strip()# remove any whitespace from the file 

            if line.startswith('>'):# if the line starts with a > then it is a header line and should be skipped
                continue  # Skip header lines

            sequence += line# add the line to the sequence

    
    return sequence


# function to ask the user for the minimum length of the genes they would like to have returned
def minimum_length():
    print ("Please enter the minimum length of base pairs in the genes you would like to have returned")
    try:
        min_length = int(input())
    except ValueError:
        print ("ERROR: Please enter a number")
        exit()
    
    if min_length < 3: 
        print ("ERROR: Minimum length must be greater than 2.")
        exit()
        
    else:
        return min_length


# function to ask the user how they would like to search for genes
def get_search_method():
    print ("How would you like to search for genes")
    print ("Please enter 1 to start from every avaliable ATG and the next avaliable stop codon")
    print ("Please enter 2 to start searching for the next ATG after the last stop codon in the last gene found")
    try:
        search_method = int(input())
    except ValueError:
        print ("ERROR: Please enter a number")
        exit()

    if search_method != 1 and search_method != 2:
        print ("ERROR: Please enter 1 or 2")
        exit()
    else:

        return search_method


# function which types out the analysis summary for DNA only
def analysis_summary(genes, DNA_sequence2, searching_method, min_length,):
    if searching_method == 1:
        search = "From every avaliable ATG"
    elif searching_method == 2:
        search = "After stop codon"

    analysis = (
    "\n"
    "===============================\n"
    "ANALYSIS SUMMARY\n"
    "===============================\n"
    "\n"
    f"Genes meeting minimum length: {min_length}, base pairs \n"
    f"Search method:  {search} \n"
    f"Number of genes found: {len(genes)} \n"
    f"Sequence length:  {len(DNA_sequence2)}, base pairs \n"
    "\n"
    "===============================\n"
    )
    return analysis


# function which types out the analysis summary for RNA only
def analysis_summary2(genes, RNA_sequence2, searching_method, min_length,):
    if searching_method == 1:
        search = "From every avaliable ATG"
    elif searching_method == 2:
        search = "After stop codon"

    analysis = (
    "\n"
    "===============================\n"
    "ANALYSIS SUMMARY\n"
    "===============================\n"
    "\n"
    f"Genes meeting minimum length: {min_length}, base pairs"
    f"Search method:  {search} /n"
    f"Number of genes found: {len(genes)} \n"
    f"Sequence length: {len(RNA_sequence2)} base pairs"
    "\n"
    "==============================="
    )
    return analysis
    


# function for the start of the code
def hello_sequence():
    print ("Hello this is a DNA sequence analyser, please specify if you want to analyse a coding strand or an mRNA strand (C/R)")
    coding_or_template = input() 
    coding_or_template_up = coding_or_template.upper()

    if coding_or_template_up == "R":
        pass
    elif coding_or_template_up == "C":
        pass
    else:
        print ("ERROR: Please enter C or R")


    if coding_or_template_up == "C":
        print ("You have chosen to analyse a coding strand") 
        print ("Please indicate if you would like to input a fasta file or the DNA sequence manually (F/M)")
        decision1 = input()
        decision = decision1.upper()
        if decision == "F":
            pass
        elif decision == "M":
            pass
        else: 
            return "ERROR please enter F (fasta file) or M (Manually)"

        if decision == "F": 
            print ("Please enter the fasta file name: ")
            
            
            filename = input()
            min_length = minimum_length()

            searching_method = get_search_method()
            
            

            if not os.path.exists(filename): # checks to see if the file name exists or it will return an error message
                return "ERROR: This file does not exist, please enter the file name exactly as it is saved in the folder"
            
            DNA_sequence_rough = read_fasta_file(filename)
            print ("----------------------------------------------------------------------------")
            general_facts, DNA_sequence2 = analyse_data_C(DNA_sequence_rough)
            genes = find_genes_C(DNA_sequence_rough, min_length, searching_method)
            amino_acid_sequences = convert_sequence_to_amino_acids_C(genes, min_length)
            
            results = general_facts 
            for gene, information in amino_acid_sequences.items():
                results += f"\n{gene}\n"
                results += information
                results += "\n"
            print (" ")
            print ("----------------------------------------------------------------------------")

            results += analysis_summary(
            genes,
            DNA_sequence2,
            searching_method,
            min_length
            )

            return results

        



            


        elif decision == "M":
            print ("Please enter the DNA sequence: ")
            DNA_sequence_rough = input()
            min_length = minimum_length()
            searching_method = get_search_method()
            print ("----------------------------------------------------------------------------")
            general_facts, DNA_sequence2 = analyse_data_C(DNA_sequence_rough)
            genes = find_genes_C(DNA_sequence_rough, min_length, searching_method)
            amino_acid_sequences = convert_sequence_to_amino_acids_C(genes, min_length)

            results = general_facts 
            for gene, information in amino_acid_sequences.items():
                results += f"\n{gene}\n"
                results += information
                results += "\n"
            print (" ")
            print ("----------------------------------------------------------------------------")

            results += analysis_summary(
            genes,
            DNA_sequence2,
            searching_method,
            min_length
            )

            return results

        else:
            return "Please enter F (fasta file) or M (manually)" 

    elif coding_or_template_up == "R":
        print ("you have chosen to analyse an mRNA strand")
        print ("Please indicate if you would like to input a fasta file or the mRNA sequence manually (F/M)")
        decision1 = input()
        decision = decision1.upper()

        if decision == "F":
            pass
        elif decision == "M":
            pass
        else:
            return "ERROR please enter F (fasta file) or M (Manually)"


        if decision == "F":
            print ("Please enter the fasta file name: ")
            
            filename = input()
            min_length = minimum_length()
            searching_method = get_search_method()
            if not os.path.exists(filename):
                return "ERROR: This file does not exist, please enter the file name exactly as it is saved in the folder"
            
            RNA_sequence_rough = read_fasta_file(filename) 
            print ("----------------------------------------------------------------------------")
            general_facts, RNA_sequence2 = analyse_data_R(RNA_sequence_rough)
            genes = find_genes_R(RNA_sequence_rough, min_length, searching_method)
            amino_acid_sequences = convert_sequence_to_amino_acids_R(genes, min_length, searching_method)

            results = general_facts 
            for gene, information in amino_acid_sequences.items():
                results += f"\n{gene}\n"
                results += information
                results += "\n"
            print (" ")
            print ("----------------------------------------------------------------------------")

            results += analysis_summary(
            genes,
            RNA_sequence2,
            searching_method,
            min_length
            )

            return results
            

        elif decision == "M":
            print ("Please enter the mRNA sequence: ")

            
            
            RNA_sequence_rough = input()
            min_length = minimum_length()
            searching_method = get_search_method()
            print ("----------------------------------------------------------------------------")
            general_facts, RNA_sequence2 = analyse_data_R(RNA_sequence_rough)
            genes = find_genes_R(RNA_sequence_rough, min_length, searching_method)
            amino_acid_sequences = convert_sequence_to_amino_acids_R(genes, min_length)

            for gene, information in amino_acid_sequences.items():
                print(gene)
                print(information)
                print()
            print (" ")
            print ("----------------------------------------------------------------------------")
            analysis = analysis_summary2(genes, RNA_sequence2, searching_method, min_length)
           


        else:
            return "Please enter F (fasta file) or M (manually)"

    return 


#  sequence length + % composition + check bases are all correct
def analyse_data_C(DNA_sequence_rough):
    ###########################################
    #inputs, sorting and checking the DNA sequence

    #print("Enter the DNA sequence")
    #DNA_sequence_rough = input()
    DNA_sequence1 = DNA_sequence_rough.upper() # convert DNA sequence to upper case
    DNA_sequence = DNA_sequence1.replace(" ", "") # remove any whitespace from the sequence
    DNA_sequence2 = DNA_sequence1
    if all(base in "ATCG" for base in DNA_sequence): # check to make sure that all of the bases in the sequence are only A T G and C
        pass
    else:
        return print("ERROR: DNA sequence must only contain the bases T, G, C, A")

    
    ############################################
    #general facts about DNA sequence

    DNA_sequence_length = len(DNA_sequence) # find length of DNA sequence

    num_of_A_and_T = DNA_sequence.count("A") + DNA_sequence.count("T")  # find % of A and T 
    percentage_of_A_and_T = (num_of_A_and_T / len(DNA_sequence)) * 100

    num_of_C_and_G = DNA_sequence.count("C") + DNA_sequence.count("G")  # find % of C and G
    percentage_of_C_and_G = (num_of_C_and_G / len(DNA_sequence)) * 100

    # printing part
    general_facts = (
    "\n "
    "-----------------------------------"
    "\n "
    "General facts: "
    " \n"
    f"Length of DNA sequence: {DNA_sequence_length} base pairs \n"
    f"Percentage of Adenine and Thymine in DNA strand: {round(percentage_of_A_and_T, 2)} % \n"
    f"Percentage of Cytosine and Guanine in DNA strand: {round(percentage_of_C_and_G, 2)} % \n"
    "\n "
    "-----------------------------------"
    "\n "
    )
    return general_facts, DNA_sequence2


# find the genes 
def find_genes_C(DNA_sequence, min_length, searching_method):

    # defining variables which will be used in the function 
    gene_number = 1
    genes = {}
    end_codon = ["TAA", "TAG", "TGA"]
    start_codon = "ATG"
    position = 0

    while position < len(DNA_sequence): # while loop which will continue to go through the dna sequence until position reches the value of the length of the sequence

        start_found = False # defining the start and end of the gene as false so that when the codons are found they can be changed to true
        end_found = False

        for base_number in range(position, len(DNA_sequence) - 2):# go through the dna sequence starting from the position variable until it reaches the end of the sequence - 2 (as the last codon will be 3 base pairs long)
            if  DNA_sequence[base_number:base_number + 3] == start_codon:  # if base number to base number + 3 (3 base pairs therefore codon) == ATG then continue
                sequence_after_start = DNA_sequence[base_number:]  # defining the sequence after the start codon as the dna sequence from the base number (A in ATG) to the end of the sequence 
                start_found = True # change the start found to true as the start codon has been found 
                start_codon_position = base_number # defining where the start codon is in the sequence (A in ATG)
                break

        if not start_found: # if start_found  == false still and has not been changed to true then the start codon has not been found and the loop needs to end to stop it going on forever 
                break
                            

        new_DNA_sequence_list_divided3 = [sequence_after_start[i:i+3] for i in range(0, len(sequence_after_start) - len(sequence_after_start) % 3, 3)]
        # this defines a new list which will be the sequence after the start codon divided into codons (3 base pairs) and will not include any base pairs which are left over at the end of the sequence which do not make a full codon

        for index, codon in enumerate(new_DNA_sequence_list_divided3):# go through the new list of codons and find the index of each codon in the list 
            if codon in end_codon: # if the codon is in the list of end codons then continue 
                end_codon_position = index * 3 # define the position of the end codon as the index of the codon in the list and then multiply that by 3 to get the position in the sequence
                end_found = True # change end_found to equal true as the end codon has been found
                finished_gene = sequence_after_start[:end_codon_position + 3] # define the finished gene as the sequence after the start codon from the start codon to the end codon (end codon position + 3 to include the end codon)
                
                if searching_method == 1: # if the search method is 1 then the next loop will start from the next avaliable ATG and the next avaliable stop codon
                    position = start_codon_position + 1 # change position to the start codon position + 1 so that the next loop will start from the next base pair after the start codon (ATGX, it will start from X)



                elif searching_method == 2: # if the search method is 2 then the next loop will start from the next avaliable ATG after the last stop codon
                    position = (end_codon_position + start_codon_position + 1)

                if len(finished_gene) >= min_length:
                    gene_info = (
                        f"Gene {gene_number}: \n"
                        f"================== \n"
                        f"Start position: {(start_codon_position + 1)} \n"
                        f"End position: {end_codon_position + start_codon_position + 4}"
                    )

                    genes[gene_info] = finished_gene

                    # add the finished gene to the genes dictionary with the key being the gene number and the value being the finished gene
                    
                    gene_number = gene_number + 1 

                break# once the end codon has been found the break the loop to stop it going on forever


        if not end_found: # if end_found == false then the end codon has not been found and the loop needs to continue to find the next start codon
                position = start_codon_position + 1 # change position to the start codon position + 1 so that the next loop will start from the next base pair after the start codon (ATGX, it will start from X)
                continue
    
    return genes # return the genes dictionary which contains the gene number as the key and the finished gene as the value


# convert the DNA sequence into amino acids and turn them into dictionarys to be printed
def convert_sequence_to_amino_acids_C(gene_dictionary, min_length):

    Amino_acid_sequences = {}
    # define amino acid sequences as an empty dictionary

    for gene, DNA_sequence in gene_dictionary.items(): # go through the gene dictionary and get the gene number and the DNA sequence for each gene

        if len(DNA_sequence) < min_length:
            continue

        amino_acids = [] # define amino acids as an empty list which will be filled with the amino acids for each gene
        
        for base in range(0, len(DNA_sequence), 3): # go through the DNA sequence in steps of 3 (codons) and get the base number for each codon
            codon = DNA_sequence[base:base + 3] # define the codon as the base number to the base number + 3 (3 base pairs therefore codon)
            amino_acid = Amino_acids_DNA [codon] # get the amino acid for the codon from the Amino_acids_DNA dictionary and define it as amino_acid
            amino_acids.append(amino_acid) # add the amino acid to the amino acids list for each gene
        
        Amino_acid_sequences[gene] = ( # add the gene number and the amino acids list to the Amino_acid_sequences dictionary with the key being the gene number and the value being the amino acids list
             f"Length of gene: {len(DNA_sequence)} base pairs \n"
             f"Number of amino acids: {int(len(DNA_sequence) / 3)} \n"
             f" \n"
             f"DNA sequence: {DNA_sequence}\n"# add the DNA sequence to the value of the dictionary
             f" \n"
             f"Resulting protein: {" ".join(amino_acids)} \n"# add the amino acids list to the value of the dictionary and join them with a space in between each amino acid
             f" \n"
             f"================== \n"
        )

    return Amino_acid_sequences # return the Amino_acid_sequences dictionary which contains the gene number as the key and the DNA sequence and amino acids list as the value


#  sequence length + % composition + check bases are all correct
def analyse_data_R(RNA_sequence_rough):

    ###########################################
    #inputs, sorting and checking the RNA sequence


    RNA_sequence = RNA_sequence_rough.upper() # convert RNA sequence to upper case
    RNA_sequence2 = RNA_sequence
    
    if all(base in "AUCG" for base in RNA_sequence): # check to make sure that all of the bases in the sequence are only A T G and C
        pass
    else:
        return print("ERROR: mRNA sequence must only contain the bases U, G, C, A")
    
    ############################################
    #general facts about RNA sequence

    RNA_sequence_length = len(RNA_sequence) # find length of RNA sequence

    num_of_A_and_U = RNA_sequence.count("A") + RNA_sequence.count("U")  # find % of A and T 
    percentage_of_A_and_U = (num_of_A_and_U / len(RNA_sequence)) * 100

    num_of_C_and_G = RNA_sequence.count("C") + RNA_sequence.count("G")  # find % of C and G
    percentage_of_C_and_G = (num_of_C_and_G / len(RNA_sequence)) * 100

    general_facts = (
    "\n "
    "-------------------------------------------------------"
    "\n "
    "General facts: "
    "\n "
    f"Length of mRNA sequence: {RNA_sequence_length} base pairs \n"
    f"Percentage of Adenine and Uracil in mRNA strand:  {round(percentage_of_A_and_U, 2)} % \n"
    f"Percentage of Cytosine and Guanine in mRNA strand:  {round(percentage_of_C_and_G, 2)} % \n"
    "\n "
    "-------------------------------------------------------"
    "\n "
    "Resulting genes and amino acids"
    "\n "
    )
    return general_facts, RNA_sequence2


# find the genes
def find_genes_R(RNA_sequence, min_length, searching_method):

    gene_number = 1
    genes = {}
    end_codon = ["UAA", "UAG", "UGA"]
    start_codon = "AUG"
    position = 0

    while position < len(RNA_sequence):

        start_found = False 
        end_found = False

        for base_number in range(position, len(RNA_sequence) - 2):    
            if  RNA_sequence[base_number:base_number + 3] == start_codon:  # if any section of 3 base pairs = ATG then continue
                sequence_after_start = RNA_sequence[base_number:]  
                start_found = True
                start_codon_position = base_number
                break

        if not start_found:
                break
                            

        new_RNA_sequence_list_divided3 = [sequence_after_start[i:i+3] for i in range(0, len(sequence_after_start) - len(sequence_after_start) % 3, 3)]

        for index, codon in enumerate(new_RNA_sequence_list_divided3):
            if codon in end_codon:
                end_codon_position = index * 3
                end_found = True
                finished_gene = sequence_after_start[:end_codon_position + 3]
                

                if searching_method == 1: # if the search method is 1 then the next loop will start from the next avaliable ATG and the next avaliable stop codon
                    position = start_codon_position + 1 # change position to the start codon position + 1 so that the next loop will start from the next base pair after the start codon (ATGX, it will start from X)

                elif searching_method == 2: # if the search method is 2 then the next loop will start from the next avaliable ATG after the last stop codon
                    position = (end_codon_position + start_codon_position + 1)

                if len(finished_gene) >= min_length:
                    gene_info = (
                        f"Gene {gene_number}: \n"
                        f"================== \n"
                        f"Start position: {start_codon_position} \n"
                        f"End position: {end_codon_position + start_codon_position + 3}"
                    )

                    genes[gene_info] = finished_gene

                    # add the finished gene to the genes dictionary with the key being the gene number and the value being the finished gene

                    gene_number = gene_number + 1
                break

        if not end_found:
                position = start_codon_position + 1
                continue
    
    return genes


# converts the mRNA sequence into amino acids and turns them into dictionaries to be printed
def convert_sequence_to_amino_acids_R(gene_dictionary, min_length, search_method):

    Amino_acid_sequences = {}

    for gene, RNA_sequence in gene_dictionary.items():
        amino_acids = []

        for base in range(0, len(RNA_sequence), 3):
            codon = RNA_sequence[base:base + 3]
            amino_acid = Amino_acids_RNA [codon]
            amino_acids.append(amino_acid)
        
        Amino_acid_sequences[gene] = (
             f"Length of gene: {len(RNA_sequence)} base pairs \n"
             f"Number of amino acids: {int(len(RNA_sequence) / 3)} \n"
             f" \n"
             f"RNA sequence: {RNA_sequence}\n"
             f" \n"
             f"Resulting protein: {' '.join(amino_acids)} \n"
             f" \n"
             f"================== \n"
             )

 
    return Amino_acid_sequences


def save_to_file(results):
    print ("Would you like to save the result as a file? (Y/N)")
    file_decision1 = input()
    file_decision = file_decision1.upper()
    if file_decision == "Y" or file_decision == "N" or file_decision == "yes" or file_decision == "Yes" or file_decision == "no" or file_decision == "No" or file_decision == "YES" or file_decision == "NO":
        pass
    else:
        return "Error: please enter Yes or No"
    if file_decision == "Y" or file_decision == "yes" or file_decision == "Yes" or file_decision == "YES":
        print ("Please enter the filename: ")
        filename = input()
        with open(filename + ".txt", "w") as file: 
            file.write(results)
        print ("File saved successfully")
    else:
        return "File not saved"



results = (hello_sequence())
print (results)
save_to_file(results)



# currently trying to make it save a file at the end 
# need to make (results) work in save_to_file() by making hello_sequence() return everything to the terminal then after print results then send that to the file function which will be a pain
# then hopefully should work

