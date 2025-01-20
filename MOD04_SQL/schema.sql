DROP DATABASE IF EXISTS supermercado;

CREATE DATABASE IF NOT EXISTS supermercado;

USE supermercado;

CREATE TABLE IF NOT EXISTS tiendas(
    id_tienda INT AUTO_INCREMENT PRIMARY KEY,
    tienda VARCHAR (25) NOT NULL,
    direccion VARCHAR (255),
    ciudad VARCHAR(25));

CREATE TABLE IF NOT EXISTS empleados(
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    empleado VARCHAR (255) NOT NULL,
    puesto VARCHAR (25) NOT NULL, 
    id_tienda INT,
    FOREIGN KEY (id_tienda) REFERENCES tiendas(id_tienda));

CREATE TABLE IF NOT EXISTS categorias(
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR (25) NOT NULL);

CREATE TABLE IF NOT EXISTS productos(
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR (255) NOT NULL,
    precio DECIMAL (10, 2) NOT NULL,
    stock INT NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria));

CREATE TABLE IF NOT EXISTS clientes(
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (50) NOT NULL,
    apellido VARCHAR (50) NOT NULL,
    email VARCHAR (255),
    codigo_postal INT);

CREATE TABLE IF NOT EXISTS ordenes(
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_empleado INT NOT NULL, 
    fecha_orden DATE NOT NULL,
    metodo_pago ENUM ('tarjeta', 'efectivo'),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));

CREATE TABLE IF NOT EXISTS detalle_orden(
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL (10, 2) NOT NULL,
    descuento DECIMAL (4,2) DEFAULT NULL,
    FOREIGN KEY (id_orden) REFERENCES ordenes(id_orden),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto));