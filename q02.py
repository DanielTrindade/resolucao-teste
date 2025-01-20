def pertence_fib(target):
  if target < 0:
    return False
  if target == 0 or target == 1:
    return True
  ant = 0
  atual = 1

  while atual <= target:
    if atual == target:
      return True
    prox = ant + atual
    ant = atual
    atual = prox
  return False



ent = int(input())

pertence = pertence_fib(ent)
print({True: "Pertence", False: "Não pertence"}[pertence])

