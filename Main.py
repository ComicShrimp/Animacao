import turtle
import random as rand
import math

# usar #000080 para azul com sobra e #0000ff para azul normal
# Apesar de existir uma função para desenhar o circulo, precisamos percorre-lo

raio = 50

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
    xs = rand.randint(-800, 800)
    ys = rand.randint(-360, 360)

    if math.sqrt(pow(xs, 2) + pow(ys, 2)) > raio:
        pen.up()
        pen.goto(xs, ys)
        pen.down()
        pen.dot(2, 'white')
    else:
        i = i - 1

tela.update() # Faz update da tela, pois a animação está desligada
pen.up()
pen.goto(0, raio)
pen.down()

pen.up()

#funciona mas está muito lento
for x in range(-raio, raio):
    for y in range(-raio, raio):
        if math.sqrt(pow(x, 2) + pow(y, 2)) < raio:
            pen.goto(x, y)
            if rand.randint(0, raio * 2) > raio + x * 1.2:
                pen.dot(1, "#191970")
            else:
                pen.dot(1, "#00ffff")
    tela.update()

tela.update()

tela.exitonclick()
