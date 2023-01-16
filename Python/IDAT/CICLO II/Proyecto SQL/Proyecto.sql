CREATE DATABASE OASIS
GO

USE OASIS
GO

CREATE TABLE TBL_CLIENTE(
DNI VARCHAR(9)NOT NULL PRIMARY KEY,
NOMBRE VARCHAR(15)NOT NULL,
APELLIDO VARCHAR(20)NOT NULL,
TELEFONO VARCHAR(10)NOT NULL,
)
GO

CREATE TABLE TBL_RT_PEDIDOS(
REGISTRO_PE INT IDENTITY(1,1)NOT NULL PRIMARY KEY,
DNI VARCHAR(9) FOREIGN KEY REFERENCES TBL_CLIENTE(DNI),
COD_VENTA VARCHAR(8) FOREIGN KEY REFERENCES TBL_VENTA(COD_VENTA),
DIRECCION VARCHAR(25)NOT NULL,
PRODUCTO VARCHAR(20)NOT NULL,
BEBIDAS VARCHAR(20)NOT NULL,
FECHA DATE
)
GO

CREATE TABLE TBL_PERSONAL(
COD_PERSONAL VARCHAR(6) NOT NULL PRIMARY KEY,
NOMBRE VARCHAR(20) NOT NULL,
TELEFONO VARCHAR(10)NOT NULL,
FECHA DATE NOT NULL,
)
GO

CREATE TABLE TBL_VENTA(
COD_VENTA VARCHAR(8) NOT NULL PRIMARY KEY,
COD_PERSONAL VARCHAR(6) FOREIGN KEY REFERENCES TBL_PERSONAL(COD_PERSONAL),
MONTO_FINAL VARCHAR(6) NOT NULL,
TIPO_VENTA VARCHAR(9) NOT NULL,
FECHA DATE 
)
GO

CREATE TABLE TBL_HORARIO(
PERSONAL VARCHAR(6) FOREIGN KEY REFERENCES TBL_PERSONAL(COD_PERSONAL),
AREA VARCHAR(10) NOT NULL,
)
GO



INSERT INTO TBL_CLIENTE VALUES ('333555','Jefferson','Vicuña','999222111'),
							   ('555888','Khennet','Kilua','111222444'),
							   ('444777','Anthony','Gomez','222555888'),
							   ('666555','Naomi','Torres','333111222'),
							   ('884123','Miguel','Ander','444222111'),
							   ('987546','Juan','Kiko','777111222'),
							   ('365412','Roberto','Huartez','555444111'),
							   ('854712','Jose','Humala','666222888'),
							   ('369541','Ignacio','Ramirez','999111555'),
							   ('256987','Pedro','Kilua','666533222'),
							   ('123654','Anai','Antauro','999332223'),
							   ('854123','Sebastian','Toso','777111555')
SELECT * FROM TBL_CLIENTE
GO

INSERT INTO TBL_PERSONAL VALUES ('10','Matias','965412111','2018-10-04'),
								('20','Torino','856332145','2018-10-10'),
								('30','Alexander','669874521','2018-10-20'),
								('40','Gilberto','975698445','2018-11-01'),
								('50','Tupac','974897888','2018-11-05'),
								('60','Mike','998977451','2018-12-25')
SELECT * FROM TBL_PERSONAL
GO

INSERT INTO TBL_VENTA VALUES ('201','60','120','TARJETA','2022-06-05'),
							 ('202','30','60','TARJETA','2022-06-20'),
							 ('203','50','300','TARJETA','2022-06-21'),
							 ('204','10','45','EFECTIVO','2022-06-21'),
							 ('205','60','50','EFECTIVO','2022-06-22'),
							 ('206','40','100','TARJETA','2022-06-22'),
							 ('207','20','20','EFECTIVO','2022-06-23'),
							 ('208','10','85','EFECTIVO','2022-06-24')
SELECT * FROM TBL_VENTA
GO

INSERT INTO TBL_HORARIO VALUES ('10','COCINERO'),
							   ('20','COCINERO'),
							   ('30','MESERO'),
							   ('40','MESERO'),
							   ('50','COCINERO'),
							   ('60','COCINERO')
SELECT * FROM TBL_HORARIO
GO


INSERT INTO TBL_RT_PEDIDOS VALUES ('854123','202','S.J.L','Causa limeña','Chicha de Jora','2022-12-02'),
								  ('333555','201','Av.Las Flores','Pachamanca','Chicha Morada','2022-12-02'),
								  ('854712','204','Av. 12','Tacu tacu','Chicha Morada','2022-12-02'),
								  ('369541','206','Av. 5','Arroz chaufa','Chicha de Jora','2022-12-03'),
								  ('666555','208','Av. 2','Anticuchos','Chicha Morada','2022-12-03'),
								  ('256987','205','Av.Las Flores','Lomo saltado','Chicha de Jora','2022-12-03'),
								  ('444777','203','Av. 60','Ceviche','Chicha Morada','2022-12-03'),
								  ('884123','207','Av. 4','Anticuchos','Chicha de Jora','2022-12-04')
SELECT * FROM TBL_RT_PEDIDOS
GO


-- Mostrar todos los registros de la tabla cliente con el nombre Jefferson
SELECT * FROM TBL_CLIENTE where Nombre='Jefferson'

-- Actualizar el nombre de MIGUEL por el nombre Kiko
SELECT * FROM TBL_CLIENTE where Nombre='MIGUEL'
UPDATE TBL_CLIENTE SET nombre = 'Kiko' WHERE DNI = 854123;
SELECT * FROM TBL_CLIENTE 
 
-- MOSTRAR todos los clientes con la primera letra de su nombre
SELECT * FROM TBL_CLIENTE WHERE NOMBRE LIKE 'R%'

-- Mostrar ventas cuyos montos sean entre 100 y 500
SELECT * FROM TBL_VENTA WHERE MONTO_FINAL BETWEEN 100 AND 500

-- Mostrar ventas del personal 60 con cantidades entre 10 y 150
SELECT * FROM TBL_VENTA WHERE (COD_PERSONAL = 60 AND MONTO_FINAL BETWEEN 10 AND 150)