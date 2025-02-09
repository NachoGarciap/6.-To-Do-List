import json
import os.path


class toDoList:

    def __init__(self):
        print('----- LISTA DE TAREAS -----')
        self.tareas = []  # lista vacia para guardar las tareas
        self.contador_id = 1  # para un id unico para cada tarea
        self.cargar_json()  # para que las tareas guardadas no se pierdan

    def menu(self):
        while True:
            print('--- Menu ---')
            print('1. Agregar una tarea')
            print('2. Listar las tareas')
            print('3. Marcar tarea como completada')
            print('4. Eliminar una tarea')
            print('5. Salir')

            opcion = int(input('Introduce una opción valida: '))

            if opcion == 1:
                self.agregar_tareas()
            elif opcion == 2:
                self.listar_tareas()
            elif opcion == 3:
                self.marcar_tareas_completadas()
            elif opcion == 4:
                self.eliminar_tarea()
            elif opcion == 5:
                print('Saliendo del programa...')
                break
            else:
                print('Introduce una opción valida.')

    def agregar_tareas(self):
        descripcion = input('Introduce la descripcion de la tarea: ')
        tarea = {
            'id': self.contador_id,
            'descripcion': descripcion,
            'completada': False
        }  # false=no completada, true=completada

        self.tareas.append(tarea)  # agregar tarea en la lista tareas
        self.contador_id += 1
        self.guardar_en_json()  # guardar cambios en el json
        print('Tarea agregada con exito!')

    def listar_tareas(self):
        if not self.tareas:
            print('No hay tareas en la lista')
            return

        print('\n----- Lista de Tareas -----')
        for tarea in self.tareas:
            estado = '✅ Completada' if tarea['completada'] else '❌ Pendiente'
            print(f'ID: {tarea['id']} | {tarea['descripcion']} -> {estado}')
        print("----------------------------")

    def marcar_tareas_completadas(self):
        self.listar_tareas()  # mostrar las tareas
        try:
            id_tarea = int(input('Introduce el id de la tarea: '))
            for tarea in self.tareas:
                if tarea['id'] == id_tarea:  # si coinciden el id
                    if tarea['completada']:
                        print('La tarea ya esta completada')
                    else:
                        tarea['completada'] = True
                        self.guardar_en_json()  # guardar cambios en el json
                        print(f'✅ Tarea "{tarea['descripcion']}" marcada como completada.')
                    return  # Salir del método después de encontrar la tarea

            print('No se encontró ninguna tarea con ese ID.')  # Si el ID no existe

        except ValueError:
            print('Error: Debes ingresar un número válido.')

    def eliminar_tarea(self):
        self.listar_tareas()  # mostrar las tareas
        try:
            eliminar_id = int(input('Eliminar una tarea por id: '))
            for tarea in self.tareas:
                if tarea['id'] == eliminar_id:
                    self.tareas.remove(tarea)
                    self.guardar_en_json()  # guardar cambios en el json
                    print(f'🗑️ Tarea "{tarea["descripcion"]}" eliminada con éxito.')
                    return  # Salir del método después de eliminar la tarea

            print("No se encontró ninguna tarea con ese ID.")  # Si el ID no existe
        except ValueError:
            print("Error: Debes ingresar un número válido.")

    def guardar_en_json(self):
        with open("tareas.json", "w", encoding="utf-8") as archivo:
            json.dump(self.tareas, archivo, indent=4, ensure_ascii=False)
            # ensure_ascii para que lea caracteres especiales como tildes
            # indent=4 para que el archivo sea legible (formato), json.dump convertir datos de python en json y guardarlos en un archivo

    def cargar_json(self):
        if os.path.exists('tareas.json'):  # verificare si el archivo existe
            with open('tareas.json', 'r', encoding='utf8') as archivo:
                self.tareas = json.load(archivo)  # cargar la lista de tareas


# PRUEBA
prueba = toDoList()
prueba.menu()
