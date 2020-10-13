#part1 Linux
#1)
 wc genome*.dat
#2)
cmp -l genome*.dat
#3)
cmp -l genome*.dat | wc -l
#4) 
grep -o "AAAAAAAAAATTTTTTTTTT" genome_01.dat
#5)
grep -Eo "A{10}T{10}" genome_01.dat | wc -l