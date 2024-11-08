personagem1 = input("Nome da primeira personagem: ") 
vida1 = int(input("Vida da personagem: "))
lvl1 = int(input("Nivel da personagem: "))

personagem2 = input("Nome da segunda personagem: ")
vida2 = int(input("Vida da personagem: "))
lvl2 = int(input("Nivel da personagem: "))

personagem3 = input("Nome da terceira personagem: ")
vida3 = int(input("Vida da personagem: "))
lvl3 = int(input("Nivel da personagem: "))

array = [
    [personagem1,(vida1,lvl1)],
    [personagem2,(vida2,lvl2)],
    [personagem3,(vida3,lvl3)]
]
print(array)

def lvl_ordem(ordem):
    for a in range(len(ordem)):
        for b in range(0,len(ordem)-a-1):
            if ordem[b][1][1]<ordem[b+1][1][1]:
                ordem[b],ordem[b+1] = ordem[b+1], ordem[b]
lvl_ordem(array)

for c in array:
    print(c[0])