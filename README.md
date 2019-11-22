1. First install the master branch of chipmunk (https://github.com/chipmunk-project/chipmunk)
2. Then install the master branch of domino-compiler (https://github.com/chipmunk-project/domino-compiler)
3. To run chipmunk, use a command line like this:
```shell
canonicalizer     blue_decrease.c > blue_decrease.sk
iterative_solver  blue_decrease.sk sub.alu stateless_alu.alu 4 2 "0,1,2,3" 10
```
4. To run domino, use a command line like this:
```shell
domino blue_decrease.c sub.sk 10 10
```
