"use strict";

const num1 = Number(prompt("Syötä ensimmäinen luku: "));
const num2 = Number(prompt("Syötä toinen luku: "));
const num3 = Number(prompt("Syötä kolmas luku: "));

const result = `Numeroiden summa on ${num1 + num2 + num3}, numeroiden tulo on ${
  num1 * num2 * num3
}, numeroiden keskiarvo on ${(num1 + num2 + num3) / 3}`;
document.querySelector(".output").textContent = result;
