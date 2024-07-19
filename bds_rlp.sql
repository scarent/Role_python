show FULL TABLES FROM sql10720721;
--select--
select * from Personaje
select * from Raza
select * from Estado
select * from Usuario
select * from Habilidad
select * from Equipamiento
select * from Poder 
select * from Usuario 
--Insert--
Insert INTO sql10720721.Personaje (id_personaje,nombre_personaje,nombre_jugador,id_raza, nivel,id_estado,id_usuario) values (3,"pedro","Leon",1,4,1 ,1);
insert Into Raza (id_raza,nombre_raza) values (2,"FUEGAZ");
Insert Into Estado(Id_estado,Nombre_estado) values (2,"Muerto")
Insert Into Usuario (id_usuario,nombre_usuario,contrasenia,tipo_usuario) value (2,"Jose","12345","Gm")
Insert into Habilidad (id_habilidad,nombre_habilidad,detalle,id_raza) value (4,"puno","golpe QUITA 10VIDA",2)
insert into Equipamiento(id_equipamiento,nombre_equipamiento) values(3,"Armadura")
insert into Poder(id_poder,nombre_poder,detalle,id_raza) value (3,"llamarada","--",1)
 SELECT Raza.nombre_raza, Poder.nombre_poder, Poder.detalle
        FROM Poder
        JOIN Raza ON Poder.id_raza = Raza.id_raza
        ORDER BY Raza.nombre_raza, Poder.nombre_poder
      
Personaje.nombre_personaje,
    Raza.nombre_raza,
    Personaje.nivel,
    Estado.nombre_estado
FROM 
	Personaje
JOIN 
	Raza on Personaje.id_raza= Raza.id_raza
JOIN
	Estado ON Personaje.id_estado=Estado.id_estado;
CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    tipo_usuario ENUM('GM', 'Jugador') NOT NULL
);
id_equipamiento
-- Tabla Raza
CREATE TABLE Raza (
    id_raza INT PRIMARY KEY AUTO_INCREMENT,
    nombre_raza VARCHAR(50) NOT NULL
);

-- Tabla Estado
CREATE TABLE Estado (
    id_estado INT PRIMARY KEY AUTO_INCREMENT,
    nombre_estado VARCHAR(50) NOT NULL
);

-- Tabla Personaje
CREATE TABLE Personaje (
    id_personaje INT PRIMARY KEY AUTO_INCREMENT,
    nombre_personaje VARCHAR(50) NOT NULL,
    nombre_jugador VARCHAR(50) NOT NULL,
    id_raza INT,
    nivel INT DEFAULT 1,
    id_estado INT,
    id_usuario INT,
    FOREIGN KEY (id_raza) REFERENCES Raza(id_raza),
    FOREIGN KEY (id_estado) REFERENCES Estado(id_estado),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Tabla Habilidad
CREATE TABLE Habilidad (
    id_habilidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_habilidad VARCHAR(50) NOT NULL,
    detalle TEXT,
    id_raza INT,
    FOREIGN KEY (id_raza) REFERENCES Raza(id_raza)
);

-- Tabla Poder
CREATE TABLE Poder (
    id_poder INT PRIMARY KEY AUTO_INCREMENT,
    nombre_poder VARCHAR(50) NOT NULL,
    detalle TEXT,
    id_raza INT,
    FOREIGN KEY (id_raza) REFERENCES Raza(id_raza)
);

-- Tabla Equipamiento
CREATE TABLE Equipamiento (
    id_equipamiento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_equipamiento VARCHAR(50) NOT NULL
);

-- Tabla Personaje_Habilidad
CREATE TABLE Personaje_Habilidad (
    id_personaje INT,
    id_habilidad INT,
    PRIMARY KEY (id_personaje, id_habilidad),
    FOREIGN KEY (id_personaje) REFERENCES Personaje(id_personaje),
    FOREIGN KEY (id_habilidad) REFERENCES Habilidad(id_habilidad)
);

-- Tabla Personaje_Poder
CREATE TABLE Personaje_Poder (
    id_personaje INT,
    id_poder INT,
    PRIMARY KEY (id_personaje, id_poder),
    FOREIGN KEY (id_personaje) REFERENCES Personaje(id_personaje),
    FOREIGN KEY (id_poder) REFERENCES Poder(id_poder)
);

-- Tabla Personaje_Equipamiento
CREATE TABLE Personaje_Equipamiento (
    id_personaje INT,
    id_equipamiento INT,
    PRIMARY KEY (id_personaje, id_equipamiento),
    FOREIGN KEY (id_personaje) REFERENCES Personaje(id_personaje),
    FOREIGN KEY (id_equipamiento) REFERENCES Equipamiento(id_equipamiento)
);