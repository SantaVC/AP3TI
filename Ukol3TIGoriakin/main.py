def ka(slovo, Q, I, f, q0, P):
    stav = q0

    for i in range(len(slovo)):
        char = slovo[i]

        if char not in I:
            return False

        if (stav, char) not in f.keys():
            return False

        stav = f[(stav, char)]
    if stav in P:
        return True
    else:
        return False


slovo1 = "01010110"
slovo2 = "0111"
q = {"q0", "q1"}
I = {"0", "1"}
f = {
    ("q0", "0"): 'q0',
    ("q0", "1"): 'q1',
    ("q1", "1"): 'q1',
    ("q1", "0"): 'q0'
}
q0 = "q0"
p = {"q1"}

print("Priklad 1 pro slovo", slovo1, "je:", ka(slovo1, q, I, f, q0, p))
print("Priklad 2 pro slovo", slovo2, "je:", ka(slovo2, q, I, f, q0, p), "\n")

slovo1 = "0100011"
slovo2 = "01010"
q = {"q0", "q1", "q2", "q3", "q4"}
I = {"0", "1"}
f = {
    ("q0", "0"): 'q1',
    ("q0", "1"): 'q2',
    ("q1", "0"): 'q1',
    ("q1", "1"): 'q3',
    ("q2", "0"): 'q1',
    ("q2", "1"): 'q2',
    ("q3", "0"): 'q1',
    ("q3", "1"): 'q4',
    ("q4", "0"): 'q1',
    ("q4", "1"): 'q2'
}
q0 = "q0"
p = {"q4"}


print("Priklad 3 pro slovo", slovo1, "je:", ka(slovo1, q, I, f, q0, p))
print("Priklad 4 pro slovo", slovo2, "je:", ka(slovo2, q, I, f, q0, p), "\n")

slovo1 = "101"
slovo2 = "01"
q = {"q0", "q1", "q2"}
I = {"0", "1"}
f = {
    ("q0", "0"): 'q1',
    ("q0", "1"): 'q2',
    ("q1", "0"): 'q2',
    ("q1", "1"): 'q1',
    ("q2", "0"): 'q2',
    ("q2", "1"): 'q0',

}
q0 = "q0"
p = {"q1"}

print("Priklad 5 pro slovo", slovo1, "je:", ka(slovo1, q, I, f, q0, p))
print("Priklad 6 pro slovo", slovo2, "je:", ka(slovo2, q, I, f, q0, p))
