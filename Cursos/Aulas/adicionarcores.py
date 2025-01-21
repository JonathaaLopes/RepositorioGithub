

'''
 \033[ é o início da sequência.
 <código de estilo> é opcional e define o estilo do texto (como negrito).
 <código de cor do texto> define a cor do texto.
 <código de cor do fundo> define a cor de fundo.

 Códigos de estilo, texto e fundo
 Aqui estão alguns códigos que você pode usar:

 Estilos:

 0: Sem estilo (padrão).
 1: Negrito.
 4: Sublinhado.
 7: Inverter cores (texto vira fundo e fundo vira texto).
 Cores do texto:

 30: Preto.
 31: Vermelho.
 32: Verde.
 33: Amarelo.
 34: Azul.
 35: Magenta.
 36: Ciano.
 37: Branco.
 Cores do fundo:

 40: Preto.
 41: Vermelho.
 42: Verde.
 43: Amarelo.
 44: Azul.
 45: Magenta.
 46: Ciano.
47: Branco.'''


#Exemplo

# Texto vermelho
print("\033[31mTexto em vermelho\033[m")



# Texto vermelho em negrito
print("\033[1;31mTexto vermelho em negrito\033[m")

# Texto branco com fundo azul
print("\033[37;44mTexto branco com fundo azul\033[m")

# Texto amarelo sublinhado com fundo magenta
print("\033[4;33;45mTexto amarelo sublinhado com fundo magenta\033[m")

