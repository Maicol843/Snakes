import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0

#Configuración de la ventana
wn = turtle.Screen()
wn.title("Juego de Snakes")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.direction = "stop"

#segmentos / cuerpo de la serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0          High Score: 0", align = "center", font = ("Courier", 20, "normal"))

#Funciones
def arriba():
    cabeza.direction = "up"
    
def abajo():
    cabeza.direction = "down"
    
def izquierda():
    cabeza.direction = "left"
    
def derecha():
    cabeza.direction = "right"

def mov():
    #Movimiento hacia arriba
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    #Movimiento hacia abajo
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    #Movimiento hacia izquierda
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    
    #Movimiento hacia derecha
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #Limpiar lista de segmentos
        segmentos.clear()
        
        #Resetear marcador
        
        texto.clear()
        texto.write("Score: {}          High Score: {}".format(score, high_score), align = "center", font = ("Courier", 20, "normal"))

    #Colisiones comida
    if cabeza.distance(comida) < 20:
        #Mover la cabeza a posición random
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        
        nuevo_Segmento = turtle.Turtle()
        nuevo_Segmento.speed(0)
        nuevo_Segmento.shape("square")
        nuevo_Segmento.color("green")
        nuevo_Segmento.penup()
        segmentos.append(nuevo_Segmento)
        
        #Aumentar marcador
        score += 10
        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write("Score: {}          High Score: {}".format(score, high_score), align = "center", font = ("Courier", 20, "normal"))

    #Mover el cuerpo de la serpiente
    total_segmentos = len(segmentos)
    for index in range(total_segmentos -1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()

        #Resetear marcador
        
        texto.clear()
        texto.write("Score: {}          High Score: {}".format(score, high_score),align = "center", font = ("Courier", 20, "normal"))
    
    time.sleep(posponer)
