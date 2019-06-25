def gera_primos(n):
  primos = []
  for i in range(2,n+1):
    div = 0
    for j in range(2,int(i/2)+1):
      if i%j==0:
        div += 1
    if div == 0:
      primos.append(i)
  
  return primos



def combinacao_fatores(n):
  todas_combinacoes = []
  combinacao_fator = []

  comb_fat_rec(2,n,todas_combinacoes,combinacao_fator)
  return todas_combinacoes


def comb_fat_rec(fator_atual, n, todas, comb_fator):
  if n <= 1:
    temp = comb_fator[:]
    temp.sort(reverse=True)
    t = tuple(temp)
    if t not in todas:
      todas.append(t)
  
  for i in range(fator_atual, n+1):    
    if n%i == 0:
      comb_fator.append(i)

      comb_fat_rec(i, n//i, todas, comb_fator)

      del comb_fator[-1]

def gera_candidato(primos,combinacao):
  candidato = 1
  for i in range(len(combinacao)):
    candidato *= primos[i]**(combinacao[i]-1)
  return candidato

def calcula(n,primos):
  todas = combinacao_fatores(n)
  candidatos = []
  for c in todas:
    candidato = gera_candidato(primos, c)
    candidatos.append(candidato)
  
  return min(candidatos)


def main():
  primos = gera_primos(100)
  c = int(input())
  for i in range(c):
    n = int(input())
    print(calcula(n,primos)%1000000007)

main()
