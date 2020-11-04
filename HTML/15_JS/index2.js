
//Operadores Matematicos
const suma = 1 + 2
const restar = 1 - 2
const multiplicar = 1 * 2
const dividir = 1 / 2

console.log(suma, restar, multiplicar, dividir);

const modulo = 10 % 3

// let vs const - con let pueden cambiar
let num = 5
// ++ suma 1 a la variable
num++
num++
console.log(num);

// sumara 5 a nuestra variable
num += 5
console.log(num);

// Operadores comparación
const resultados1 = 5 === 6
const resultados2 = 5 == 6
const resultados3 = 5 == '5' // podemos compararlos incluso si son string
const resultados4 = 5 === '5' // igual estricta
console.log(resultados1, resultados2, resultados3, resultados4);

const resultados5 = 5 < 6
const resultados6 = 5 >= 6
console.log(resultados5, resultados6);

const resultados7 = 5 !== '5'
const resultados8 = 5 != 5
console.log(resultados7, resultados8);

// or ||, and &&, not !

const resultadoOr = false || false || false
console.log(resultadoOr);

// Control de Flujo IF
const edad = 5
if (edad > 5 && edad < 18) {
    console.log('El niño puede jugar')
} else {
    console.log('El niño no puede jugar')
}

// Control de Flujo While
let x = 0
while (x < 5) {
    console.log(x);
    x++
}

console.log('terminando loop');
console.log('cambios desde linux');