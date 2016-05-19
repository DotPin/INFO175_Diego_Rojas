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
    fecha = ["2013-11-01","2013-11-30"]
    query = "select count([date]) as 'Ventas x Dia', [date] as 'Fecha', sum(net_total) as 'Total x Dia'  from sale where [date] between ? and ? group by [date]"
    resultado= c.execute(query,fecha)
    cnt_mnt = resultado.fetchall()
    con.close()
    return cnt_mnt 

def obt_cnt_dsc():
    con = conectar()
    c = con.cursor()
    query = "select product_id as 'Productos', count(product_id) as 'Cantidades', sum(net_unit_price) as 'Totales' from sale_product group by product_id order by count(product_id) DESC"
    #Sentencia limitada a 300 salidas query = "select product_id as 'Productos', count(product_id) as 'Cantidades', sum(net_unit_price) as 'Totales' from sale_product group by product_id order by count(product_id) DESC"
    resultado= c.execute(query)
    cnt_dsc = resultado.fetchall()
    con.close()
    return cnt_dsc 
  

  
if __name__ == "__main__":


  print "Ingrese una las siguientes opciones"
  print	"1 = ¿Cantidad total de ventas en el año 2013?"
  print "2 = ¿Precio promedio de venta por producto?"
  print "3 = ¿Total de ventas (gross_total) por cliente?"
  print "4 = ¿Total de ventas por cliente en el año 2014?"
  print "5 = ¿Cantidad y monto total de ventas por día en noviembre de 2013?"
  print "6 = ¿Cantidad y montos totales agrupados por producto en orden descendente según cantidad?"
  x = input("Ingrese la opción a revisar: ")
  
  if x == 1:
    cventas = obtener_cventas()		#¿Cantidad total de ventas en el año 2013
    print "Total de ventas realizadas  durante el 2013 es de: ",cventas[0]
      
  elif x == 2:
    pventas = obt_pventa()	#¿Precio promedio de venta por producto
    for a in pventas:
      print "Predio promedo de venta por producto, [Producto, Promedio]: ",a["product_id"], a["Promedio"]
      
  elif x == 3:
    vcliente = obt_vcliente()	#¿Total de ventas (gross_total) por cliente
    for b in vcliente:
      if b["Nombres"] == "":
	print "Total de ventas a clientes no identificados", b["Total"]
      else:
	print "total de ventas por cliente [Cliente , Total] ", b["Nombres"],b["Total"]
      
  elif x == 4:
    fcliente = obt_fcliente()	#¿Total de ventas por cliente en el año 2014
    for c in fcliente:
      if c["Nombres"] == "":
	print "Total de ventas del 2014 a clientes no identificados", c["Total"]
      else:
	print "total de ventas del 2014 por cliente [Cliente , Total] ", c["Nombres"],c["Total"]
      
  elif x == 5:
    cnt_mnt = obt_cnt_mnt()	#¿Cantidad y monto total de ventas por día en noviembre de 2013?
    for d in cnt_mnt:
      print "Cantidad y monto total de ventas Noviembre [Ventas x Dia , Fecha, Total x Dia ] ", d["Ventas x Dia"], d["Fecha"], d["Total x Dia"]
      
  elif x == 6:
    cnt_dsc = obt_cnt_dsc()	#¿Cantidad y montos totales agrupados por producto en orden descendente según cantidad?
    for e in cnt_dsc:
      if e["Productos"] == "" and e["Productos"] == "None":
	print "Cantidad y montos totales de productos desconocidos [Cantidades, Totales]: ", e["Cantidades"],e["Totales"]
      else:
	print "Cantidad y montos totales por productos [Producto, Cantidades, Totales]: ", e["Productos"], e["Cantidades"],e["Totales"]
  
  elif x != "":
     print "Numero no Válido"
	
#Program Edited By Hackerter.