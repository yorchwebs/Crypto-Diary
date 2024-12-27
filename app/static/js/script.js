function actualizar(){$('#precios').load(document.URL +  '  #precios');}

//Función para actualizar cada 5 segundos(5000 milisegundos)
setInterval("actualizar()",1000);