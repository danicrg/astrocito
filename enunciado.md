# Astrocito

Estamos trabajando en el estudio de la estructura neuronal del cerebro. Para ello, grabamos vídeos de una lámina de tejido cerebral de ratones y examinamos cómo reaccionan las neuronas a impulsos eléctricos. Lamentablemente nuestros científicos no son muy tecnológicos y la resolución de algunos vídeos es peor que otros.  Viendo los videos se observa que se excitan las neuronas tras un impulso eléctrico y a continuación se disipa por sus dentritas (las colas). 

El objetivo del problema es, dado el video, encontrar la posición de la neurona en el tejido, que es la zona de interés para nuestro estudio. Cada vídeo está muestreado a 60 fps y dura 10 segundos. El valor de cada píxel del fotograma equivale a un nivel de intensidad lumínica. Cuando la neurona se excita, el nivel de intensidad lumínica alcanza picos.

## Input

La primera linea contiene el alto (H) , ancho (W) y número de fotogramas (N) del vídeo. 

Las líneas siguientes contienen los píxeles de los fotogramas.

## Output

Una matriz de ceros donde no hay neuronas y de unos donde hay neurona.

## Constraints

1 < H < 500

1 < W < 500

N = 600

0 <= P <= 10 (Potencia lumínica del pixel)