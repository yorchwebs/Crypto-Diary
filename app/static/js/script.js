const carrusel = document.querySelector(".carrusel-items");

        let maxScrollLeft = carrusel.scrollWidth - carrusel.clientWidth;
        let intervalo = null;
        let step = 1;
        const start = () => {
        intervalo = setInterval(function () {
            carrusel.scrollLeft = carrusel.scrollLeft + step;
            if (carrusel.scrollLeft === maxScrollLeft) {
            step = step * -1;
            } else if (carrusel.scrollLeft === 0) {
            step = step * -1;
            }
        }, 10);
        };

        const stop = () => {};

        start();

function actualizar(){$('#precios').load(document.URL +  '  #precios');}

//Función para actualizar cada 5 segundos(5000 milisegundos)
setInterval("actualizar()",1000);