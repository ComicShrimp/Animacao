import turtle
import random as rand
import math

# usar #000080 para azul com sobra e #0000ff para azul normal

tela = turtle.Screen()  # Instancia a tela (Não necessario caso n mudar atributos)
tela.bgcolor('black')    # Define a cor da tela
tela.setup(1200, 720)    # Define o tamanho da janela

pen = turtle.Pen()   # Constrói um objeto caneta  (Pen)
pen.hideturtle()     # Esconde a Turtle

pen.speed(0)
pen.color('white')

tela.tracer(0, 0) # Retira a animação da turtle

# Função para adicionar ceu estrelado
for i in range(500):
    x = rand.randint(-800, 800)
    y = rand.randint(-360, 360)

    if math.sqrt(pow(x, 2) + pow(y, 2)) > 200:
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.dot(2, 'white')
    else:
        i = i - 1

tela.update() # Faz update da tela, pois a animação está desligada
pen.up()
pen.goto(0, -200)
pen.down()
pen.circle(200)       # Desenha um circulo de raio 50

pen.up()             # Levanta o 'Rabo' para parar de desenhar
pen.goto(0, 0)     # Indica uma coordenada a ir
pen.color("#000080")
pen.dot(10)

tela.exitonclick()
