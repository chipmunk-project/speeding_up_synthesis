1. First install the master branch of chipmunk (https://github.com/chipmunk-project/chipmunk)
2. Then install the master branch of domino-compiler (https://github.com/chipmunk-project/domino-compiler)
3. To run chipmunk, use a command line like this:
```shell
python3 compile_with_chipmunk.py domino_benchmarks/rcp.c 1 chipmunk_alus/stateful_alus/pred_raw.alu chipmunk_alus/stateless_alus/stateless_alu.alu 3 3 "0,1,2,3" 10
python3 compile_with_chipmunk.py domino_benchmarks/blue_increase.c 1 chipmunk_alus/stateful_alus/pred_raw.alu chipmunk_alus/stateless_alus/stateless_alu.alu 4 2 "0,1,2,3" 10
python3 compile_with_chipmunk.py domino_benchmarks/blue_decrease.c 1 chipmunk_alus/stateful_alus/sub.alu chipmunk_alus/stateless_alus/stateless_alu.alu 4 2 "0,1,2,3" 10
```
4. To run domino, use a command line like this:
```shell
domino domino_benchmarks/blue_decrease.c domino_atoms/sub.sk 10 10
domino domino_benchmarks/blue_increase.c domino_atoms/pred_raw.sk 10 10
domino domino_benchmarks/rcp.c domino_atoms/pred_raw.sk 10 10
```
5. Examples fails for domino but success for Chipmunk
```shell
python3 compile_with_chipmunk.py success_for_chipmunk_fail_for_domino/blue_increase_equivalent.c 1 chipmunk_alus/stateful_alus/pred_raw.alu chipmunk_alus/stateless_alus/stateless_alu.alu 4 2 "0,1,2,3" 10
domino success_for_chipmunk_fail_for_domino/blue_increase_equivalent.c domino_atoms/pred_raw.sk 10 10
```
