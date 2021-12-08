# 1. 

curve(
      x^2-3*x + 30,
      xlim = c(-15,15), 
      main = "Una parabola", 
      xlab = expression(x),
      ylab = expression(y = x^{2} - 3*x + 30),
      col = "blueviolet",
      lwd  = 2
)

# 2. 

# El script es incorrecto. Si se define un función y los valores de entrada 
# el gráfico saldrá en forma de puntos f(I), necesitaría de argumentos 
# complementarios para generar un curva

# Definimos la función y su dominio
f = function(x){
  x^2 - 3*x + 30
  }
I = c(-15:15)
# Lo correcto sería
plot(
     I, 
     f(I),
     xlim = c(-15,15),
     type = "l",
     main = "Una parabola",
     xlab = expression(x),
     ylab = expression(y=x^2-3*x+30),
     col = "blueviolet",
     lwd  = 2
)

# plot(f,main="Una parabola",
#      xlim = c(-15,15),
#      xlab = expression(x),
#      ylab = expression(y=x^{2}-3*x+30),
#      col = "blueviolet",
#      lwd  = 2
#      )

# 3.

curve(
      5*2^x,
      xlim = c(-10,25),
      ylab = expression(y = 5*2^x), 
      xlab = "",
      col = "blueviolet",
      lwd  = 2
)

# 4. 
curve(
      3*x,
      xlim = c(-10, 20), 
      xlab = "", 
      ylab = "",
      col = "blue", 
      main = "2 rectas", 
      sub = "Dos rectas con pendiente opuesto"
) 

curve(
      -3*x,
      col = "green",
      add = TRUE
)

legend(
       x = 13, 
       y = 10,
       legend = c("3x", "-3x"),
       lty = c(1,1),
       cex = 0.7,
       col = c("blue", "green")
)

# 5.

curve(
      3*x,
      xlim = c(-10, 20), 
      xlab = "", 
      ylab = "",
      col = "blue", 
      main = "2 rectas", 
      sub = "Dos rectas con pendiente opuesto"
) 

curve(
      -3*x,
      col = "green",
      add = TRUE
)

abline(
       h = 0,
       col = "red",
       lwd = 5
)

legend(
       x = 13, 
       y = 10,
       legend = c("3x", "-3x"),
       lty = c(1,1),
       cex = 0.7,
       col = c("blue", "green")
)

# 6.
curve(
      3*x,
      xlim = c(-10, 20), 
      xlab = "", 
      ylab = "",
      col = "blue", 
      main = "2 rectas", 
      sub = "Dos rectas con pendiente opuesto"
) 

curve(
      -3*x,
      col = "green",
      add = TRUE
)

abline(
       h = 0,
       col = "red",
       lwd = 5
)

abline(
       a = 7,
       b = 2,
       col = "blue",
       lwd = 2,
)

legend(
       x = 13, 
       y = 10,
       legend = c("3x", "-3x"),
       lty = c(1,1),
       cex = 0.7,
       col = c("blue", "green")
)
