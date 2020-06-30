def funcaoArmazenamento(nome, email):
    try:
        arquivos = open("LogDeSistema.txt", "a")
        arquivos.write("\n")
        arquivos.write("Nome: ")
        arquivos.write(nome)
        arquivos.write("\n")
        arquivos.write("Email: ")
        arquivos.write(email)
        
    except:
        arquivos = open("LogDeSistema.txt", "a")
        arquivos.write("\n     ")
        arquivos.write(input(nome))
        arquivos.write("\n")
        arquivos.write(input(email))
        arquivos.write("\n   ")

