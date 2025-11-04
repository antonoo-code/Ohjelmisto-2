alert("nyt toimii");

let num_ar1 = [];

let imp_no = Number(prompt("Syötä numero: "));

while (imp_no != 0) {
  if (num_ar1.includes(imp_no)) {
    console.log("Numero on jo syötetty");
    break;
  } else {
    num_ar1.push(imp_no);
  }
  imp_no = Number(prompt("Syötä uusi numero:"));
}
num_ar1.sort(function (a, b) {
  return a - b;
});

console.log(num_ar1);
