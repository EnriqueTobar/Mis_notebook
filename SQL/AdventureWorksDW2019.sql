/* Descargar e importar base de datos AdventureWorksDW2019 a SQL Server
1. Descargar el archivo y pegar en la dirección
   C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup
2. Click derecho en Databases y luego en 'Restore Database...'
3. Seleccionar 'Device' buscar archivo 'ADD', agregar y cargar.  */

USE AdventureWorksDW2019
GO -- GO es un limitador de sentencia, SQL ejecutirá primero todo lo que está por encima de él.

/* Crear Diagramas 
1. Si se presentan problemas de autorización correr el siguiente script */

ALTER AUTHORIZATION ON DATABASE::AdventureWorksDW2019 TO sa
GO

/*
2. Luego Propiedades de la base de datos y en Files/Owner seleccionar ...
   para luego asignar autorizaciones.
*/

-- Tabla de Consumidores
SELECT
	*
FROM
	DimCustomer
ORDER BY
	DateFirstPurchase DESC

SELECT
	MaritalStatus, COUNT(MaritalStatus) AS N_MaritalStatus
FROM
	DimCustomer
GROUP BY
	MaritalStatus

-- Cantidad Autos que posee cada persona
SELECT
	NumberCarsOWned, COUNT(MaritalStatus) AS N_NumberCarsOWned
FROM 
	DimCustomer
GROUP BY 
	NumberCarsOWned
ORDER BY 
	NumberCarsOwned

SELECT * FROM DimCustomer
--SELECT DISTINCT EnglishCountryRegionName FROM DimGeography
SELECT * FROM FactInternetSales

SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'DimCustomer'

select e.BusinessEntityID, e.*,
d.Name
from HumanResources.Employee e 
inner join 
HumanResources.EmployeeDepartmentHistory h
on e.BusinessEntityID = h.BusinessEntityID
inner join HumanResources.Department d
on d.DepartmentID = h.DepartmentID
and h.EndDate is null
and d.Name in ('Quality Assurance', 'Production');

SELECT * FROM DimDate

