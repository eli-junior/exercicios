"""
Objetivo
Desenvolver um programa em Python que determine se um número fornecido pelo usuário é um número primo ou não.

Regras e Requisitos
Entrada de Dados: O programa deve solicitar ao usuário que insira um número inteiro positivo.
Validação de Entrada: O programa deve verificar se a entrada é válida (um número inteiro positivo). Se a entrada for inválida (por exemplo, uma string, um número negativo ou zero), o programa deve solicitar ao usuário que forneça uma nova entrada válida.

Definição de Número Primo: Um número primo é um número inteiro maior que 1 que tem exatamente dois divisores distintos: 1 e ele mesmo. O programa deve usar essa definição para determinar se o número é primo.
Cálculo e Otimização: O programa não deve apenas verificar cada número até o número de entrada para determinar se é primo. Ele deve usar uma abordagem otimizada, como verificar divisores apenas até a raiz quadrada do número de entrada, pois se um número tem um divisor maior que sua raiz quadrada, então ele necessariamente terá um divisor menor que ela.
Saída de Dados: O programa deve imprimir uma mensagem indicando se o número de entrada é um número primo ou não.
Re-execução Opcional: Após fornecer o resultado, o programa pode opcionalmente perguntar ao usuário se ele deseja testar outro número, permitindo múltiplas execuções sem necessidade de reiniciar o programa.

Exemplo de Execução
O usuário insere o número 29.
O programa verifica se 29 é um número primo.
Como 29 é um número primo (não tem divisores além de 1 e ele mesmo), o programa imprime: "29 é um número primo."
Se o usuário inserir 28, o programa imprime: "28 não é um número primo." pois 28 pode ser dividido por 1, 2, 4, 7, 14, e 28.

Dicas para Implementação: 
Use loops para verificar a primalidade.
Lembre-se de que 2 é o único número primo par.
A otimização da verificação até a raiz quadrada pode significativamente reduzir o tempo de execução para números grandes.
Este desafio é uma excelente oportunidade para praticar habilidades de programação em Python, entender melhor os números primos e explorar técnicas de otimização de algoritmos.

Extra:
Crie um parâmetro adicional para que, quando passado, o programa retorne uma lista com todos os números primos até o número informado.
ex: funcao_primo(100, listar_primos=True) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
players = ["Leo", "Dea", "Victor", "Jr"]

import pytest


def valida_entrada(entrada):
    if not isinstance(entrada, int) or entrada <= 0:
            raise ValueError("O valor de entrada precisa ser um número inteiro positivo")
    return True


def calcula_divisores(entrada):
    divisores = []
    for i in range(1, entrada + 1):
        if entrada % i == 0:
            divisores.append(i)
    return divisores


def verifica_resultado(divisores):
    valor = divisores[-1]
    if len(divisores) == 1:
        return "1 é 1."
    if len(divisores) == 2:
        return f"{valor} é um número primo."
    else:
        d = divisores[:]
        ultimos = d.pop()
        d = str(d)[1:-1]
        return f"{valor} não é um número primo. pois {valor} pode ser dividido por {d} e {ultimos}."


############### TESTES ####################

def test_valida_entrada_recebendo_string_levanta_valueerror():
        with pytest.raises(ValueError):
                assert valida_entrada("23")


def test_valida_entrada_passando_zero_levanta_valueerror():
        with pytest.raises(ValueError):
                assert valida_entrada(0) 


def test_valida_entrada_passando_valor_negativo_levanta_valueerror():
        with pytest.raises(ValueError):
                assert valida_entrada(-1) 


def test_valida_entrada_passando_valor_um_retorna_true():
        assert valida_entrada(1) is True


def test_valida_entrada_passando_valor_oitenta_e_cinco_retorna_true():
        assert valida_entrada(85) is True


def test_calcula_divisores_passando_dois_retorna_lista_com_1_e_2():
        assert calcula_divisores(2) == [1, 2]


def test_calcula_divisores_passando_tres_retorna_lista_com_1_e_3():
        assert calcula_divisores(3) == [1, 3]


def test_calcula_divisores_passando_quatro_retorna_lista_com_1_2_e_4():
        assert calcula_divisores(4) == [1, 2, 4]
    

def test_calcula_divisores_passando_dez_retorna_lista_com_1_2_5_e_10():
    assert calcula_divisores(10) == [1, 2, 5, 10]


def test_calcula_divisores_passando_cem_retorna_lista_com_divisores():
    assert calcula_divisores(30) == [1, 2, 3, 5, 6, 10, 15, 30]


def test_verifica_resultado_passando_29_retorna_que_e_primo():
        assert verifica_resultado([1, 29]) == "29 é um número primo."


def test_verifica_resultado_passando_5_retorna_que_e_primo():
    assert verifica_resultado([1, 5]) == "5 é um número primo."


def test_verifica_resultado_passando_28_retorna_que_nao_e_primo():
    assert verifica_resultado([1, 2, 4, 7, 14, 28]) == "28 não é um número primo. pois 28 pode ser dividido por 1, 2, 4, 7, 14 e 28."


def test_verifica_resultado_passando_8_retorna_que_nao_e_primo():
    assert verifica_resultado([1, 2, 4, 8]) == "8 não é um número primo. pois 8 pode ser dividido por 1, 2, 4 e 8."


if __name__ == "__main__":
    # pytest.main(['-svvrP', __file__])
    entrada = int(input("digite um número positivo: "))
    valida_entrada(entrada)
    divisores = calcula_divisores(entrada)
    print(verifica_resultado(divisores))