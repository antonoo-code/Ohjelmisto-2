"use strict";

const rivi1 = document.createElement("li");
rivi1.textContent = "First item";
document.getElementById("target").appendChild(rivi1);
const rivi2 = document.createElement("li");
rivi2.textContent = "Second item";
document.getElementById("target").appendChild(rivi2);
const rivi3 = document.createElement("li");
rivi3.textContent = "Third item";
document.getElementById("target").appendChild(rivi3);

document.getElementById("target").className = "my-list";
