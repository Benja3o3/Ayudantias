contacts = []

while True:
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    choice = input("Elige una opción: ")

    if choice == '1':
        name = input("Nombre: ")
        phone = input("Teléfono: ")
        email = input("Email: ")
        contacts.append({'name': name, 'phone': phone, 'email': email})
        print("Contacto agregado.")
    elif choice == '2':
        name = input("Nombre del contacto a eliminar: ")
        found = False
        for contact in contacts:
            if contact['name'] == name:
                contacts.remove(contact)
                found = True
                print("Contacto eliminado.")
                break
        if not found:
            print("Contacto no encontrado.")
    elif choice == '3':
        name = input("Nombre del contacto a buscar: ")
        found = False
        for contact in contacts:
            if contact['name'] == name:
                print(f"Nombre: {contact['name']}, Teléfono: {contact['phone']}, Email: {contact['email']}")
                found = True
                break
        if not found:
            print("Contacto no encontrado.")
    elif choice == '4':
        for contact in contacts:
            print(f"Nombre: {contact['name']}, Teléfono: {contact['phone']}, Email: {contact['email']}")
    elif choice == '5':
        break
    else:
        print("Opción no válida.")
