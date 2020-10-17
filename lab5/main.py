from sort import insertion_sort
from sort import merge_sort

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    input_list = input_file.read().split() # get list of each number's string
    input_list = [int(x) for x in input_list] # change element to int
    input_file.close()

    answer = sorted(input_list) # ground truth using python's sort
    
    print("INSERTION SORT")
    output_insertion = insertion_sort(input_list)
    #print(output_insertion)
    assert output_insertion == answer # check if our answer is the same with python's sort

    print("MERGE SORT")
    output_merge = merge_sort(input_list)
    #print(output_merge)
    assert output_merge == answer # check if our answer is the same with python's sort

    
    output_file = open("output.txt", "w")
    output_file.write("{:15} | {:15}\n".format("INSERTION SORT", "MERGE SORT"))
    for i in range(len(input_list)):
        output_file.write("{:<15d} | {:<15d}\n".format(output_insertion[i], output_merge[i]))

    output_file.close()