CREATE DATABASE sistema_solar;

USE sistema_solar;

CREATE TABLE planeta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    tipo VARCHAR(255),
    radio DECIMAL(10, 2),
    distancia_sol DECIMAL(10, 2)
);
  