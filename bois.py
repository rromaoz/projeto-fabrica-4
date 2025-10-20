print("=== Fazenda Rio Claro ===")
print("Organização dos bois para embarque na feira agropecuária\n")

# Lista para armazenar os bois
bois = []

# Lista fixa com os nomes dos bois (poderia ser digitada também)
nomes_bois = ["Gallardo", "Huracan", "Tempesta"]

# Entrada de dados
for nome in nomes_bois:
    peso = float(input(f"Digite o peso de {nome} (em kg): "))
    bois.append({"nome": nome, "peso": peso})

# Ordena os bois pelo peso (maior -> menor)
bois.sort(key=lambda b: b["peso"], reverse=True)

# Exibe o ranking
print("\n=== Ranking dos Bois (do mais pesado ao mais leve) ===")
for i, boi in enumerate(bois, start=1):
    print(f"{i}º lugar: {boi['nome']} - {boi['peso']:.2f} kg")

# Destaque do campeão
print(f"\n🏆 O boi mais pesado é {bois[0]['nome']} com {bois[0]['peso']:.2f} kg!")
print("\nEmbarque pronto! 🚛🐮")