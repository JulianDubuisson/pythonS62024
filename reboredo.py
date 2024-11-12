class ChatBot:
    def __init__(self):
        self.options = {
            "Inicio": {
                "mensaje": "Hola! Gracias por contactarte con Lucy Uñas ¿En qué puedo ayudarte?",
                "opciones": [
                    "1. Sacar turno",
                    "2. Reprogramar turno",
                    "3. Lista de precios",
                    "4. Horario de atención"
                ]
            },
            "Turnos": {
                "opciones": [
                    "1. Manicuria y esmaltado regular",
                    "2. Manicuria y esculpidas",
                    "3. Manicuria y semipermanente",
                    "4. Solo manicuria",
                    "5. Remoción",
                    "6. Volver al inicio"
                ]
            },
            "Profesional": {
                "mensaje" : "Nuestras profesionales son: ",
                "opciones": [
                    "1. Carla",
                    "2. Luisa",
                    "3. Lucia",
                    "4. No tengo ninguna preferencia",
                    "5. Volver a Turnos",
                    "6. Volver al inicio"
                ]
            },
            "diaHorario": {
                "mensaje" : "🕛 Los turnos disponibles son: ",
                "opciones": [
                    "1. Lunes 25/11: 14:05 hs.",
                    "2. Lunes 25/11: 14:35 hs.",
                    "3. Martes 26/11: 09:00 hs.",
                    "4. Martes 26/11: 16:35 hs.",
                    "5. Volver a Profesional",
                    "6. Volver a Turnos",
                    "7. Volver al menú principal"
                ]
            },
            "confirmarCancelar": {
                "opciones": [
                    "1. Confirmar turno",
                    "2. Cancelar turno",
                    "3. Volver a diaHorario",
                    "4. Volver al menú principal"
                ]
            }
        }

        self.respuestas = {
            "precio_manicuraEsmaltado": "$12000",
            "precio_manicuraSemi": "$18000",
            "precio_manicuraEsculpidas": "$25000",
            "precio_remocion": "$5000",
            "precio_Manicuria": "$9000",
            "reprogramar": "Para reprogramar el turno, llamar al número de teléfono: +54911 6465 4890. \n www.lucinails.com.ar",
        }

        self.estado_actual = "Inicio"

    def mostrar_menu(self):
        try:
            if self.estado_actual not in self.options:
                raise KeyError(f"Estado no válido: {self.estado_actual}")

            menu_actual = self.options[self.estado_actual]

            print("\n" + "-" * 50)
            print("\n💅 " + menu_actual.get("mensaje", "Elige una opción:"))
            print("\n✨ Opciones disponibles:")
            for opcion in menu_actual["opciones"]:
                print("  " + opcion)

            print("\n" + "-" * 50)
            print("(Ingresa 'q' para salir)")

        except KeyError as e:
            print(f"\nError: {e}")
            self.estado_actual = "Inicio"
            print("Regresando al menú principal...")
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, contacta al administrador del sistema.")


    def procesar_entrada(self, opcion):
        try:
            opcion = opcion.strip()
            opciones_validas = len(self.options[self.estado_actual]["opciones"])

            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > opciones_validas:
                print("\n❌ Opción no válida. Por favor, elige un número entre 1 y", opciones_validas)
                return

            opcion = int(opcion)

            if self.estado_actual == "Inicio":
                if opcion == 1:
                    self.estado_actual = "Turnos"
                elif opcion == 2:
                    print("\n📞 Reprogramar turno:")
                    print(self.respuestas["reprogramar"])
                elif opcion == 3:
                    print("\n📋 Información sobre precios:")
                    print(f"Manicuria y esmaltado regular: {self.respuestas['precio_manicuraEsmaltado']}")
                    print(f"Manicuria y semipermanente: {self.respuestas['precio_manicuraSemi']}")
                    print(f"Manicuria y esculpidas: {self.respuestas['precio_manicuraEsculpidas']}")
                    print(f"Remoción: {self.respuestas['precio_remocion']}")
                    print(f"Solo manicuria: {self.respuestas['precio_Manicuria']}")
                elif opcion == 4:
                    print("\n🕒 Horario de Atención:")
                    print("Lunes a viernes de 9:00 a 18:00 hrs")
                    self.estado_actual = "Inicio"

            elif self.estado_actual == "Turnos":
                if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
                    self.estado_actual = "Profesional"
                elif opcion == 6:
                    self.estado_actual = "Inicio"

            elif self.estado_actual == "Profesional":
                if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
                    self.estado_actual = "diaHorario"
                elif opcion == 5:
                    self.estado_actual = "Turnos"
                elif opcion == 6:
                    self.estado_actual = "Inicio"

            elif self.estado_actual == "diaHorario":
                if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
                    self.estado_actual = "confirmarCancelar"
                elif opcion == 5:
                    self.estado_actual = "Profesional"
                elif opcion == 6:
                    self.estado_actual = "Turnos"
                elif opcion == 7:
                    self.estado_actual = "Inicio"

            elif self.estado_actual == "confirmarCancelar":
                if opcion == 1:
                    print("\n✨ Turno confirmado!")
                    self.estado_actual = "Inicio"
                elif opcion == 2:
                    print("\n🗑️ Turno cancelado.")
                    self.estado_actual = "Inicio"
                elif opcion == 3:
                    self.estado_actual = "diaHorario"
                elif opcion == 4:
                    self.estado_actual = "Inicio"

        except Exception as e:
            print(f"\n❌ Error procesando la opción: {e}")
            print("Por favor, intenta nuevamente.")

    def ejecutar(self):
        print("\n¡Bienvenido al ChatBot de Lucy Nails! 💅")

        while True:
            self.mostrar_menu()
            opcion = input("\n➤ Ingresa el número de la opción deseada: ").strip()

            if opcion.lower() == 'q':
                print("\n¡Gracias por usar nuestro ChatBot! ¡Hasta pronto! 👋")
                break

            self.procesar_entrada(opcion)

if __name__ == "__main__":
    bot = ChatBot()
    bot.ejecutar()

# EL FLUJO DE CONVESASIÓN ES INICIO -> TURNOS -> PROFESIONAL -> DIAHORARIO -> CONFIRMAR CANCELAR

# UNA VEZ CONFIRMADO O CANCELADO EL TURNO, VUELVE AUTOMÁTICAMENTE AL MENÚ INICIAL