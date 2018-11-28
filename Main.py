import turtle
import time

tela = turtle.Screen()  # Instancia a tela (Não necessario caso n mudar atributos)
tela.bgcolor('black')    # Define a cor da tela
tela.setup(1200, 720)    # Define o tamanho da janela

pen = turtle.Pen()   # Constrói um objeto caneta  (Pen)
pen.shape('classic') # Muda a forma do cursor/caneta
pen.color('white')
pen.forward(100)     # anda 100 posições para a frente
pen.right(45)        # gira o ponteiro em 45 graus para a direita
pen.forward(100)     # anda mais 100 posições para a frente
pen.circle(50)       # Desenha um circulo de raio 50

pen.up()             # Levanta o 'Rabo' para parar de desenhar
pen.goto(20, 20)     # Indica uma coordenada a ir
pen.dot(5, 'white')  # Desenha um ponto de tamanho 5 e cor branca
pen.goto(0, 0)
pen.down()           # Abaixa o 'Rabo'

time.sleep(2)        # Tempo até janela ser fechada
