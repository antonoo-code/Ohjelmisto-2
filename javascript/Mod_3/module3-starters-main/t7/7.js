"use strict";

const kuva = document.getElementById("target");
const trig = document.getElementById("trigger");

const kuva_A = kuva.src;

trig.addEventListener("mouseover", () => {
  kuva.src = "img/picB.jpg";
});

trig.addEventListener("mouseout", () => {
  kuva.src = kuva_A;
});
