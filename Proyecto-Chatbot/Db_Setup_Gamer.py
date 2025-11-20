import sqlite3 # Se empieza importando sqlite3 que es un modulo que casi siempre al instalar python o python3 ya viene integrado y es una base de datos ligera, sin servidor y basadas en disco.
               # Le permite a uno mediante python usar el lenguaje sql para crear tablas, insertar, manipular y consultar datos, en este caso es buena para prototipos o proyectos no muy grandes.

def proyecto_db(db_nombre="pc_gamer.db"):  # Se usa una funcion para una mayor organizacion y calidad, reutilizar el codigo y controlar cuando debe ejecutarse.
    conexion = sqlite3.connect(db_nombre) # Variable conexion que tiene sqlite3.connect (un objeto), y se gestiona y establece la union con el nombre del archivo y la base de datos.
    cursordb = conexion.cursor() # Otra variable que tiene la variable anterior "conexion" y "cursor" la cual es un objeto que TE PERMITE ejecutar comandos SQL dentro de python.
     
     # Abajo se encuentra .execute la cual es el objeto que ya puedes hacer comandos usando SQL, a su vez se crea una tabla la cual tendra los componentes junto con sus campos y su tipo de dato
    cursordb.execute(''' CREATE TABLE componentesPC (
                       
                     id INTEGER PRIMARY KEY,
                     tipo TEXT NOT NULL,
                     modelo TEXT NOT NULL UNIQUE,
                     precio REAL NOT NULL,
                     socket TEXT,
                     tipo_ram TEXT,
                     potencia_w REAL
                                                   );
                                                        ''') 
    
    # Se crea otra tabla la cual contiene los id (identificadores y son enteros) y la construccion de la pc
    cursordb.execute('''
        CREATE TABLE IF NOT EXISTS construccionPC (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            estimacion_minima REAL,
            cpu_id INTEGER NOT NULL,
            gpu_id INTEGER NOT NULL,
            placa_madre_id INTEGER NOT NULL,
            fuente_poder_id INTEGER NOT NULL,
            ram_id INTEGER NOT NULL,

            FOREIGN KEY(cpu_id) REFERENCES componentesPC(id),
            FOREIGN KEY(gpu_id) REFERENCES componentesPC(id),
            FOREIGN KEY(placa_madre_id) REFERENCES componentesPC(id),
            FOREIGN KEY(fuente_poder_id) REFERENCES componentesPC(id),
            FOREIGN KEY(ram_id) REFERENCES componentesPC(id)
        ); 
    ''')
    # Usando la variable conexion y commit, la cual es para terminar de confirmar cambios en la base de datos y tambien para modificar sentencias como INSERT, UPDATE y/o DELETE
    conexion.commit()
    # Como su nombre indica, cierra la conexion de la base de datos cuando se haya terminado de usar
    conexion.close()


# Se crea otra funcion en la cual comienza igual que la anterior, osea, conectando la base de datos y cursor para ejecutar comandos, solo que aqui ya ingresamos datos
def componentes_db(db_nombre="pc_gamer.db"):
    conexion = sqlite3.connect(db_nombre)
    cursordb = conexion.cursor()
    # Se crea una variable componentes en los que [ es una lista en la que introducimos datos como Cpu, Gpu, PlacaMadre y la FuentePoder con sus modelos, precios, socket, tipo de ram y potencia de vatios 
    componentes = [
        ('Cpu',  'Ryzen 9 9950X3D',   800.0,   'AM5',   'DDR5',   120),
        ('Cpu',  'Ryzen 7 9800X3D',   479.0,   'AM5',   'DDR5',   120),
        ('Cpu',  'Ryzen 5 7600X',   250.0,   'AM5',   'DDR5',   105),
        ('Cpu',  'Ryzen 5 5600',   130.0,   'AM4',   'DDR4',   65),
        ('Cpu',  'Core i7-15700K',   400.0,   'LGA1851',   'DDR5',   125),
        ('Cpu',  'Core i5-13400F',   195.0,   'LGA1700',   'DDR4/DDR5',   65),

        ('Gpu',   'GeForce RTX 5090',   2000.0,   'PCIe x16',   'GDDR7',   450),
        ('Gpu',   'GeForce RTX 5090',   600.0,   'PCIe x16',   'GDDR7',   200),
        ('Gpu',   'GeForce RTX 5080',   1100.0,   'PCIe x16',   'GDDR7',   320),
        ('Gpu',   'GeForceRTX 3060',   320.0,   'PCIe x16',   'GDDR6',   170),

        ('PlacaMadre',  'Chipset Asus Z890',   429.0,   'LGA1851',   'DDR5',   6),
        ('PlacaMadre',  'Chipset X870E',   250.0,   'AM5',   'DDR5',   14),
        ('PlacaMadre',  'Chipset Z890',   230.0,   'LGA1851',   'DDR5',   6),
        ('PlacaMadre',  'Chipset B650',   180.0,   'AM5',   'DDR5',   7),
        ('PlacaMadre',  'Chipset B550',   110.0,   'AM4',   'DDR4',   7),
        ('PlacaMadre',  'Chipset B769',   160.0,   'LGA1700',   'DDR4/DDR5',   6),

        ('FuentePoder',   'Fuente 750W',   90.0,   'Conexión ATX',   'No usan',   750),
        ('FuentePoder',   'Fuente 550W ',   50.0,   'Conexión ATX',   'No usan', 550),
        ('FuentePoder',   'Fuente 1000W ',   200.0,   'Conexión ATX',   'No usan', 1000),

        ('Ram',   'DDR5 48GB 8000mhz',   300.0,   'DIMM',   'DDR5',   7),
        ('Ram',   'DDR5 32GB 6000mhz',   145.0,   'DIMM',   'DDR5',   5),
        ('Ram',   'DDR5 32GB 6000mhz',   120.0,   'DIMM',   'DDR5',   5),
        ('Ram',   'DDR4 16GB 3200mhz',   50.0,   'DIMM',   'DDR4',   3),
    ]
    # Llamamos la variable cursordb junto con executemany, la cual usando comandos SQL insertamos dentro de la variable componentes los tipos, modelos, precio, socket, tipo de ram y potencia en vatios los datos anteriormente escritos 
    cursordb.executemany('''
                        INSERT OR IGNORE INTO componentesPC (tipo, modelo, precio, socket, tipo_ram, potencia_w)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', componentes)     
    conexion.commit()
    print(f"{cursordb.rowcount} componentes insertados o actualizados.") # Rowcount devuelve el numero de filas modificadas por la ultima instruccion ejecutada
    conexion.close()
# __name__ es una variable especial ya integrada en python que almacena el nombre del modulo actual, solo se ejecutara cuando corramos el codigo
# Tambien tiene mas usos como importar el archivo como en un modulo en otro archivo como por ejemplo import Db_Setup_Gamer sin poner .py
# proyecto_db y componentes_db qué son el nombre de las 2 funciones que inician las bases de datos, su finalidad es encender el programa cuando se ejecute if name
if __name__ == '__main__':
    proyecto_db()
    componentes_db() 
