# This file will take domino program as input and compile with Chipmunk compiler

# Step1: transform domino program to .sk file
# domino.c --- (canonicalizer) ---> domino_canonicalizer.c
# --- (grouper) ---> a_group_of_domino.c --- (domino_to_chipmunk) ---> chipmunk.sk

# Step2: run iterative_solver on generated .sk file

import sys
import re
import subprocess
import time

def main(argv):
    """Main program"""

    # deal with input 
    # cmd line: python3 XX.py domino.c group_size stateful_alu stateless_alu length width "0,1,2,3" 10         ok 
    # take domino.c as example
    # run canonicalizer
    # run grouper 
    # run domino_to_chipmunk
    # run iterative_solver
    if len(argv) != 9:
        print("Usage: python3 " + argv[0] + " <domino program> <group size> " +
              "<stateful_alu> <stateless_alu> <num of pipelines> <num of ALUs per stage> " +
              "<constant set> <input bits>")
        sys.exit(1)
    else:
        domino_program = str(argv[1])
        group_size = str(argv[2])
        stateful_alu = str(argv[3])
        stateless_alu = str(argv[4])
        num_of_pipelines = str(argv[5])
        num_of_alu_per_stage = str(argv[6])
        constant_set = str(argv[7])
        input_bits = str(argv[8])

    # get the name of .c file 
    # domino_program_name.c --> domino_program_name
    domino_program_name = domino_program.split("/")[len(domino_program.split("/")) - 1].split(".")[0]
    assert(domino_program_name.find('/') == -1)
    canonicalized_program = "/tmp/" + domino_program_name + "_canonicalized.c"

    cmd_to_canonicalizer = "canonicalizer " + domino_program + " > " + canonicalized_program
    (ret_code_canonicalizer, _) = subprocess.getstatusoutput(cmd_to_canonicalizer)
    # print(cmd_to_canonicalizer)
    assert(ret_code_canonicalizer == 0)

    cmd_to_grouper = "grouper " + canonicalized_program + " " + group_size
    (ret_code_grouper, grouper_output) = subprocess.getstatusoutput(cmd_to_grouper)
    # print(cmd_to_grouper)
    assert(ret_code_grouper == 0)
   
    total_num_of_grouped_files = int(grouper_output)
    for i in range(total_num_of_grouped_files):
        grouper_file_name = "/tmp/" + domino_program_name + "_canonicalized_equivalent_" + str(i) + ".c"
        chipmunk_program_name = "/tmp/" + domino_program_name + "_" + str(i) + ".sk"
        cmd_to_domino_to_chipmunk = "domino_to_chipmunk " + grouper_file_name + " > " + chipmunk_program_name
        # print("cmd_to_domino_to_chipmunk::",cmd_to_domino_to_chipmunk)
        (ret_code_domino_to_chipmunk, domino_to_chipmunk_output) = subprocess.getstatusoutput(cmd_to_domino_to_chipmunk)
        assert(ret_code_domino_to_chipmunk == 0)
        # print(cmd_to_domino_to_chipmunk)
        cmd_to_iterater_solver = "time iterative_solver " + chipmunk_program_name + " " +\
                             stateful_alu + " " + \
                             stateless_alu + " " + num_of_pipelines + " " + \
                             num_of_alu_per_stage + " " + "\"" + constant_set + "\"" +\
                             " " + input_bits
        # print(cmd_to_iterater_solver)
        start_time = time.time()
        (ret_code_iterative_solver, _) = subprocess.getstatusoutput(cmd_to_iterater_solver)
        end_time = time.time()
        if ret_code_iterative_solver == 0:
            print("Compilation succeeds for Program: " + domino_program_name + ", with stateful alu: " + stateful_alu + 
                  " and stateless alu: " + stateless_alu + ", with grid size: " + num_of_pipelines + " * " + num_of_alu_per_stage)
            print("Total time used for this compilation is " + str(round(end_time - start_time, 2)) + " seconds")
            sys.exit(0)
    print("Compilation fails for Program: " + domino_program_name + ", with stateful alu: " + stateful_alu + 
          " and stateless alu: " + stateless_alu + ", with grid size: " + num_of_pipelines + " * " + num_of_alu_per_stage)
    sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)
