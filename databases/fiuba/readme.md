# Resumen de la materia de base de datos.

## NOMENCLATURA
             (min_2, max_2)                       (min_1, max_1)
[ENTIDAD_1] -------------------------@-------------------------- [ENTIDAD_2]
1. La cardinalidad se expresa en el lado opuesto
2. si el min = 0, significa participación parcial, ya que es optativo
3. si el min=1 y max=1, significa participación total, es decir hay un A para cada B y viceversa
4. si el min=1 y max=4, significa participación parcial, conociendo el destino no es posible reconstruir el origen.

## MODELO RELACIONAL

**DOMINIO**: Conjunto de valores homogéneos (mismo tipo)
  - D1 = {Barcelona, Sevilla, Bs As}
**PRODUCTO CARTESIANO**: Todas las combinaciones que pueden obtenerse con el dominio de 2 atributos
  - $\{(a, b) : a\in A, b\in B \}
  - $D1\times D2$ = {(Barcelona, Argentina), (Barcelona, España), ... (Bs As, España)}
**RELACION**: Subconjunto del producto cartesiano
  - R = {(Barcelona, España) .. (Bs As, Argentina)}

--- 

**ESQUEMA DE RELACION**: Nombre de relación seguido por lista de atributos
  - R(A1 .. An)
  - Peliculas(nombre, año, num. oscars)
**DOMINIO DE ATRIBUTO**: Los valores que dicho atributo puede tomar
  - D(nombre) = string
  - D(año) = datetime
  - D(num. oscars) = Naturales
**ESQUEMA DE BASE DE DATOS**: Conjunto de esquemas de relación junto a Conjunto de restricciones de integridad
  - S = {R1 .. Rm}
  - **Cine** = {**Peliculas**(nombre, año, oscars), **Actores**(nombre, pais), **Actuaciones**(nombre_actor)}

---

**TUPLA**: una instancia de la relación
  - (kill bill, 2003, 0)
**VALOR**: instancia de un atributo de una tupla
  - t[A]=t.A
  - t[nombre] = t.nombre = "kill bill"
**CARDINALIDAD**: Cantidad de tuplas que posee la relación
  - n(R)
  - n(Peliculas) = 4 (si guardaste 4 peliculas)

### RESTRICCIONES
**Nota.** Los atributos deben ser atómicos, no se permite compuestos o multivaluados

**RESTRICCIONES DE DOMINIO**: el valor del A de una tupla t debe pertenecer al dom(A)
  - t_1[nombre] = 8. MAL
  - t_2[nombre] = Kill bill. BIEN
  - t_3[nombre] = NULL. Nulo era o no parte del dominio?
**RESTRICCIONES DE UNICIDAD**: No pueden existir t_1 y t_2 que coincidan en los valores de todos sus atributos
  - t_1=(Kill Bill, 2003, 0)
  - t_2=(Kill Bill, 2003, 0) . MAL
  **SUPERCLAVE**: subconjunto de atributos que identifican unicamente a la tupla
    - {nombre, año, oscars} . BIEN (nombre unico)
    - {nombre, oscars}      . BIEN
    - {oscars}              . MAL, sabiendo num. oscars no sabes que peli era
    **CLAVE PRIMARIA**: El conjunto minimal de superclaves
      - {nombre}            . Con esto ya identifico a la pelicula

**RESTRICCION DE INTEGRIDAD**
  **DE ENTIDAD**: La clave primaria no puede tomar el valor nulo
    - Pelicula("", 2000, 0) . mal, debe tener un nombre
  **REFERENCIAL**: Los atributos de la clave foránea deben referir a entidades existentes
    - Si un actor interpretó Star Wars, dicha película debe existir
    - Sean R(A1 .. An) y S(B1 .. Bm) dos relaciones de entidad
      - $FK \subset \{A1 .. An\}$ . Sea FK la **clave foranea** de S en R
      - $PK \subset \{B1 .. Bm\}$ . Sea Pk la **clave primaria** de S
      - Entonces: 
        - para todas las tuplas t_i no nulas, existe una tupla s que puede ser referenciada por FK
         $\forall t \in R: t[FK]\neq Null \rightarrow \exists s\in s : s[PK]=t[FK]$

      
### OPERACIONES
- Operaciones de consulta (Read)
  - Al no modificar nada, no violan restricciones
- Operaciones de actualización (Write)
  - Inserción: al insertar una tupla se puede violar
    - Restricciones de dominio
    - Restricciones de unicidad
    - Restricciones de integridad de entidad
    - Restricciones de integridad referencial
    - SOLUCION: RECHAZAR OPERACION
  - Eliminación: Puede violar
    - Restricciones de integridad referencial
    - SOLUCION:
      - RECHAZAR OPERACION
      - ELIMINAR EN CASCADA (todos los que me hacían referencia, desaparecen)
      - PONER EN NULO (a todos los que me hacían referencia)
  - Modificación:
    - Clave Foránea: verificar integridad referencial
    - Clave Primaria:
      - Verificar restriccion de integridad de entidad
      - Verificar restriccion de integridad referencial
     

**TRANSACCIONES**: Conjunto ordenado de operaciones que o se ejecutan todas o ninguna
  - En caso de violar alguna restriccion, se deben deshacer los cambios

### PASAJE DE MODELOS
**CASO 1** Entidad con atributos

![](1.jpg)
```
Pais(Nombre PK, poblacion, area)
```
**CASO 2** Atributos Multivaluados
- los atributos multivaluados se modelan con una tabla o relación aparte
  
![](2.jpg)

```
Medicos(legajo PK, nombre)
Telefonos(legajo FK PK, telefono PK)
Mails(legajo FK PK, mail PK)
```

**CASO 3** Atributos Compuestos
- los sub-atributos se incluyen como si fuesen atributos normales

![](3.jpg)

```
Tarjeta(MII PK, issuer_subid PK, cuenta PK, checksum PK, fecha_venc)
```

**CASO 4** INTERRELACION CON CARDINALIDAD ARBITRARIA
- Aprobaciones necesita ambas claves foráneas para definirse,
  - entonces tanto padrón como código son PK

![](4.jpg)
```
Alumnos(padron PK, nombre) #Entidad 1
Asignaturas(codigo PK, nombre) #Entidad 2
Aprobaciones(padron PK FK, codigo PK FK, fecha) #Interrelación
```

**CASO 5** INTERRELACION CON CARDINALIDAD 1:1
- Cuando la cardinalidad es 1, saber el gerente sabe el dpto.
  - sólo una PK es necesaria para definir la relación
- El viceversa también es válido
  
![](5.jpg)

```
Gerentes(nombre_gerente PK, tel, mail)
Departamentos(codigo PK, nombre)
Dirige(nombre_gerente FK PK, codigo FK)
```

**CASO 6** INTERRELACION CON CARDINALIDAD 1:1 Y PARTICIPACION TOTAL DE UNA ENTIDAD
- Si además una entidad tiene participación total,
  - se escoje esa entidad como clave primaria de la relación
- En este caso Gerente tiene participación total
  - cada gerente tiene un departamento, pero además existen dptos sin asignar.
- En este caso nos ahorramos la tabla 'dirige'
  - y gerente toma la FK del dpto
    
![](6.jpg)

```
Gerentes(nombre_gerente PK, telefono, mail, codigo_dpto FK)
Departamentos(codigo PK, nombre_dpto)
```
**CASO 7** INTERRELACION CON CARDINALIDAD 1:1 Y PARTICIPACION TOTAL DE AMBAS ENTIDADES
- En este caso particular, definir al gerente define al dpto y viceversa.
- Es posible ahorrarse dos tablas,
- luego una sóla PK (gerente o dpto) es suficiente para definir una super tupla.
  
![](7.jpg)

```
GerentesDepartamentos(nombre_gerente PK, tel, mail, codigo_dpto, nombre_dpto)
```
**CASO 8** INTERRELACION CON CARDINALIDAD 1:N 
- El caso general usa 3 tablas
- Determinar el futbolista, determina el club
- Así que la tabla usa como PK el que tiene cardinalidad 1
  
![](8.jpg)

```
Futbolistas(nombre_fut PK, f_nac, pais)
Clubes(nombre_club PK, pais PK, division)
JuegaEn(nombre_fut FK PK, nombre_club FK, pais FK)
```

**CASO 9** INTERRELACION CON CARDINALIDAD 1:N Y PARTICIPACION TOTAL
- Aqui nos ahorramos una tabla
- En este caso existen clubes vacíos
- Pero cada jugador pertenece a un único club.
  - Determinar al futbolista determina el club,
    - el recíproco, conocer el club puede tener jugadores nulos y la tupla queda mal formada
  - El futbolista tiene el FK del club
    
![](9.jpg)

```
Futbolistas(nombre_fut PK, f_nac, pais_fut, nombre_club FK, pais_club FK)
Clubes(nombre_club PK, pais_club PK, division)
```
