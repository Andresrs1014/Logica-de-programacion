class Participant():
    
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Olimpycs:
    
    def __init__(self):
        self.events = []
        self.participants = {}
    
    
    def register_event(self):
        event = input('introduce el nombre del evento deportivo').strip
        
        if event in self.events:
            print(f'El evento {event} ya ha sido registrado. ')
        else:
            print(f'El evento {event} ha sido registrado')
        
        self.events.append(event)
        
    def register_participant(self):
        
        if not self.events:
            print('No hay eventos registrados, registra uno antes de registrar participantes')
            return 
        
        name = input('Introduce el nombre del participante: ').strip
        country = input('Introducre el pais del participante: ').strip
        participant = Participant(name, country)
        
        print('Eventos deportivos disponibles disponibles')
        
        for index, event in enumerate(self.events):
            print(f'{index + 1}. {event}')
            
        event_choice = int(input('Selecciona el numero del evento para asignar al participante: ')) - 1
    
        if event_choice >= 0 and event_choice < len(self.events):
            
            event = self.events[event_choice]
            
            if participant in self.participants[event]:
                print(f'El participante {participant} del pais {country} ya ha sido registrado en {event}, no puede ser registrado nuevamente ')
            else:
                self.participants[event].append(participant)
                print(f'El participante {participant} del pais {country} ha sido registrado en {event}')
            
            
       




 
 
olimpycs = Olimpycs()
 
print('\n Simulador de Juegos Olimpicos ')

 
while True:
    
    print()
 
    print('1. Registro de eventos.')
    print('2. Registro de participantes.')
    print('3. Simulación de eventos.')
    print('4. Creación de informes.')
    print('5. Salir del programa.')
    
    option = input('Elige una opcion: ')
    
    
    match option:
        case '1':
            olimpycs.register_event()
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            print('Saliendo del simulador..')
            break
        case _:
            print('Opcion invalida, por favor elige una nueva')    
    

  
  

 
 