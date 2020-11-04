console.log('Hola Mundo')

// Comentario en JS
// Tipos de datos en JS
// String: cadena de caracteres. 'a' comillas simples
// Boolean: true false.
// Null: es un valor, cuyo significado es vacio.
// Number: 123143 - no necesita comillas
// "123" distinto a 123
// Undefined
// Object: objeto. estructuras que nos permite agrupar datos.

// Definición de Variables en JS
//var :intentaremos evitarla debido a que al declararla JS lo interpreta como si estuviera en el inicio
//let :principal forma para definir variables

let miPrimeraVariable = 'Mi primera variable!'
console.log(miPrimeraVariable);
//const

miPrimeraVariable = 'Esto ha cambiado'
console.log(miPrimeraVariable);

//Boolean
let miBoolean = true
let miOtroBool = false

let miNumero = 0
let miNumero2 = 12
let miNumero3 = -258

console.log(miNumero, miNumero2, miBoolean);

// al no entregarle valor, queda indefinido 
let undef
console.log(undef);

// nulo si posee valor, pero es nulo
let nulo = null
console.log(nulo)

//Objeto vacio
const miPrimerObjeto = {}

//Objeto: los objetos tiene propiedades que hacen sentido entre si
const miObjeto = {
    unNumero: 12,
    unString: 'Esta cadena de caracteres',
    unaCondicion: true,
}

console.log(miObjeto);

//imprimir propiedad de un objeto
console.log(miObjeto.unNumero);

// Arreglo: pueden tener diferentes elementos dentro
const arrVacio = []
const arr = [1,2,'hola','mundo',miObjeto]

//console.log(arrVacio, arr);

//agregar elementos a un arreglo
arr.push(5)
console.log(arr)