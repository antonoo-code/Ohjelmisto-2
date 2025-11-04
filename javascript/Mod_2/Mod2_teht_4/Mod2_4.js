alert("nyt toimii");

let imp_no = Number(prompt("Syötä numero: "));

num_ar = [];
while (imp_no != 0) {
  imp_no = Number(prompt("Syötä uusi numero:"));
  num_ar.push(imp_no);
}

num_ar.sort(function (a, b) {
  return b - a;
});

console.log(num_ar);
