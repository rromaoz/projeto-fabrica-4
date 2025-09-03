# 🐂 Ordenador de Bois da Fazenda

Um mini-projeto em **Python** para ler **três bois** (nome e peso) e exibir um **ranking do mais pesado para o mais leve**.  
Foco em praticar **entrada de dados**, **conversão para `float`**, **ordenação** e **saída formatada** — tudo com um toque de **mundo real**.

---

## 🎯 Objetivo Educacional
- Reforçar o fluxo **entrada → processamento → saída**.
- Praticar `input()`, conversão para `float` e **f-strings**.
- Trabalhar **ordenação decrescente** com `sorted(..., reverse=True)`.
- Exercitar leitura e impressão de dados com **experiência de terminal** (UX simples).

---

## 📖 Histórinha
A **Fazenda Rio Claro** foi convidada para uma feira agropecuária e precisa organizar o embarque de **três bois**.  
Para otimizar a logística (espaço no caminhão, sequência de apresentação e controle de manejo), a equipe decidiu embarcar os animais **do mais pesado para o mais leve**.  
Você ficou responsável por criar um **programa simples** que peça o **nome** e o **peso** dos bois e mostre um **ranking**. Assim, ninguém perde tempo reordenando os animais na hora da saída! 😉

---

## 📝 Enunciado
Faça um programa que pergunte o **nome** e o **peso** de **três bois** e **mostre-os em ordem decrescente de peso** (do mais pesado para o mais leve).

> **Simplificações propositalmente didáticas**
> - Usaremos **apenas três bois**.
> - Os **pesos** devem ser digitados como `float` usando **ponto** como separador decimal (ex.: `512.3`).  
> - Não há validações avançadas (para deixar o foco na lógica principal).

---

## 🔎 Exemplo de execução
```
Nome do boi 1: Maromba
Peso de Maromba (kg, use ponto, ex.: 485.7): 485.7
Nome do boi 2: Trovão
Peso de Trovão (kg, use ponto, ex.: 485.7): 512.3
Nome do boi 3: Carvão
Peso de Carvão (kg, use ponto, ex.: 485.7): 498.0

=== Ranking (mais pesado → mais leve) ===
1) Trovão — 512.30 kg
2) Carvão — 498.00 kg
3) Maromba — 485.70 kg
```

---


## 💻 Como executar

Pré‑requisito: **Python 3.8+**

1) Clone este repositório ou baixe os arquivos.
```bash
git clone https://github.com/seu-usuario/projeto-fabrica-4.git
cd projeto-fabrica-4
```

2) Rode o programa:
```bash
python ordenar_bois.py
```

> Dica (Windows): se `python` não funcionar, tente `py ordenar_bois.py`.

3) Siga as instruções no terminal e **digite os pesos com ponto** (`.`).

---

## 🧠 Conceitos trabalhados
- Leitura de dados com `input()`  
- Conversão de texto para número (`float`)  
- Estruturas sequenciais (listas/tuplas)  
- **Ordenação decrescente**: `sorted(bois, key=lambda x: x[1], reverse=True)`  
- Exibição com **f-strings** e formatação `:.2f`

---

## 🚀 Extensões sugeridas (para avançar aos poucos)
- **Mais bois**: permitir cadastrar `N` bois e ordenar todos.
- **Validação**: impedir pesos negativos ou entradas vazias.
- **Critérios alternativos**: ordenar por **idade**, **altura** ou **ID**.
- **Empate**: tratar bois com o **mesmo peso**.
- **Exportação**: salvar o ranking em um `.csv`.
- **Interface gráfica**: criar uma GUI simples com **Tkinter**.

> Dica pedagógica: comece simples (versão atual) e vá adicionando uma extensão por vez. 🧩

---

## 📂 Estrutura do projeto
```
ordenar-bois-fazenda-simples/
├─ ordenar_bois.py  # Programa principal (versão simples)
└─ README.md        # Este arquivo
```

---

## 📝 Licença
Este projeto está sob licença **MIT** — você pode usar, adaptar e compartilhar. ✨
****
