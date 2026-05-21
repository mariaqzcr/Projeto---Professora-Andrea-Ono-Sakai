# =============================================================
# main.py — Ponto de entrada do Gerenciador de Locadora
# Responsabilidade: exibir o menu principal e direcionar
#                   as escolhas do usuário para as funções
#                   dos módulos correspondentes.
# =============================================================

import dados
from filmes import (cadastrar_filme, listar_catalogo,
                    registrar_aluguel, registrar_devolucao,
                    ver_historico_devolucoes, buscar_por_titulo,
                    listar_disponiveis_por_genero)


def popular_catalogo():
    """
    Pré-cadastra um filme de cada gênero disponível na tupla GENEROS.
    É chamada uma única vez ao iniciar o programa, antes do menu.
    Cada filme é um dicionário adicionado ao catálogo e à fila de reservas.
    """
    # Lista de tuplas: (titulo, genero, ano)
    # Um filme representativo para cada gênero da tupla GENEROS
    filmes_iniciais = [
        ('Mad Max: Estrada da Fúria',       'Ação',              2015),
        ('Se Beber, Não Case!',             'Comédia',           2009),
        ('Forrest Gump',                    'Drama',             1994),
        ('O Iluminado',                     'Terror',            1980),
        ('Interestelar',                    'Ficção Científica', 2014),
        ('Divertida Mente',                 'Animação',          2015),
        ('Free Solo',                       'Documentário',      2018),
        ('Orgulho e Preconceito',           'Romance',           2005),
    ]

    for titulo, genero, ano in filmes_iniciais:
        filme = {
            'id':          dados.gerar_id(),
            'titulo':      titulo,
            'genero':      genero,
            'ano':         ano,
            'status':      dados.STATUS_FILME[0],   # 'Disponível'
            'alugado_por': None,
        }
        dados.catalogo.append(filme)        # entra na lista geral
        dados.fila_reservas.append(filme)   # entra no final da fila (FIFO)


def exibir_menu():
    """Imprime as opções do menu principal na tela."""
    print()
    print('╔══════════════════════════════════════╗')
    print('║     LOCADORA DE FILMES — MENU        ║')
    print('╠══════════════════════════════════════╣')
    print('║  1. Cadastrar filme                  ║')
    print('║  2. Ver catálogo completo            ║')
    print('║  3. Registrar aluguel (fila FIFO)    ║')
    print('║  4. Registrar devolução              ║')
    print('║  5. Histórico de devoluções (LIFO)   ║')
    print('║  6. Buscar filme por título  [bônus] ║')
    print('║  7. Disponíveis por gênero   [bônus] ║')
    print('║  0. Sair                             ║')
    print('╚══════════════════════════════════════╝')


def main():
    """
    Função principal: loop while True que mantém o programa rodando.
    Lê a opção do usuário e chama a função correspondente via if/elif.
    O loop encerra com break quando o usuário digita 0.
    """
    print('\n  Bem-vindo ao Gerenciador de Locadora de Filmes!')

    # Popula o catalogo com um filme de cada genero ao iniciar
    popular_catalogo()
    print('  Catalogo inicial carregado: 8 filmes disponiveis.')

    while True:
        exibir_menu()

        try:
            opcao = int(input('  Escolha uma opção: '))
        except ValueError:
            print('  ✗ Digite apenas o número da opção.')
            continue

        if opcao == 1:
            cadastrar_filme()
        elif opcao == 2:
            listar_catalogo()
        elif opcao == 3:
            registrar_aluguel()
        elif opcao == 4:
            registrar_devolucao()
        elif opcao == 5:
            ver_historico_devolucoes()
        elif opcao == 6:
            buscar_por_titulo()
        elif opcao == 7:
            listar_disponiveis_por_genero()
        elif opcao == 0:
            print('\n  Encerrando o sistema. Até logo!\n')
            break   # encerra o loop while True
        else:
            print('  ✗ Opção inválida. Escolha entre 0 e 7.')


# Garante que main() só é chamado quando o arquivo é executado diretamente
if __name__ == '__main__':
    main()
