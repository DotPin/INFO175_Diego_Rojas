# -*- coding: utf-8 -*- 
#¿Cantidad total de ventas en el año 2013? OK
#¿Precio promedio de venta por producto? OK
#¿Total de ventas (gross_total) por cliente? 
#¿Total de ventas por cliente en el año 2014?
#¿Cantidad y monto total de ventas por día en noviembre de 2013?
#¿Cantidad y montos totales agrupados por producto en orden descendente según cantidad?

import sqlite3

def conectar():
    con = sqlite3.connect('pos_empresa.bin')
    con.row_factory = sqlite3.Row
    return con
    
def obtener_cventas():
    con = conectar()
    c = con.cursor()
    fecha = ["2013-01-01", "2013-12-31"]
    query = ("select sum(gross_total) from sale where [date] between ? and ? ")
    resultado= c.execute(query,fecha)
    cventas = resultado.fetchone() #entrega tupla de datos en raw
    con.close()
    return cventas

def obt_pventa():
    con = conectar()
    c = con.cursor()
    #a = "Promedio"
    query = "select product_id, AVG(net_unit_price) as 'Promedio' from sale_product group by product_id"
    resultado= c.execute(query)
    pventas = resultado.fetchall() #entrega kmo tupla de datos string
    con.close()
    return pventas

def obt_vcliente():
    con = conectar()
    c = con.cursor()
    query = "select entity.names as 'Nombres' , count(sale.gross_total) as 'Total' from sale JOIN entity where sale.entity_id = entity.id group by entity.names"
    resultado= c.execute(query)
    vcliente = resultado.fetchall()
    con.close()
    return vcliente 

def obt_fcliente():
    con = conectar()
    c = con.cursor()
    fecha = ["2014-01-01","2014-12-31"]
    query = "select entity.names as 'Nombres' , count(sale.gross_total) as 'Total' from sale JOIN entity where sale.entity_id = entity.id and sale.[date] between ? and ? group by entity.names"
    resultado= c.execute(query,fecha)
    fcliente = resultado.fetchall()
    con.close()
    return fcliente 

def obt_cnt_mnt():
    con = conectar()
    c = con.cursor()
    query = ""
    resultado= c.execute(query)
    cnt_mnt = resultado.fetchall()
    con.close()
    return cnt_mnt 
  
  

if __name__ == "__main__":

    cventas = obtener_cventas()		#¿Cantidad total de ventas en el año 2013
    print "Total de ventas realizadas  durante el 2013 es de: ",cventas[0]
    
    pventas = obt_pventa()	#¿Precio promedio de venta por producto
    for a in pventas:
      print "Predio promedo de venta por producto, [Producto, Promedio]: ",a["product_id"], a["Promedio"]
      
    vcliente = obt_vcliente()	#¿Total de ventas (gross_total) por cliente
    for b in vcliente:
      if b["Nombres"] == "":
	print "Total de ventas a clientes no identificados", b["Total"]
      else:
	print "total de ventas por cliente [Cliente , Total] ", b["Nombres"],b["Total"]
    
    fcliente = obt_fcliente()	#¿Total de ventas por cliente en el año 2014
    for c in fcliente:
      if c["Nombres"] == "":
	print "Total de ventas del 2014 a clientes no identificados", c["Total"]
      else:
	print "total de ventas del 2014 por cliente [Cliente , Total] ", c["Nombres"],c["Total"]
    
    cnt_mnt = obt_cnt_mnt()