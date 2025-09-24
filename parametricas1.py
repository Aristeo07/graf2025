import numpy as np
import cv2


opcion = int(input("Ingresa un numero del 1 al 10 para seleccionar la ecuacion parametrica a trazar"))


# Opción 1: Curva de Limacon
# Opción 2: Espiral de Arquímedes
# Opción 3: Elipse
# Opción 4: Hipocicloide(Curva dentada)
# Opcion 5: Epicicloide
# Opcion 6: Lemniscata de Bernoulli
# Opcion 7 : Curva de Lissajous
# Opcion 8: Rosa polar
# Opcion 9: Cardioide
# Opcion 10 : Espiral logaritmica






if(opcion ==1):
    # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            r = a + b * np.cos(k * t)
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (x-2, y-2), 3, (0, 0, 0), -1)  # Color rojo


            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)


        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()

elif(opcion ==2):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            r = 10 * t
            x = r * np.cos(t)
            y = r * np.sin(t)


            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()


elif(opcion ==3):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            x = 250 * np.cos(t)
            y = 150 * np.sin(t)


            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()


elif(opcion ==4):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            R, r = 150, 50
            x = (R - r) * np.cos(t) + r * np.cos((R - r) * t / r)
            y = (R - r) * np.sin(t) - r * np.sin((R - r) * t / r)

            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()    

elif(opcion ==5):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            R, r = 100, 30
            x = (R + r) * np.cos(t) - r * np.cos((R + r) * t / r)
            y = (R + r) * np.sin(t) - r * np.sin((R + r) * t / r)

            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()        



elif(opcion ==6):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            a = 200
            x = (a * np.cos(t)) / (1 + np.sin(t)**2)
            y = (a * np.sin(t) * np.cos(t)) / (1 + np.sin(t)**2)

            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()


elif(opcion ==7):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            A, B, a, b, delta = 200, 200, 3, 2, np.pi/2
            x = A * np.sin(a * t + delta)
            y = B * np.sin(b * t)


            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()     


elif(opcion ==8):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            k = 5  # número de pétalos si k es impar, 2k si es par
            r = 200 * np.cos(k * t)
            x = r * np.cos(t)
            y = r * np.sin(t)

            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()     


elif(opcion ==9):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            a = 150
            r = a * (1 - np.cos(t))
            x = r * np.cos(t)
            y = r * np.sin(t)

            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()     



elif(opcion ==10):
      # Definir los parámetros iniciales
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
    k = 0.7# Constante de multiplicación del ángulo
    theta_increment = 0.05  # Incremento del ángulo
    max_theta = 2 * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            a, b = 5, 0.15
            r = a * np.exp(b * t)
            x = r * np.cos(t)
            y = r * np.sin(t)

            #Convertir a coordenadas de la imagen, en enteros y centrados
            px = int(center_x  - x)
            py = int(center_y - y)

            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (px, py), 3, (0, 0, 0), -1)  # Color rojo


            

        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break

    # Cerrar la ventana al finalizar
    cv2.destroyAllWindows()     

