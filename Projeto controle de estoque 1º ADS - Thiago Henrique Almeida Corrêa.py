import os.path, mmap



print("######### LOJA DE GAMES #########\n\n")
plat='0'
menu = 0
categ = 0
global quest
quest = '1'
menu_laço='0'


def menu_categoria():  # FUNÇÃO PARA ESCOLHER A CATEGORIA DO PRODUTO
    global categ
    print("Escolha a categoria do produto.\n")
    print("Digite '1' para selecionar a categoria jogos: ")
    print("Digite '2' para selecionar a categoria console/hardware: ")
    print("Digite '3' para selecionar a categoria periféricos: ")
    categ = input()


def menu_da_loja():  # FUNÇÃO PRA USAR OS MENUS NOS LAÇOS
    global menu
    print("Digite '1' para consultar o estoque de um produto. ")
    print("Digite '2' para registrar um produto no estoque. ")
    print("Digite '3' para retirar um produto do estoque. ")
    print("Digite '9' para retornar ao menu inicial.\n")
    menu = input()


print("BEM VINDO AO SOFTWARE DE CONTROLE DE ESTOQUE, UTILIZE OS NUMEROS de 1 a 4 PARA NAVEGAR PELAS OPÇÕES OU 9 PARA SAIR!\n\n")
while plat is not '9':
    quest='1'
    print("Escolha qual plataforma que você deseja registrar/consultar.\nDigite 1 para playstation.\nDigite 2 para xbox.\nDigite 3 para nintendo.\nDigite 4 para pc.\nDigite 5 para outros produtos. \nDigite 9 para sair do programa. ")
    plat = input()
    if plat == '1':  # LAÇO DO PLAYSTATION
       print("====== SONY PLAYSTATION====== \n")
       menu_da_loja()
       while menu is not '9':
            if menu == '1':  # CONSULTA
               while quest == '1':
                  menu_categoria()
                  if categ == '1':  # CATEGORIA
                      consult = input("Digite o nome ou código do produto a ser consultado: ")
                      consult = consult.lower()
                      arq = open("jogos_play.txt", 'r')
                      for linha in arq:
                          linha = linha.rstrip()
                          search = consult
                          if consult in linha:
                              print(linha)
                      print("Consulta completa.")
                  if categ == '2':  # CATEGORIA
                      consult = input("Digite o nome ou código do produto a ser consultado: ")
                      consult = consult.lower()
                      arq = open("consoles_play.txt", 'r')
                      for linha in arq:
                          linha = linha.rstrip()
                          search = consult
                          if consult in linha:
                              print(linha)
                  if categ == '3':  # CATEGORIA
                      consult = input("Digite o nome ou código do produto a ser consultado: ")
                      consult = consult.lower()
                      arq = open("peri_play.txt", 'r')
                      for linha in arq:
                          linha = linha.rstrip()
                          search = consult
                          if consult in linha:
                              print(linha)
                  quest = input("\nDeseja consultar outro produto? \nDigite 1 para consultar outro.\nDigite 2 para sair do menu de consulta:\n ")
               break
            if menu == '2':  # REGISTRO
                while quest == '1':
                    menu_categoria()
                    if categ == '1':
                        regi_play_nome = str(input("Digite o nome do produto: "))
                        regi_play_nome = regi_play_nome.lower()
                        regi_play_preço = float(input("Digite o preço do produto: "))
                        regi_play_cod = int(input("Digite o código do produto: "))
                        if os.path.exists("jogos_play.txt"):
                            arq = open("jogos_play.txt", "a")
                            arq.write(
                                "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                            arq.close()
                        else:
                            arq = open("jogos_play.txt", "w")
                            arq.write(
                                "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                    if categ == '2':
                        regi_play_nome = str(input("Digite o nome do produto: "))
                        regi_play_nome = regi_play_nome.lower()
                        regi_play_preço = float(input("Digite o preço do produto: "))
                        regi_play_cod = int(input("Digite o código do produto: "))
                        if os.path.exists("consoles_play.txt"):
                            arq = open("consoles_play.txt", "a")
                            arq.write(
                                "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                        else:
                            arq = open("consoles_play.txt", "w")
                            arq.write(
                                "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                    if categ == '3':
                        regi_play_nome = str(input("Digite o nome do produto: "))
                        regi_play_nome = regi_play_nome.lower()
                        regi_play_preço = float(input("Digite o preço do produto: "))
                        regi_play_cod = int(input("Digite o código do produto: "))
                        if os.path.exists("peri_play.txt"):
                            arq = open("peri_play.txt", "a")
                            arq.write(
                                "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                        else:
                            arq = open("peri_play.txt", "w")
                            arq.write(
                                "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                    quest = (input("\nDeseja cadastrar outro produto?\nDigite 1 para sim\nDigite 2 para não:\n"))
                break
            if menu == '3': #RETIRAR
               while quest=='1':
                   menu_categoria()
                   if categ == '1':  # CATEGORIA
                       consult = input("Digite o nome ou código do produto a ser retirado: ")
                       consult=consult.lower()
                       with open("jogos_play.txt",'r') as arq:
                           lines=arq.readlines()
                           arq.close()
                           arq=open("jogos_play.txt",'w')
                           for line in lines:
                               if consult not in line +"\n":
                                   arq.write(line)
                           print("Produto retirado com sucesso! ")
                   if categ == '2':  # CATEGORIA
                       consult = input("Digite o nome ou código do produto a ser retirado: ")
                       consult=consult.lower()
                       with open("consoles_play.txt",'r') as arq:
                           lines=arq.readlines()
                           arq.close()
                           arq=open("consoles_play.txt",'w')
                           for line in lines:
                               if consult not in line +"\n":
                                   arq.write(line)
                           print("Produto retirado com sucesso! ")
                   if categ == '3':  # CATEGORIA
                       consult = input("Digite o nome ou código do produto a ser retirado: ")
                       consult=consult.lower()
                       with open("peri_play.txt",'r') as arq:
                           lines=arq.readlines()
                           arq.close()
                           arq=open("peri_play.txt",'w')
                           for line in lines:
                               if consult not in line +"\n":
                                   arq.write(line)
                           print("Produto retirado com sucesso! ")

                   quest = input("\nDeseja retirar outro produto? \nDigite 1 para retirar outro.\nDigite 2 para sair.\n ")
               break

    if plat == '2':  # LAÇO DO XBOX
                print("====== MICROSOFT XBOX ======\n")
                menu_da_loja()
                while menu is not '9':
                    if menu == '1':  # CONSULTA
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("jogos_xbox.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                                print("Consulta completa.")
                            if categ == '2':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("consoles_xbox.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                            if categ == '3':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("peri_xbox.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                            quest = input(
                                "\nDeseja consultar outro produto? \nDigite 1 para consultar outro.\nDigite 2 para sair do menu de consulta:\n ")
                        break
                    if menu == '2':  # REGISTRO
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("jogos_xbox.txt"):
                                    arq = open("jogos_xbox.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                    arq.close()
                                else:
                                    arq = open("jogos_xbox.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            if categ == '2':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("consoles_xbox.txt"):
                                    arq = open("consoles_xbox.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                else:
                                    arq = open("consoles_xbox.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            if categ == '3':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("peri_xbox.txt"):
                                    arq = open("peri_xbox.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                else:
                                    arq = open("peri_xbox.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            quest = (
                                input("\nDeseja cadastrar outro produto?\nDigite 1 para sim\nDigite 2 para não:\n"))
                        break
                    if menu == '3':  # RETIRAR
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("jogos_xbox.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("jogos_xbox.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")
                            if categ == '2':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("consoles_xbox.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("consoles_xbox.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")
                            if categ == '3':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("peri_xbox.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("peri_xbox.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")

                            quest = input(
                                "\nDeseja retirar outro produto? \nDigite 1 para retirar outro.\nDigite 2 para sair.\n ")
                        break

    if plat == '3':  # LAÇO DA NINTENDO
                print("====== NINTENDO ======\n")
                menu_da_loja()
                while menu is not '9':
                    if menu == '1':  # CONSULTA
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("jogos_nintendo.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                                print("Consulta completa.")
                            if categ == '2':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("consoles_nintendo.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                            if categ == '3':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("peri_nintendo.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                            quest = input(
                                "\nDeseja consultar outro produto? \nDigite 1 para consultar outro.\nDigite 2 para sair do menu de consulta:\n ")
                        break
                    if menu == '2':  # REGISTRO
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("jogos_nintendo.txt"):
                                    arq = open("jogos_nintendo.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                    arq.close()
                                else:
                                    arq = open("jogos_nintendo.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            if categ == '2':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("consoles_nintendo.txt"):
                                    arq = open("consoles_nintendo.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                else:
                                    arq = open("consoles_nintendo.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            if categ == '3':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("peri_nintendo.txt"):
                                    arq = open("peri_nintendo.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                else:
                                    arq = open("peri_nintendo.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            quest = (
                                input("\nDeseja cadastrar outro produto?\nDigite 1 para sim\nDigite 2 para não:\n"))
                        break
                    if menu == '3':  # RETIRAR
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("jogos_nintendo.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("jogos_nintendo.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")
                            if categ == '2':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("consoles_nintendo.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("consoles_nintendo.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")
                            if categ == '3':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("peri_nintendo.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("peri_nintendo.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")

                            quest = input(
                                "\nDeseja retirar outro produto? \nDigite 1 para retirar outro.\nDigite 2 para sair.\n ")
                        break

    if plat == '4':  # LAÇO DO PC
                print("====== COMPUTADOR ======\n")
                menu_da_loja()
                while menu is not '9':
                    if menu == '1':  # CONSULTA
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("jogos_pc.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                                print("Consulta completa.")
                            if categ == '2':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("hardware_pc.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                            if categ == '3':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser consultado: ")
                                consult = consult.lower()
                                arq = open("peri_pc.txt", 'r')
                                for linha in arq:
                                    linha = linha.rstrip()
                                    search = consult
                                    if consult in linha:
                                        print(linha)
                            quest = input(
                                "\nDeseja consultar outro produto? \nDigite 1 para consultar outro.\nDigite 2 para sair do menu de consulta:\n ")
                        break
                    if menu == '2':  # REGISTRO
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("jogos_pc.txt"):
                                    arq = open("jogos_pc.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                    arq.close()
                                else:
                                    arq = open("jogos_pc.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            if categ == '2':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("hardware_pc.txt"):
                                    arq = open("hardware_pc.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                else:
                                    arq = open("hardware_pc.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            if categ == '3':
                                regi_play_nome = str(input("Digite o nome do produto: "))
                                regi_play_nome = regi_play_nome.lower()
                                regi_play_preço = float(input("Digite o preço do produto: "))
                                regi_play_cod = int(input("Digite o código do produto: "))
                                if os.path.exists("peri_pc.txt"):
                                    arq = open("peri_pc.txt", "a")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                                else:
                                    arq = open("peri_pc.txt", "w")
                                    arq.write(
                                        "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço, regi_play_cod))
                            quest = (
                                input("\nDeseja cadastrar outro produto?\nDigite 1 para sim\nDigite 2 para não:\n"))
                        break
                    if menu == '3':  # RETIRAR
                        while quest == '1':
                            menu_categoria()
                            if categ == '1':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("jogos_pc.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("jogos_pc.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")
                            if categ == '2':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("hardware_pc.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("hardware_pc.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")
                            if categ == '3':  # CATEGORIA
                                consult = input("Digite o nome ou código do produto a ser retirado: ")
                                consult = consult.lower()
                                with open("peri_pc.txt", 'r') as arq:
                                    lines = arq.readlines()
                                    arq.close()
                                    arq = open("peri_pc.txt", 'w')
                                    for line in lines:
                                        if consult not in line + "\n":
                                            arq.write(line)
                                    print("Produto retirado com sucesso! ")

                            quest = input(
                                "\nDeseja retirar outro produto? \nDigite 1 para retirar outro.\nDigite 2 para sair.\n ")
                        break

    if plat == '5':  # OUTROS PRODUTOS
       print("OUTROS.\n")
       menu_da_loja()
       while menu is not '9':
            if menu == '1':  # CONSULTA
               while quest == '1':
                      consult = input("Digite o nome ou código do produto a ser consultado: ")
                      consult = consult.lower()
                      arq = open("outros.txt", 'r')
                      for linha in arq:
                          linha = linha.rstrip()
                          search = consult
                          if consult in linha:
                              print(linha)
                      print("Consulta completa.")
                      quest = input("\nDeseja consultar outro produto? \nDigite 1 para consultar outro.\nDigite 2 para sair do menu de consulta:\n ")
               break
            if menu == '2':  # REGISTRO
                while quest == '1':
                        regi_play_nome = str(input("Digite o nome do produto: "))
                        regi_play_nome = regi_play_nome.lower()
                        regi_play_preço = float(input("Digite o preço do produto: "))
                        regi_play_cod = int(input("Digite o código do produto: "))
                        if os.path.exists("outros.txt"):
                            arq = open("outros.txt", "a")
                            arq.write(
                                "{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                            arq.close()
                        else:
                            arq = open("outros.txt", "w")
                            arq.write("{} R$:{}  Código:{}\n".format(regi_play_nome, regi_play_preço,regi_play_cod))
                        quest = (input("\nDeseja cadastrar outro produto?\nDigite 1 para sim\nDigite 2 para não:\n"))
                break
            if menu == '3': #RETIRAR
               while quest=='1':
                       consult = input("Digite o nome ou código do produto a ser retirado: ")
                       consult=consult.lower()
                       with open("outros.txt",'r') as arq:
                           lines=arq.readlines()
                           arq.close()
                           arq=open("outros.txt",'w')
                           for line in lines:
                               if consult not in line +"\n":
                                   arq.write(line)
                           print("Produto retirado com sucesso! ")

                       quest = input("\nDeseja retirar outro produto? \nDigite 1 para retirar outro.\nDigite 2 para sair.\n ")
               break

print("Programa encerrado. ")