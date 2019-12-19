cmd line:
Step 1: go back to previous folder
```shell
cd ..  
```
Step 2: run the benchmarks
```shell
python3 compile_with_chipmunk.py benchmarks_running_for_a_long_time/blue_decrease_mutation_1.c 1 chipmunk_alus/stateful_alus/sub.alu chipmunk_alus/stateless_alus/stateless_alu.alu 4 2 "0,1,2,3,10" 10
python3 compile_with_chipmunk.py benchmarks_running_for_a_long_time/flowlets_mutation_1.c 1 chipmunk_alus/stateful_alus/pred_raw.alu chipmunk_alus/stateless_alus/stateless_alu.alu 4 5 "0,1,2,3,5" 10
```
