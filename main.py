import csv

# ===========================
# Função: carregar_produtos
# Lê os dados do CSV e carrega na memória
# ===========================
def carregar_produtos(caminho):
    produtos = []
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            produtos.append({
                "nome": linha["nome"],
                "categoria": linha["categoria"],
                "tipo": linha["tipo"],
                "preco": float(linha["preco"])
            })
    return produtos

# ===========================
# Exibir produtos no terminal
# ===========================
def mostrar_produtos(produtos):
    print("\n🧺 Lista de Produtos Disponíveis:\n")
    for i, produto in enumerate(produtos, 1):
        tipo = "kg" if produto["tipo"] == "peso" else "unidade"
        print(f"{i}. {produto['nome']} ({produto['categoria']}) - R$ {produto['preco']:.2f} por {tipo}")
    print()

# ===========================
# Adiciona item ao carrinho
# ===========================
def adicionar_ao_carrinho(produtos, carrinho):
    mostrar_produtos(produtos)
    escolha = input("Digite o número do produto que deseja adicionar ao carrinho: ").strip()

    # Validando a escolha do usuário
    if not escolha.isdigit() or not (1 <= int(escolha) <= len(produtos)):
        print("⚠️ Opção inválida. Tente novamente.\n")
        return

    produto = produtos[int(escolha) - 1]

    # Pergunta a quantidade com base no tipo (peso ou unidade)
    if produto["tipo"] == "peso":
        quantidade = input(f"Quantos quilos de {produto['nome']} você deseja? ")
    else:
        quantidade = input(f"Quantas unidades de {produto['nome']} você deseja? ")

    # Validando para que o usuário insira uma quantidade válida
    try:
        quantidade = float(quantidade)
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        print("⚠️ Quantidade inválida. Por favor, insira um valor numérico positivo.\n")
        return

    # Adiciona ao carrinho
    total_item = quantidade * produto["preco"]
    carrinho.append({
        "nome": produto["nome"],
        "categoria": produto["categoria"],
        "tipo": produto["tipo"],
        "preco_unitario": produto["preco"],
        "quantidade": quantidade,
        "total": total_item
    })

    print(f"✅ {produto['nome']} adicionado ao carrinho com sucesso!\n")

# ===========================
# Finaliza a compra e gera nota
# ===========================
def finalizar_compra(carrinho):
    print("\n🧾 Gerando sua nota fiscal...\n")
    total_geral = sum(item["total"] for item in carrinho)
    nome_arquivo = "nota_fiscal.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("===== NOTA FISCAL DO MINI MERCADO =====\n\n")
        for item in carrinho:
            tipo = "kg" if item["tipo"] == "peso" else "unid."
            f.write(f"{item['nome']} ({item['categoria']}) - {item['quantidade']} {tipo} x R$ {item['preco_unitario']:.2f} = R$ {item['total']:.2f}\n")
        f.write(f"\nTOTAL DA COMPRA: R$ {total_geral:.2f}\n")
        f.write("\nObrigado por comprar com a gente! Volte sempre! 🛒")

    print(f"🎉 Compra finalizada com sucesso!")
    print(f"💰 Total: R$ {total_geral:.2f}")
    print(f"📄 Nota fiscal salva como '{nome_arquivo}'\n")

# ===========================
# Função principal (main loop)
# ===========================
def main():
    produtos = carregar_produtos("produtos.csv")
    carrinho = []
    primeira_compra = True  # Para mudar a mensagem do menu

    print("🛒 Bem-vindo(a) ao Mini Mercado!\n")

    while True:
        print("\n📋 MENU PRINCIPAL")
        if primeira_compra:  # Se for a primeira compra, exibe "Comprar"
            print("1 - Comprar")
        else:
            print("1 - Continuar comprando")
        print("2 - Finalizar compra")
        print("3 - Sair sem comprar")

        opcao = input("\nDigite o número da opção desejada: ").strip()

        if opcao == "1":
            adicionar_ao_carrinho(produtos, carrinho)
            primeira_compra = False  # Após a primeira compra, muda o menu
        elif opcao == "2":
            if carrinho:
                finalizar_compra(carrinho)
            else:
                print("🛒 Seu carrinho está vazio! Adicione produtos antes de finalizar.")
            break
        elif opcao == "3":
            print("\n👋 Até logo! Agradecemos sua visita.")
            break
        else:
            # Validando se a opção digitada é válida
            print("⚠️ Opção inválida. Por favor, escolha 1, 2 ou 3.\n")

# ===========================
# Execução do programa
# ===========================
if __name__ == "__main__":
    main()    