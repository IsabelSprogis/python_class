idade_pessoa = 14
status_amigo_do_dono = True
maior_de_idade = idade_pessoa >= 18
# Esse é um comentario
# blocos if else com statementes booleanos (and or not, ==, > , <  ou !=)
# Existe um tipo especial None que é igual ao null
if maior_de_idade or status_amigo_do_dono:
    print('Pode beber')
    print('... ou amigo do dono ...')
else:
    print('Menor de idade')
    print('Nao pode beber')
