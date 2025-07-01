import os

restaurantes = [{'nome': 'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo':False}]
                


def exibir_nome_do_programa():
    """
    Essa função exibe o nome do programa
    """
    print('Sabor Express\n')

def exibir_opcoes():
    """

    Função para exibição das opções disponíveis no menu principal

    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Exibe a mensagem de finalização do aplicativo
    """
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    """
    Função que ao apertar uma tecla retorna ao menu de opções
    Outputs: 
    -Retorna ao menu principal
    """
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()    
    
def opcao_invalida():
    """
    Essa função aparece quando o usuário seleciona uma opção inválida e retorna ao menu principal
    
    Outputs:
    -Retorna ao menu principal
    
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """
    Exibe o subtítulo na tela
    Inputs:
    -texto: str - O texto do subtítulo
    """
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    -Nome do restaurante
    -Categoria

    Output:
    -Adiciona um novo restaurante à lista de restaurantes
    
"""
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,
                             'categoria':categoria,
                             'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Exibe a lista dos restaurante cadastrados
    
    Outputs:
    -Exibe a lista de restaurantes na tela
    
    """
    exibir_subtitulo('Listando restaurantes')
    

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'} ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante ['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Altera o estado ativo/desativado de um restaurante

    Outputs:
    -Exibe mensagem indicando o sucesso da operação
    """
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativo com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Solicita e executa a opção escolhida pelo usuário

    Outputs:
    -Executa a opção escolhida pelo usuário
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()     
    except:
        opcao_invalida()
        
def main():
    """Função principal que inicia o programa
    
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
        main()