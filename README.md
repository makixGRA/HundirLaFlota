# HundirLaFlota

Autores del proyecto: Miguel Anguita y Olivier

Hemos desarrollado el clásico juego de Hundir La Flota. 

Hay dos jugadores: tú y la maquina. Manejaremos un tablero de 10 x 10 posiciones donde irán los barcos.

Colocamos los siguientes barcos:

- 4 barcos de 1 posición de eslora
- 3 barcos de 2 posiciones de eslora
- 2 barcos de 3 posiciones de eslora
- 1 barco de 4 posiciones de eslora

Tanto tú, como la maquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde. Funciona por turnos y empiezas tú.

En cada turno disparas a una coordenada (X, Y) del tablero adversario. Si aciertas, te vuelve a tocar. En caso contrario, le toca a la maquina.

En los turnos de la máquina, si acierta, también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.

Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
