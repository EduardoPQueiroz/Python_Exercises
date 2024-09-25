import os
os.system("cls")

# Lista de comentários sobre um smartphone
comentarios = [
    "Ótimo smartphone, recomendo!\n",
    "A câmera é incrível, tira fotos nítidas.\n",
    "Bateria dura o dia todo, muito satisfeita.\n",
    "O desempenho é rápido, sem travamentos.\n",
    "Design elegante e moderno, amei!\n",
    "A tela é muito boa, ótima para assistir vídeos.\n",
    "Chegou rápido, muito feliz com a entrega.\n",
    "A qualidade do som é excelente.\n",
    "A interface é intuitiva e fácil de usar.\n",
    "O preço vale a pena pela qualidade.\n",
    "Fiquei impressionado com a durabilidade da bateria.\n",
    "Não gosto do tamanho, é um pouco grande para mim.\n",
    "O suporte ao cliente foi ótimo, ajudaram rapidamente.\n",
    "Apenas o carregador poderia ser mais rápido.\n",
    "As atualizações são frequentes e melhoram o desempenho.\n",
    "Os aplicativos rodam muito bem, sem lags.\n",
    "A cor do aparelho é linda, exatamente como na foto.\n",
    "A segurança biométrica é rápida e precisa.\n",
    "A memória interna é suficiente para meus aplicativos.\n",
    "O smartphone esquentou um pouco durante jogos intensos.\n",
    "A qualidade de construção é robusta, parece durável.\n",
    "O reconhecimento facial é prático e funciona bem.\n",
    "As configurações são fáceis de ajustar.\n",
    "Faltam alguns recursos que eu gostaria de ter.\n",
    "A experiência geral é muito positiva.\n",
    "O modo noturno da câmera é ótimo para fotos em baixa luz.\n",
    "A conectividade 5G é rápida e estável.\n",
    "Não consegui encontrar uma capinha que sirva.\n",
    "O sistema operacional é leve e eficiente.\n",
    "A função de carregamento sem fio é super prática.\n",
    "As cores da tela são vibrantes e vívidas.\n",
    "O peso é ideal, não é muito pesado.\n",
    "Estou adorando as funcionalidades de câmera.\n",
    "A proteção de tela é resistente, não arranha facilmente.\n",
    "O smartphone se destaca em comparação com outros.\n",
    "Fiquei decepcionado com a qualidade do suporte técnico.\n",
    "O armazenamento é expansível, ótima opção.\n",
    "A personalização de temas é muito legal.\n",
    "Os jogos rodam perfeitamente, sem queda de frames.\n",
    "O GPS é preciso e rápido na localização.\n",
    "Os anúncios de software são um pouco invasivos.\n",
    "O design é um pouco escorregadio, preciso de capinha.\n",
    "O modo retrato da câmera é um destaque.\n",
    "A experiência de uso é fluida e sem interrupções.\n",
    "As funcionalidades de privacidade são excelentes.\n",
    "O Bluetooth conecta rápido a outros dispositivos.\n",
    "A qualidade das chamadas é cristalina.\n",
    "O smartphone não é resistente à água, isso é um ponto negativo.\n",
    "A tela é sensível ao toque e responde rapidamente.\n",
    "Os recursos de acessibilidade são muito bons.\n",
    "As cores disponíveis são bem variadas.\n",
    "O smartphone se integra bem com outros dispositivos.\n",
    "O carregamento rápido faz toda a diferença.\n",
    "Não tem a opção de rádio FM, o que eu gostaria.\n",
    "Os atalhos são muito úteis e práticos.\n",
    "O modo de economia de bateria é eficaz.\n",
    "Estou bastante satisfeito com a compra.\n"
]

# Lista de palavras descartáveis
palavras_descartaveis = [
    "a\n", "o\n", "as\n", "os\n", "um\n", "uma\n", "para\n", "de\n", "do\n", "da\n", 
    "em\n", "no\n", "na\n", "com\n", "que\n", "por\n", "e\n", "ou\n", "mas\n", 
    "se\n", "não\n", "é\n", "um\n", "na\n", "ao\n", "aos\n", "das\n", "dos\n", 
    "como\n", "mais\n", "menos\n", "sobre\n", "até\n", "entre\n", "dentro\n", 
    "fora\n", "sempre\n", "também\n", "muito\n", "pouco\n", "cada\n", 
    "todos\n", "alguns\n", "quem\n", "cujo\n", "este\n", "essa\n", "isto\n", 
    "aquilo\n", "meu\n", "tua\n", "seu\n", "sua\n", "minha\n", "nos\n", 
    "nós\n", "eles\n", "elas\n", "você\n", "vocês\n"
]

with open("sujo.txt", "w+", encoding = "utf-8") as arq:
    arq.writelines(comentarios)
