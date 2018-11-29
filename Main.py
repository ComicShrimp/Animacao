import turtle
import random as rand
import math

# usar #000080 para azul com sobra e #0000ff para azul normal
# Apesar de existir uma função para desenhar o circulo, precisamos percorre-lo

raio = 200

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

    if math.sqrt(pow(x, 2) + pow(y, 2)) > raio:
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.dot(2, 'white')
    else:
        i = i - 1

tela.update() # Faz update da tela, pois a animação está desligada
pen.up()
pen.goto(0, raio)
pen.down()

passo = math.pi * raio / 180

for j in range(360):
    pen.forward(passo)
    pen.right(1)

pen.up()             # Levanta o 'Rabo' para parar de desenhar
pen.goto(0, 0)       # Indica uma coordenada a ir
pen.color("#000080")
pen.dot(10)

tela.exitonclick()
