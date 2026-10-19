def get_sequence():
    sequence_1 = input("Hello please enter the first sequence which you would like to compare ")
    sequence_1 = sequence_1.upper()
    sequence_1 = sequence_1.replace(" ", "") 
    if all(base in "ATGC" for base in sequence_1):
        pass
    else:
        return "Please enter a valid sequence containing only A, T, G, and C."
            
        
    sequence_2 = input("Hello please enter the second sequence which you would like to compare ")
    sequence_2 = sequence_2.upper()
    sequence_2 = sequence_2.replace(" ", "") 
    if all(base in "ATGC" for base in sequence_2):
        pass
    else:
        return "Please enter a valid sequence containing only A, T, G, and C."

    return sequence_1, sequence_2

def intro_sequence(sequence_1, sequence_2):
    

    number_of_differences = 0
    
    for base_1, base_2 in zip(sequence_1, sequence_2):
        if base_1 != base_2: 
            number_of_differences += 1
        else:
            pass
            
    number_of_matching_positions = 0

    for base_1, base_2 in zip(sequence_1, sequence_2):
        if base_1 == base_2:
            number_of_matching_positions += 1
    
        
    if len(sequence_1) > len(sequence_2):
        total_length = len(sequence_2)
        extra_bases = len(sequence_1) - len(sequence_2)
    elif len(sequence_2) > len(sequence_1):
        total_length = len(sequence_1)
        extra_bases = len(sequence_2) - len(sequence_1)
    else:
        total_length = len(sequence_1)
        extra_bases = 0

    percentage_of_matching_positions = number_of_matching_positions / total_length * 100
    percentage_of_matching_positions = round(percentage_of_matching_positions, 2)


    if len(sequence_1) > len(sequence_2):
        end_facts = (
            " "
            "\n "
            "===================================================="
            "\n "
            " "
            "\n "
            f"The percentage of positions that match in the two sequences is {percentage_of_matching_positions}%. "
            "\n "
            f"Sequence 1 is longer than Sequence 2 by {extra_bases} bases with sequence 2 being {len(sequence_2)} bases long and sequence 1 being {len(sequence_1)} bases long. "  
            "\n "
            f"There are {number_of_differences} differences in the first {total_length} bases."     
            "\n "
            " "
            "\n "
            "===================================================="


        )

    elif len(sequence_2) > len(sequence_1):
        end_facts = (
            " "
            "\n "
            "===================================================="
            "\n "
            " "
            "\n "
            f"The percentage of positions that match in the two sequences is {percentage_of_matching_positions}%. "
            "\n "
            f"Sequence 2 is longer than Sequence 1 by {extra_bases} bases with sequence 1 being {len(sequence_1)} bases long and sequence 2 being {len(sequence_2)} bases long. "  
            "\n "
            f"There are {number_of_differences} differences in the first {total_length} bases."     
            "\n "
            " "
            "\n "
            "===================================================="
        )

    else:
        end_facts = (
            " "
            "\n "
            "===================================================="
            "\n "
            " "
            "\n "
            f"The percentage of positions that match in the two sequences is {percentage_of_matching_positions}%. "
            "\n "
            f"Both sequences are the same length with sequence 1 being {len(sequence_1)} bases long and sequence 2 being {len(sequence_2)} bases long. "  
            "\n "
            f"There are {number_of_differences} differences in the first {total_length} bases."     
            "\n "
            " "
            "\n "
            "===================================================="
        )


    zips = list(zip(sequence_1, sequence_2))


    return end_facts, zips





sequence_1, sequence_2 = get_sequence()
end_facts, zips = intro_sequence(sequence_1, sequence_2)
print(end_facts)
print (zips)
def sequence_comparison(zips):



    for base_1, base_2 in zips:
        if base_1 == base_2:
            pass
        elif base_1 != base_2:
