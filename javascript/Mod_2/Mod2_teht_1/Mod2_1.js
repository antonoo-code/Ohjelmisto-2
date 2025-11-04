let num_ar = [];

const num1 = prompt("Syötä ensimmäinen numero: ");
num_ar.push(num1);

const num2 = prompt("Syötä toinen numero: ");
num_ar.push(num2);

const num3 = prompt("Syötä kolmas numero: ");
num_ar.push(num3);

const num4 = prompt("Syötä neljäs numero: ");
num_ar.push(num4);

const num5 = prompt("Syötä viides numero: ");
num_ar.push(num5);

for (let i = 5; i >= 0; i--) {
  console.log(num_ar[i]);
}
