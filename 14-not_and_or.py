# Obs: not tem uma prioridade mais baixa que os operadores relacionais. 
# Portanto, not a == b é interpretado como: not (a == b) e a == not b gera um erro de sintaxe.

# Obs2: Assim como as operações matemáticas possuem ordem de precedência, as operações booleanas também têm. 
# Essa prioridade obedece à seguinte ordem: not primeiro, and em seguida e or por último (BANIN, 2018).

A = 15
B = 9
C = 9

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C )