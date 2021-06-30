# Take an amino acid input sequence and create a permutation array .txt file given a target AA and mutant
# Was written during my NSERC USRA placement in 2018.


from itertools import product

inputseq = input("Enter sequence: ").upper()
residue = input("Which residue will be mutated out? ").upper()
mutant = input("Which residue will be the mutant? ").upper()
print("Number of ",  residue,  "residues: ", )
combonumber = 2**inputseq.count(residue)
print("Total combinations ", combonumber)

seqarray = list(inputseq)
seqarray.append("a")
filename = list(inputseq)
filename.append(".txt")
fn = ''.join(filename)
print(''.join(filename))
i = 0
positions = []

while i < len(inputseq):
    if seqarray[i] == residue:
        positions.append(i)
    i += 1


li = [residue, mutant]
for comb in product(li, repeat=inputseq.count(residue)):
    ##print(''.join(comb))
    combos = []
    combos.append(comb)
    n = 0
    while n < len(comb):
        seqarray[positions[n]] = comb[n]
        ##print(seqarray,"seqarray")
        n += 1
    print(" ".join(seqarray),file=open(fn, "a"))




