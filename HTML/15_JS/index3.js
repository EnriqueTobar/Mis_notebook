// Funciones: se definen con function

function sumar(a ,b ,cb) {
    const r = a + b
    cb(r)
}

function callback(result) {
    console.log('resultado', result);
}
//callback(6)
//sumar(2, 3, callback);

// fat arrow functions: otra forma, no requiere de function
// primer ejemplo directo
const miFatArrowFunction = (a, b) => a + b
//const r = miFatArrowFunction(1, 2)
//console.log(r);

//  segundo ejemplo con llaves para indicar el return 
const otraFAF = (a, b) => {
    return a + b
}
const r = otraFAF(1,3)
//console.log(r);

// funcion anonima
sumar(2, 3, function(r) {
    console.log('Soy una funcion anonima y mi resultado es:', r)
})