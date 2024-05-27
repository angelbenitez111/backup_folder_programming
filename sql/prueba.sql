SELECT
      I.CODIGO,
      I.NOMBRE,
      A.AGENTE,
      A.SECCION,
      A.POLIZA, 
      A.ENDOSO, 
      H.ORDEN,
      A.NUMERO_FACTURA AS FACTURA, 
      A.EMISION, 
      A.DESDE, 
      A.HASTA,
      F.NOMBRE AS MARCA, 
      E.NOMBRE AS MODELO, 
      G.NOMBRE AS TIPO_VEHICULO,
      D.ANO, 
      D.CHASSIS,
      B.SUMA_ASEGURADA,
      A.PRIMA, 
      A.PREMIO
FROM
      FPOL A

inner join 
      FPOLARTICULOS B ON A.EMITIDO = B.EMITIDO AND
                      A.SECCION = B.SECCION AND
                      A.POLIZA = B.POLIZA AND
                      A.ENDOSO = B.ENDOSO

inner join FPOLARTCOD C on B.EMITIDO = C.EMITIDO and
      B.SECCION = C.SECCION and
      B.POLIZA = C.POLIZA and
      B.ENDOSO = C.ENDOSO and
      B.ARTICULO = C.ARTICULO

INNER JOIN 
      F521 D ON C.CODIGO = D.CODIGO
INNER JOIN 
      F522 E ON D.MARCA = E.MARCA
INNER JOIN 
      F522 F ON E.MARCA_PRINCIPAL = F.MARCA
INNER JOIN 
      F523 G ON D.TIPO_VEHICULO = G.CODIGO
INNER JOIN 
      FSERVICIOS_REALIZADOS H ON A.EMITIDO = H.EMITIDO AND
                      A.SECCION = H.SECCION AND
                      A.POLIZA = H.POLIZA AND
                      A.ENDOSO = H.ENDOSO
INNER JOIN 
      FCODGENERAL I ON A.ASEGURADO = I.CODIGO

WHERE 
      A.EMITIDO = 'N' AND
      A.SECCION = '0501' AND
      A.AGENTE = '0001690000' AND
      A.EMISION BETWEEN '2024-04-08' AND '2024-04-19' AND
      I.CODIGO = '000000066880000'

ORDER BY A.EMITIDO,
      A.SECCION,
      A.POLIZA,
      A.ENDOSO,
      H.ORDEN































select  A.AGENTE,
        A.POLIZA, 
        A.ENDOSO, 
        A.FACTURA, 
        A.EMISION, 
        A.DESDE, 
        A.HASTA,
        D.CHASSIS,
        F.MARCA as MARCA, 
        E.NOMBRE as MODELO, 
        D.ANO, 
        B.SUMA_ASEGURADA as RESP_MAXIMA,
        A.AGENTE,
        A.PRIMA, 
        A.PREMIO, 
from 
FPOL A

/*Marca, modelo*/
inner join FPOLARTICULOS B on A.EMITIDO = B.EMITIDO and
      A.SECCION = B.SECCION and
      A.POLIZA = B.POLIZA and
      A.ENDOSO = B.ENDOSO

inner join FPOLARTCOD C on B.EMITIDO = C.EMITIDO and
      B.SECCION = C.SECCION and
      B.POLIZA = C.POLIZA and
      B.ENDOSO = C.ENDOSO and
      B.ARTICULO = C.ARTICULO

inner join F521 D on C.CODIGO = D.CODIGO
inner join F522 E on D.MARCA = E.MARCA
inner join F522 F on E.MARCA_PRINCIPAL = F.MARCA

inner join F523 G on D.TIPO_VEHICULO = G.CODIGO
inner join F523 H on G.TIPO_PRINCIPAL = H.CODIGO

where 
    A.EMITIDO = 'N' and
    A.AGENTE = '0001690000'









































      
      



where 
      (A.SECCION = '0501' and
      A.AGENTE_PRINCIPAL = '0001690000') and
      A.HASTA >= current_date
order by A.EMITIDO,
    A.SECCION,
    A.POLIZA,
    A.ENDOSO  nro. de orden de instalación	 

    /*FDENTER - F521 AUTOMOVIL - */






select A.EMITIDO, A.SECCION, A.POLIZA, A.ENDOSO,
       FG.nombre AS COBRADOR,
       TC.nombre AS TIPO_COBRADOR,
       A.NUMERO_TARJETA AS NUMERO_EN_POLIZA,
       GB.NUMERO AS NUMERO_EN_ASEGURADO
from 
FPOL A
left join FASEG_TARJETA_DEBITO GB on A.ASEGURADO = GB.CODIGO and
      GB.COBRADOR = A.COBRADOR and
      GB.TIPO = A.TIPO_COBRADOR
LEFT JOIN f008_tipo_cobrador TC ON GB.tipo = TC.codigo
LEFT JOIN F008 F8 ON F8.cobrador = A.cobrador
INNER JOIN FCODGENERAL FG ON FG.codigo = F8.codigo_fcodgeneral
      
      
where 
      A.EMITIDO = 'N' and
      (A.SECCION = '0707' and
      A.POLIZA in (353)) or (A.SECCION = '0104' and
      A.POLIZA in (1985, 1988)) or (A.SECCION = '0401' and
      A.AGENTE_PRINCIPAL = '0001530000') and
      A.HASTA >= current_date
order by A.EMITIDO,
    A.SECCION,
    A.POLIZA,
    A.ENDOSO  

    /*FDENTER - F521 AUTOMOVIL - */

 select E.NOMBRE as ASEGURADO,
       A.EMITIDO,
       A.SECCION,
       A.POLIZA,
       A.ENDOSO,
       C.CHAPA,
       F.MARCA,
       F.MARCA_PRINCIPAL,
       case
         when A.MONEDA = 1 then 'Gs'
         else 'Us'
       end as MONEDA,
       A.PRIMA,
       A.PREMIO,
       A.SUMA_ASEGURADA,
       case A.TRANSFERENCIA
         when 'N' then 'No tiene Transferencia'
         when 'S' then 'Acreedor Prendario'
         when 'H' then 'Acreedor Hipotecario'
         when 'P' then 'Propietario del Bien Asegurado'
         when 'B' then 'Banco Fiduciario'
         when 'A' then 'Acreedor Quirografario'
         when 'D' then 'Depósitos y Warrant'
         when 'C' then 'Especial Cooperativas (Tajy)'
       end as TIPO_ACREEDOR,
       D.NOMBRE as ACREEDOR
from FPOL A
inner join FPOLARTCOD B on A.EMITIDO = B.EMITIDO and
      A.SECCION = B.SECCION and
      A.POLIZA = B.POLIZA and
      A.ENDOSO = B.ENDOSO
inner join F521 C on B.CODIGO = C.CODIGO
inner join FCODGENERAL D on A.COD_TRANSFERENCIA = D.CODIGO
inner join FCODGENERAL E on A.ASEGURADO = E.CODIGO
inner join F522 F on C.MARCA = F.MARCA
where A.TRANSFERENCIA = 'S' and
      A.HASTA >= current_date and
      A.ANULADA <> 'S' and
      A.TIPO in (1, 2, 5) and
      A.ASEGURADO in ('000005229160000', '000001287250000')
order by 1,
    2,
    3,
    4,
    5;



    /*FDENTER - F521 AUTOMOVIL - */


 select F.MARCA as MARCA, E.NOMBRE as MODELO, D.ANO, B.SUMA_ASEGURADA as RESP_MAXIMA,
       (select round(N.SUMA_ASEGURADA * A.CAMBIO)
        from FPOLCOB N
        where N.EMITIDO = B.EMITIDO and
              N.EMITIDO N.SECCION = B.SECCION and
              N.POLIZA = B.POLIZA and
              N.ENDOSO = N.ENDOSO and
              N.CODIGO_COBERTURA = 1) as COB_BASICA_1
       case
         when A.TIPO <> 3 then B.PRIMA * A.CAMBIO
         else (B.PRIMA * -1) * A.CAMBIO
       end as PRIMA
from FPOL A
inner join FPOLARTICULOS B on A.EMITIDO = B.EMITIDO and
      A.SECCION = B.SECCION and
      A.POLIZA = B.POLIZA and
      A.ENDOSO = B.ENDOSO
inner join FPOLARTCOD C on B.EMITIDO = C.EMITIDO and
      B.SECCION = C.SECCION and
      B.POLIZA = C.POLIZA and
      B.ENDOSO = C.ENDOSO and
      B.ARTICULO = C.ARTICULO

inner join F521 D on C.CODIGO = D.CODIGO
inner join F522 E on D.MARCA = E.MARCA
inner join F522 F on E.MARCA_PRINCIPAL = F.MARCA
where A.SECCION_PRINCIPAL = '0500' and
      A.EMISION between '01/01/2023' and '31/01/2023'
order by A.EMITIDO, A.SECCION, A.POLIZA, A.ENDOSO, A.TIPO