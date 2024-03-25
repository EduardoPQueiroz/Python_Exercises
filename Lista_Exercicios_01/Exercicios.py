import os 
os.system("cls")

print("1. lê valor maior")
print("2. pode votar?")
print("3. valida senha")
print("4. calcula valor das maçãs")
print("5. ordem crescente")
print("6. calcula peso ideal")
print("7. numero de lados polígono regular")
print("8. é polígono ou não é ")
print("9. maior entre três")
print("10. lados dos triângulos ")
print("11. ângulos dos triângulos ")
print("12. Verifica os primos.")
print("13.Verifica Notas.")
print("Digite '0' para sair")

opcao = ''
while opcao != "exit":

    opcao = int(input("escolha a sua opção (0-13): "))

    match opcao:
        case 1:
            primeiroNumero = float(input("insira o primeiro número: "))
            segundoNumero = float(input("insira o segundo número: "))

            if primeiroNumero == segundoNumero:
                print("Números inválidos")
            else:
                if primeiroNumero > segundoNumero:
                    print(primeiroNumero)
                else:
                    print(segundoNumero)
            continue

        case 2:
            anoNascimento = int(input("Insira o ano em que você nasceu: "))
            idade = 2024 - anoNascimento
            if idade < 16:
                print("Você não pode votar nesse ano.")
            elif idade > 18:
                print("Você é obrigado a votar a esse ano.")
            else:
                print("Você pode votar esse ano")
            continue

        case 3:
            senhaCerta = int(1234)
            senha = int(input("Insira a senha: "))

            if senha != senhaCerta:
                print("ACESSO INVÁLIDO")
            else:
                print("ACESSO VÁLIDO")
            continue
        case 4:
            quantidadeMacas = int(input("Insira a quantidade de maçãs compradas: "))
            if quantidadeMacas < 12:
                valor = 0.30 * quantidadeMacas
                print("O Valor da sua compra é:", valor)
            else:
                valor = 0.25 * quantidadeMacas
                print("O Valor da sua compra é:", valor)
            continue
        case 5:
            primeiroValor = int(input("Insira o primeiro valor: "))
            segundoValor = int(input("Insira o segundo valor: "))
            terceiroValor = int(input("Insira o terceiro valor: "))

            if primeiroValor < segundoValor and segundoValor < terceiroValor:
                print("a sequência é: ", primeiroValor, segundoValor, terceiroValor)
            elif primeiroValor < terceiroValor and terceiroValor < segundoValor:
                print("a sequência é: ", primeiroValor, terceiroValor, segundoValor)
            elif segundoValor < primeiroValor and primeiroValor < terceiroValor:
                print("a sequência é: ", segundoValor, primeiroValor, terceiroValor)
            elif segundoValor < terceiroValor and terceiroValor < primeiroValor:
                print("a sequência é: ", segundoValor, terceiroValor, primeiroValor)
            elif terceiroValor < primeiroValor and primeiroValor < segundoValor:
                print("a sequência é: ", terceiroValor, primeiroValor, segundoValor)
            else:
                print("a sequência é: ", terceiroValor, segundoValor, primeiroValor)
            continue
        case 6:
            altura = float(input("Insira sua altura: "))
            sexo = int(input("Insira seu sexo, sendo 1 = F e 2 = M: "))
            if sexo == 2:
                pesoIdeal = (72.7 * altura) - 58
                print("Seu peso ideal é: ", pesoIdeal)
            elif sexo == 1:
                pesoIdeal = (62.1 * altura) - 44.7
                print("Seu peso ideal é: ", pesoIdeal)
            else:
                print("Insira um sexo válido.")
            continue
        case 7:
            numeroLados = int(input("insira a quantidade de lados do polígono: "))
            cmLados = int(input("inisira o tamanho dos lados: "))
            
            if numeroLados == 3:
                print("Triângulo")
                area = (cmLados * cmLados) / 2
                print("a área do triângulo é: ", area)
            elif numeroLados == 4:
                print("Quadrado")
                area = (cmLados * cmLados)
                print("a área do quadrado é: ", area)
            elif numeroLados == 5:
                print("Pentágono")
            else:
                print("Inválido!")
            continue
        case 8:
            numeroLados = int(input("insira a quantidade de lados do polígono: "))
            cmLados = int(input("inisira o tamanho dos lados: "))
            
            if numeroLados < 3:
                print("NÃO É UM POLÍGONO")
            elif numeroLados > 5:
                print("POLÍGONO NÃO IDENTIFICADO")
            else:
                if numeroLados == 3:
                    print("Triângulo")
                    area = (cmLados * cmLados) / 2
                    print("a área do triângulo é: ", area)
                elif numeroLados == 4:
                    print("Quadrado")
                    area = (cmLados * cmLados)
                    print("a área do quadrado é: ", area)
                else:
                    print("Pentágono")
            continue
        case 9:
            primeiroValor = float(input("Insira o primeiro Valor: "))
            segundoValor = float(input("Insira o segundo Valor: "))
            terceiroValor = float(input("Insira o terceiro Valor: "))

            if primeiroValor > segundoValor and segundoValor > terceiroValor:
                print("O maior valor inserido foi: ", primeiroValor)
            elif primeiroValor > terceiroValor and terceiroValor > segundoValor:
                print("O maior valor inserido foi: ", primeiroValor)
            elif segundoValor > primeiroValor and primeiroValor > terceiroValor:
                print("O maior valor inserido foi: ", segundoValor)
            elif segundoValor > terceiroValor and terceiroValor > primeiroValor:
                print("O maior valor inserido foi: ", segundoValor)
            elif terceiroValor > primeiroValor and primeiroValor > segundoValor:
                print("O maior valor inserido foi: ", terceiroValor)
            else:
                print("O maior valor inserido foi: ", terceiroValor)
            continue

        case 10:
            primeiroLado = int(input("insira o primeiro lado do triângulo: "))
            segundoLado = int(input("insira o segundo lado do triângulo: "))
            terceiroLado = int(input("insira o terceiro lado do triângulo: "))

            if primeiroLado == segundoLado and primeiroLado == terceiroLado:
                print("triângulo equilátero")
            elif primeiroLado == segundoLado or primeiroLado == terceiroLado or segundoLado == terceiroLado:
                print("Triângulo Isóscele")
            else:
                print("Triângulo escaleno")
            continue
        case 11:
            primeiroAngulo = float(input("Insira o valor do primeiro Ângulo: "))
            segundoAngulo = float(input("Insira o valor do segundo Ângulo: "))
            terceiroAngulo = float(input("Insira o valor do terceiro Ângulo: "))
            
            if primeiroAngulo < 90 and segundoAngulo < 90 and terceiroAngulo < 90:
                print("Isso é um Triângulo Acutângulo: ")
            elif primeiroAngulo > 90 and segundoAngulo < 90 and terceiroAngulo < 90 or primeiroAngulo < 90 and segundoAngulo > 90 and terceiroAngulo < 90 or primeiroAngulo < 90 and segundoAngulo < 90 and terceiroAngulo > 90:
                print("Isso é um Triângulo Obtusângulo.")
            elif primeiroAngulo == 90 and segundoAngulo < 90 and terceiroAngulo < 90 or segundoAngulo == 90 and primeiroAngulo < 90 and terceiroAngulo < 90 or terceiroAngulo == 90 and primeiroAngulo and segundoAngulo < 90:
                print("Isso é um Triângulo Retângulo.")
            else:
                print("Os angulos inseridos não formam um triângulo") 
            continue

        case 12:
            number = int(input("Insira um número: "))
            if number == 1:
                print("O NÚMERO 1 NÃO É CONSIDERADO PRIMO.")
            elif number == 2:
                print("O Número inserido é primo!")
            elif number == 3:
                print("O Número inserido é primo!")
            else:
                count = 1
                while count < number -1:
                    if number % 2 == 0 or number % 3 == 0:
                        print("O número inserido não é primo!")
                        break
                    else:
                        print("O Número inserido é primo!")
                        break
            continue    
        case 13:
            mediaSala = 0
            acimaMedia = 0
            for i in range (1, 11, 1):
                verificaNota = 0
                while verificaNota == 0:
                    alunoAtual = int(i)
                    nota1 = float(input(f"Insira a primeira nota do aluno {i}: "))
                    nota2 = float(input(f"Insira a segunda nota do aluno {i}: "))
                    nota3 = float(input(f"Insira a terceira nota do aluno {i}: "))
                    print("Nota Adquirida!\n")
                    if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota1 > 10 or nota2 > 10 or nota3 > 10:
                        print("A NOTA INSERIDA NÃO É VÁLIDA!")
                        continue
                    else: 
                        verificaNota = 1   
                        if nota1 < nota2 and nota1 < nota3:
                            nota1 = 0
                        elif nota2 < nota3:
                            nota2 = 0
                        else:
                            nota3 = 0
                        mediaAlunoAtual = (nota1 + nota2 + nota3) / 2
                        if mediaAlunoAtual >= 9:
                            acimaMedia = acimaMedia + 1
                        mediaSala = mediaSala + mediaAlunoAtual

            mediaSala = mediaSala / 10
            print(f"\n A Média da sala é igual a: {mediaSala}!")
            print(f"{acimaMedia} alunos tiveram média 9 ou superior!")

            continue
        case 0:
            break

        case _:
            print("-Opção inválida-")
            
        
