try:
    file = open('testefile', 'w')
    file.write("Teste")
#except IOError, não é necessário utilizar apenas se quiser expecificar o erro
except:
    print("Erro ao tratar o arquivo.")
else:
    print("Não houve erro")
finally:
    print("Bloco finally")
