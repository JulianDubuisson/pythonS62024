class ChatBot:
    def __init__(self):
        self.options = {
            "inicio": {
                "mensaje": "Bienvenidos a Bot Day School ¿En qué te puedo ayudar?",
                "opciones": [
                    "1. Secciones y Areas",
                    "2. Admisiones",
                    "3. Contacto",
                    "4. Horario de atención"
                ]    
            },
            "secciones": {
                "mensaje": "Selecciona una sección:",
                "opciones": [
                    "1. Kinder",
                    "2. Primary",
                    "3. Middle",
                    "4. Senior",
                    "5. Volver al inicio"
                ]
            },
            "kinder": {
                "mensaje": "Información sobre Kinder 👶:",
                "opciones": [
                    "1. Jornada",
                    "2. Edades",
                    "3. Actividades",
                    "4. Volver a Secciones y Áreas",
                    "5. Volver al menú principal"
                ]
            },
            "primary": {
                "mensaje": "Información sobre Primary 👦🏽:",
                "opciones": [
                    "1. Jornada",
                    "2. Actividades",
                    "3. Volver a Secciones y Áreas",
                    "4. Volver al menú principal"
                ]
            },
            "middle": {
                "mensaje": "Información sobre Middle 👧🏼:",
                "opciones": [
                    "1. Jornada",
                    "2. Actividades",
                    "3. Volver a Secciones y Áreas",
                    "4. Volver al menú principal"
                ]
            },
            "senior": {
                "mensaje": "Información sobre Senior 👩🏼:",
                "opciones": [
                    "1. Jornada",
                    "2. Electivas y Orientativas",
                    "3. Actividades",
                    "4. Volver a Secciones y Áreas",
                    "5. Volver al menú principal"
                ]
            }
        }
        
        self.respuestas = {
            "kinder_jornada": "Horario de 8:00 AM a 2:00 PM",
            "kinder_edades": "Niños de 3 a 5 años",
            "kinder_actividades": "Juegos didácticos, arte, música y desarrollo motriz",
            "primary_jornada": "Horario de 8:30 AM a 3:00 PM",
            "primary_actividades": "Materias básicas, deportes y talleres creativos",
            "middle_jornada": "Horario de 8:25 AM a 16:05 PM",
            "middle_actividades": "Materias avanzadas, laboratorios y proyectos",
            "senior_jornada": "Horario de 8:25 AM a 16:05 PM",
            "senior_electivas": "Ciencias, humanidades, artes y tecnología",
            "senior_actividades": "Proyectos de investigación, pasantías y orientación vocacional",
            "admisiones": "Para iniciar el proceso de admisión, ingresa a https://bds.edu.ar/admisiones/ \nO enviá un mail a rrpp@bdsnet.com.ar",
            "contacto": "Email: info@dayschool.edu\nTeléfono: 555-0123",
            "horario_atencion": "Lunes a Viernes de 8:00 AM a 5:00 PM",
        }
        
        self.estado_actual = "inicio"

    def mostrar_menu(self):
        try:
            if self.estado_actual not in self.options:
                raise KeyError(f"Estado no válido: {self.estado_actual}")

            menu_actual = self.options[self.estado_actual]
            
            print("\n" + "="*50)
            print("\n🏫 " + menu_actual["mensaje"])
            print("\n📋 Opciones disponibles:")
            for opcion in menu_actual["opciones"]:
                print("  " + opcion)
            
            print("\n" + "="*50)
            print("(Ingresa 'q' para salir)")
            
        except KeyError as e:
            print(f"\nError: {e}")
            self.estado_actual = "inicio"
            print("Regresando al menú principal...")
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, contacta al administrador del sistema.")

    def procesar_entrada(self, opcion):
        """Procesa la entrada del usuario y actualiza el estado"""
        try:
            # Convertir la entrada a un número (si es posible)
            opcion = opcion.strip()
            
            # Verificar si la opción es válida para el menú actual
            opciones_validas = len(self.options[self.estado_actual]["opciones"])
            
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > opciones_validas:
                print("\n❌ Opción no válida. Por favor, elige un número entre 1 y", opciones_validas)
                return

            opcion = int(opcion)
            
            # Procesar según el estado actual
            if self.estado_actual == "inicio":
                if opcion == 1:
                    self.estado_actual = "secciones"
                elif opcion == 2:
                    print("\n📝 Información de Admisiones:")
                    print(self.respuestas["admisiones"])
                elif opcion == 3:
                    print("\n📞 Información de Contacto:")
                    print(self.respuestas["contacto"])
                elif opcion == 4:
                    print("\n🕒 Horario de Atención:")
                    print(self.respuestas["horario_atencion"])

            #RESPUESTAS SECCIONES

            elif self.estado_actual == "secciones":
                if opcion == 1:
                    self.estado_actual = "kinder"
                elif opcion == 2:
                    self.estado_actual = "primary"
                elif opcion == 3:
                    self.estado_actual = "middle"
                elif opcion == 4:
                    self.estado_actual = "senior"
                elif opcion == 5:
                    self.estado_actual = "inicio"

            #RESPUESTAS POR AREAS
                    
            elif self.estado_actual in ["kinder", "primary", "middle", "senior"]:
                if opcion == 1:  # Jornada
                    print(f"\n🕒 Jornada {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_jornada"])
                elif opcion == 2:  # Edades/Actividades/Electivas
                    if self.estado_actual == "kinder":
                        print("\n👶 Edades:")
                        print(self.respuestas["kinder_edades"])
                    elif self.estado_actual == "senior":
                        print("\n📚 Electivas y Orientativas:")
                        print(self.respuestas["senior_electivas"])
                    else:
                        print(f"\n📋 Actividades {self.estado_actual.capitalize()}:")
                        print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 3:  # Actividades
                    print(f"\n🎯 Actividades {self.estado_actual.capitalize()}:")
                    print(self.respuestas[f"{self.estado_actual}_actividades"])
                elif opcion == 4:  # Volver a secciones
                    self.estado_actual = "secciones"
                elif opcion == 5:  # Volver al inicio
                    self.estado_actual = "inicio"
                    
        except Exception as e:
            print(f"\n❌ Error procesando la opción: {e}")
            print("Por favor, intenta nuevamente.")

    def ejecutar(self):
        print("\n¡Bienvenido al ChatBot del Day School! 🎓")
        
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