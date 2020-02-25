# apenas um exeplo para entender o while not
# lopp só fica rodando enquanto o valor é true
acertou = false
while not acertou:
    if (jogador == computador):
        acertou == true

#https://cursos.alura.com.br/forum/topico-duvida-no-laco-while-81833
print("""Para ficar dentro do laço 'while' a expressão que é verificada precisa ser verdadeira. 
Para isso, as duas variáveis precisam ser 'False' para que a condição 'not enforcou and not acertou' seja verdadeira no final, pois o 'not' inverte o valor de 'enforcou' e 'acertou' para 'True' na verificação.
Quando mais a frente no programa o valor de uma delas muda para 'True', na expressão de verificação do 'while' o 'not' altera o valor dela para 'False' fazendo a expressão 'not enforcou and not acertou' ser falsa e saindo do laço.

No caso do jogador enforcar:

enforcou == True
acertou == False

not enforcou == False
not acertou == True

not enforcou and not acertou == False """)
