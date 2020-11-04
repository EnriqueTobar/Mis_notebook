function sumar(a ,b ,cb) {
    const r = a + b
    cb(r)
}

function callback(result) {
    console.log('resultado', result);
}
//callback(6)
sumar(2, 3, callback);