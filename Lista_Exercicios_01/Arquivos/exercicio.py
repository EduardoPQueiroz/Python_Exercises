import os
os.system("cls")

# Lista de comentários sobre um smartphone
comentarios = [
    "Ótimo smartphone, recomendo!",
    "A câmera é incrível, tira fotos nítidas.",
    "Bateria dura o dia todo, muito satisfeita.",
    "O desempenho é rápido, sem travamentos.",
    "Design elegante e moderno, amei!",
    "A tela é muito boa, ótima para assistir vídeos.",
    "Chegou rápido, muito feliz com a entrega.",
    "A qualidade do som é excelente.",
    "A interface é intuitiva e fácil de usar.",
    "O preço vale a pena pela qualidade.",
    "Fiquei impressionado com a durabilidade da bateria.",
    "Não gosto do tamanho, é um pouco grande para mim.",
    "O suporte ao cliente foi ótimo, ajudaram rapidamente.",
    "Apenas o carregador poderia ser mais rápido.",
    "As atualizações são frequentes e melhoram o desempenho.",
    "Os aplicativos rodam muito bem, sem lags.",
    "A cor do aparelho é linda, exatamente como na foto.",
    "A segurança biométrica é rápida e precisa.",
    "A memória interna é suficiente para meus aplicativos.",
    "O smartphone esquentou um pouco durante jogos intensos.",
    "A qualidade de construção é robusta, parece durável.",
    "O reconhecimento facial é prático e funciona bem.",
    "As configurações são fáceis de ajustar.",
    "Faltam alguns recursos que eu gostaria de ter.",
    "A experiência geral é muito positiva.",
    "O modo noturno da câmera é ótimo para fotos em baixa luz.",
    "A conectividade 5G é rápida e estável.",
    "Não consegui encontrar uma capinha que sirva.",
    "O sistema operacional é leve e eficiente.",
    "A função de carregamento sem fio é super prática.",
    "As cores da tela são vibrantes e vívidas.",
    "O peso é ideal, não é muito pesado.",
    "Estou adorando as funcionalidades de câmera.",
    "A proteção de tela é resistente, não arranha facilmente.",
    "O smartphone se destaca em comparação com outros.",
    "Fiquei decepcionado com a qualidade do suporte técnico.",
    "O armazenamento é expansível, ótima opção.",
    "A personalização de temas é muito legal.",
    "Os jogos rodam perfeitamente, sem queda de frames.",
    "O GPS é preciso e rápido na localização.",
    "Os anúncios de software são um pouco invasivos.",
    "O design é um pouco escorregadio, preciso de capinha.",
    "O modo retrato da câmera é um destaque.",
    "A experiência de uso é fluida e sem interrupções.",
    "As funcionalidades de privacidade são excelentes.",
    "O Bluetooth conecta rápido a outros dispositivos.",
    "A qualidade das chamadas é cristalina.",
    "O smartphone não é resistente à água, isso é um ponto negativo.",
    "A tela é sensível ao toque e responde rapidamente.",
    "Os recursos de acessibilidade são muito bons.",
    "As cores disponíveis são bem variadas.",
    "O smartphone se integra bem com outros dispositivos.",
    "O carregamento rápido faz toda a diferença.",
    "Não tem a opção de rádio FM, o que eu gostaria.",
    "Os atalhos são muito úteis e práticos.",
    "O modo de economia de bateria é eficaz.",
    "Estou bastante satisfeito com a compra."
]

# Lista de palavras descartáveis
palavras_descartaveis = [
    "a", "o", "as", "os", "um", "uma", "para", "de", "do", "da", 
    "em", "no", "na", "com", "que", "por", "e", "ou", "mas", 
    "se", "não", "é", "um", "na", "ao", "aos", "das", "dos", 
    "como", "mais", "menos", "sobre", "até", "entre", "dentro", 
    "fora", "sempre", "também", "muito", "pouco", "cada", 
    "todos", "alguns", "quem", "cujo", "este", "essa", "isto", 
    "aquilo", "meu", "tua", "seu", "sua", "minha", "nos", 
    "nós", "eles", "elas", "você", "vocês"
]

# CRIAÇÃO DO ARQUIVO SUJO.TXT
with open("sujo.txt", "w+", encoding = "utf-8") as arq:
    arq.writelines(comentarios)


# Colocando o conteudo do arquivo sujo em uma variável
conteudo = ""
if os.path.exists("sujo.txt"):
    with open("sujo.txt", "r+", encoding= "utf-8") as arq:
        conteudo = arq.read()
    arq.close()

# Removendo as palavras descartáveis
for word in palavras_descartaveis:
    conteudo = conteudo.replace(word, "")

# Copiando as informações no arquivo limpo.
with open("limpo.txt", "w+", encoding= "utf-8") as arq:
    arq.writelines(conteudo)

#CONTANDO A PALAVRA COM MAIS OCORRÊNCIAS
# Separar em as palavras em uma lista de palavras
palavras_limpo = conteudo.split()
# Criar um dicionário para armazenar a contagem das palavras
contagem_palavras = {}
# Contar as palavras usando um for
for word in palavras_limpo:
    if word in contagem_palavras:
        contagem_palavras[word] =+ 1
    else:
        contagem_palavras[word] = 1
# Identificar a palavra que mais aparece e quantas vezes aparece
palavraFreq = max(contagem_palavras, key=contagem_palavras.get)
Freq = contagem_palavras[palavraFreq]
# Exibir a palavra que mais aparece
print(f"A Palavra que mais aparece no arquivo é a palavra: '{palavraFreq}', ela aparece '{Freq}' vezes.")