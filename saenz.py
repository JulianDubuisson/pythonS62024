class ChatBot:
    def __init__(self):
        self.estado_actual = "inicio"
        
        # Estructura de opciones de menú
        self.options = {
            "inicio": {
                "mensaje": "Bienvenidos a Varela, ¿en qué te podemos ayudar?",
                "opciones": [
                    "1. Productos",
                    "2. Ayuda al hincha",
                    "3. A copar Varela",
                    "4. Contactos",
                ]
            },
            "Productos": {
                "mensaje": "¿Qué producto te interesa?",
                "opciones": [
                    "1. Camisetas",
                    "2. Pantalones",
                    "3. Accesorios",
                    "4. Volver al inicio",
                ]
            },
            "Camisetas": {
                "mensaje": "¿Qué tipo de camiseta buscas?",
                "opciones": [
                    "1. Titular",
                    "2. Suplente",
                    "3. Entrenamiento",
                    "4. Volver a Productos",
                ]
            },
            "precioCamisetaTitular": {
                "mensaje": "Precio: $15.000",
                "opciones": [
                    "1. Confirmar compra",
                    "2. Cancelar compra",
                    "3. Volver a Productos",
                    "4. Volver al inicio",
                ]
            },
            "precioCamisetaSuplente": {
                "mensaje": "Precio: $12.000",
                "opciones": [
                    "1. Confirmar compra",
                    "2. Cancelar compra",
                    "3. Volver a Productos",
                    "4. Volver al inicio",
                ]
            },
            "precioCamisetaEntrenamiento": {
                "mensaje": "Precio: $10.000",
                "opciones": [
                    "1. Confirmar compra",
                    "2. Cancelar compra",
                    "3. Volver a Productos",
                    "4. Volver al inicio",
                ]
            },
            "Pantalones": {
                "mensaje": "¿Qué tipo de pantalón te interesa?",
                "opciones": [
                    "1. Verde de juego",
                    "2. Volver a Productos",
                ]
            },
            "precioPantalon": {
                "mensaje": "Precio: $20.000",
                "opciones": [
                    "1. Confirmar compra",
                    "2. Cancelar compra",
                    "3. Volver a Productos",
                    "4. Volver al inicio",
                ]
            },
            "Accesorios": {
                "mensaje": "¿Qué accesorio te gustaría?",
                "opciones": [
                    "1. Ojotas",
                    "2. Piluso",
                    "3. Volver a Productos",
                ]
            },
            "precioOjota": {
                "mensaje": "Precio: $5.000",
                "opciones": [
                    "1. Confirmar compra",
                    "2. Cancelar compra",
                    "3. Volver a Productos",
                    "4. Volver al inicio",
                ]
            },
            "precioPiluso": {
                "mensaje": "Precio: $3.000",
                "opciones": [
                    "1. Confirmar compra",
                    "2. Cancelar compra",
                    "3. Volver a Productos",
                    "4. Volver al inicio",
                ]
            },
            "Ayuda al hincha": {
                "mensaje": "¿Qué necesitas saber sobre el hincha?",
                "opciones": [
                    "1. Hacete socio",
                    "2. Saca tu abono",
                    "3. Compra una entrada",
                    "4. Volver al inicio",
                ]
            },
            "Hacete socio": {
                "mensaje": "Ingresa a nuestra página web para hacerte socio.",
                "opciones": [
                    "1. Volver al inicio",
                ]
            },
            "Saca tu abono": {
                "mensaje": "Ingresa a nuestra página web para sacar tu abono.",
                "opciones": [
                    "1. Volver al inicio",
                ]
            },
            "Compra una entrada": {
                "mensaje": "Ingresa a nuestra página web para comprar tu entrada.",
                "opciones": [
                    "1. Volver al inicio",
                ]
            },
            "A copar Varela": {
                "mensaje": "¿Qué sector prefieres para copar Varela?",
                "opciones": [
                    "1. Platea",
                    "2. Popular local",
                    "3. Popular visitante",
                    "4. Volver al inicio",
                ]
            },
            "Contactos": {
                "mensaje": "¿Cómo te podemos contactar?",
                "opciones": [
                    "1. Ver contacto",
                    "2. Volver al inicio",
                ]
            }            
        }
        
        # Datos de contacto
        self.respuesta = {
            "contacto": "Correo: Sudamericana@defeyj.com.ar\nTeléfono: 9112830292",
        }

    def mostrar_menu(self):
        """Muestra el menú correspondiente al estado actual."""
        try:
            if self.estado_actual not in self.options:
                raise KeyError(f"Estado no válido: {self.estado_actual}")
                
            menu_actual = self.options[self.estado_actual]
            
            print("\n" + "_"*50)
            print("\n " + menu_actual["mensaje"])
            print("\n Opciones disponibles:")
            for opcion in menu_actual["opciones"]:
                print("  " + opcion)
            
            print("\n" + "_"*50)
            print("(Ingresa 'q' para salir)")
            
        except KeyError as e:
            print(f"\nError: {e}")
            self.estado_actual = "inicio"
            print("Regresando al menú principal...")
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, contacta al administrador del sistema.")
        
    def procesar_entrada(self, opcion):
        """Procesa la entrada del usuario y actualiza el estado."""
        try:
            opcion = opcion.strip()
            
            # Verificar si la opción es válida para el menú actual
            menu_actual = self.options[self.estado_actual]
            opciones_validas = len(menu_actual["opciones"])
            
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > opciones_validas:
                print("\n❌ Opción no válida. Por favor, elige un número entre 1 y", opciones_validas)
                return
            
            opcion = int(opcion)
                
            # Procesar según el estado actual

            #ESTADO ACTUAL INICIO
            if self.estado_actual == "inicio":
                if opcion == 1:
                    self.estado_actual = "Productos"
                elif opcion == 2:
                    self.estado_actual = "Ayuda al hincha"
                elif opcion == 3:
                    self.estado_actual = "A copar Varela"
                elif opcion == 4:
                    self.estado_actual = "Contactos"
            
            #ESTADO ACTUAL PRODUCTO
            elif self.estado_actual == "Productos":
                if opcion == 1:
                    self.estado_actual = "Camisetas"
                elif opcion == 2:
                    self.estado_actual = "Pantalones"
                elif opcion == 3:
                    self.estado_actual = "Accesorios"
                elif opcion == 4:
                    self.estado_actual = "inicio"
            
            #ESTADO ACTUAL CAMISETA
            elif self.estado_actual == "Camisetas":
                if opcion == 1:
                    self.estado_actual = "precioCamisetaTitular"
                elif opcion == 2:
                    self.estado_actual = "precioCamisetaSuplente"
                elif opcion == 3:
                    self.estado_actual = "precioCamisetaEntrenamiento"
                elif opcion == 4:
                    self.estado_actual = "Productos"
                elif opcion == 5: 
                    self.estado_actual = "inicio"
            
            #ESTADO ACTUAL PANTALON
            elif self.estado_actual == "pantalon":
                if opcion == 1:
                    self.estado_actual = "precioPantalonVerde"
                elif opcion == 2:
                    self.estado_actual = "Productos"
                elif opcion == 3:
                    self.estado_actual = "inicio"
            

            
            #ESTADO ACTUAL CAMISETA TITULAR
            elif self.estado_actual == "precioCamisetaTitular":
                if opcion == 1:
                    print("\n✅ La compra se ha realizado con éxito")
                elif opcion == 2:
                    print("\n❌ La compra no se ha realizado con éxito")
                elif opcion == 3:
                    self.estado_actual = "Productos"
                elif opcion == 4:
                    self.estado_actual = "inicio"        
            
            elif self.estado_actual == "Pantalones":
                if opcion == 1:
                    self.estado_actual = "precioPantalon"
                elif opcion == 2:
                    self.estado_actual = "Productos"
                elif opcion == 3:
                    self.estado_actual = "inicio"
            
            elif self.estado_actual == "Accesorios":
                if opcion == 1:
                    print("\nOjotas seleccionadas")
                elif opcion == 2:
                    print("\nPiluso seleccionado")
                elif opcion == 3:
                    self.estado_actual = "Productos"
            
            elif self.estado_actual == "Ayuda al hincha":
                if opcion == 1:
                    self.estado_actual = "Hacete socio"
                elif opcion == 2:
                    self.estado_actual = "Saca tu abono"
                elif opcion == 3:
                    self.estado_actual = "Compra una entrada"
                elif opcion == 4:
                    self.estado_actual = "inicio"
            
            elif self.estado_actual == "Contactos":
                if opcion == 1:
                    print("\n" + self.respuesta["contacto"])
                elif opcion == 2:
                    self.estado_actual = "inicio"
        
        except Exception as e:
            print(f"\nError procesando la opción: {e}")
    
    def ejecutar(self):
        print("\n¡Bienvenido al ChatBot del Halcón de Varela! 🎓")
        
        while True:
            self.mostrar_menu()
            opcion = input("\n➤ Ingresa el número de la opción deseada: ").strip()
            
            if opcion.lower() == 'q':
                print("\n¡Gracias por usar nuestro ChatBot! ¡Hasta pronto! 👋")
                break
                
            self.procesar_entrada(opcion)

# Ejemplo de uso
if __name__ == "__main__":
    bot = ChatBot()
    bot.ejecutar()
