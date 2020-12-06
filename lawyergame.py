name = input("Qual o seu nome? ")
print(name, "Bem-vindo(a) ao LawyersGame!")

status = input(
    "Antes de começarmos, precisamos verificar se você está pronto(a). Qual o nome dado à Suprema Corte brasileira? "
).lower()
health = 10

if status == "supremo tribunal federal":
    print("Correto! Você está!")

    whants_to_play = input("Você quer jogar? ").lower()
    if whants_to_play == "sim":
        print(
            "As regras são simples. Você começará com",
            health,
            "vidas. Seu objetivo é analisar o caso concreto e responder corretamente.",
        )
        print("Entendidos? Vamos lá!")

        contestacao = input(
            "Primeira escolha... Sua cliente é ré em uma ação de cobrança por não ter pago a totalidade de uma contrato de prestação de serviço. Ela, ao te procurar, diz que já foi citada e não apresentou contestação, mas gostaria de pedir danos morais junto a sua defesa. O que você deve fazer? (apresentar contestação/apresentar reconvenção/apresentar contestação e reconvenção juntas)? "
        ).lower()
        if contestacao == "apresentar contestação":
            print(
                "Os danos morais solicitados pela cliente não podem ser apresentados em contestação. Esse é um erro grave e por isso você perdeu 5 vidas"
            )
            health -= 5

        if contestacao == "apresentar contestação e reconvenção juntas":
            print(
                "Hum... Funciona. Mas você acabou trabalhando demais, já que só a reconvenção seria o suficiente. Menos 3 vidas para você - para compensar o esforço"
            )
            health -= 3

        elif contestacao == "apresentar reconvenção":
            print("Escolha correta! Vamos prosseguir!")

        rese = input(
            "Para o indeferimento de requerimento para reconhecimento de prescrição da pretenção punitiva estatal antes do oferecimento de alegações finais, qual o recurso adequado? (apelação/embargos/rese)"
        ).lower()
        if rese == "apelação":
            print(
                "Sinto muito, mas a resposta está errada. Você acabou de perder mais 5 vidas"
            )
            health -= 3

            if health <= 0:
                print("Hum... Parece que você acabou de perder!")

        if rese == "embargos":
            print(
                "Sinto muito, mas a resposta está errada. Você acabou de perder mais 7 vidas"
            )
            health -= 3
            if health <= 0:
                print("Hum... Parece que você acabou de perder!")

        elif rese == "rese":
            print("Correto!")

        principios = input(
            "Última questão! Dos princípios listados, qual não é aplicado no Direito Trabalhista? (princípio da proteção/primazia da realidade/princípio da anterioridade) "
        )

        if principios == "princípio da proteção":
            print("Bom, talvez você tenha mais sorte na próxima")

        if principios == "primazia da realidade":
            print("Bom, talvez você tenha mais sorte na próxima")

        elif principios == "princípio da anterioridade":
            print("Parabéns! Você ganhou!")

    else:
        print("Tudo bem! Nos vemos por aí")

elif status == "stf":
    print("Hum... Eu tenho quase certeza que não é esse. Tente por extenso da próxima!")

else:
    print("Hum... Acho melhor você tentar outra hora")