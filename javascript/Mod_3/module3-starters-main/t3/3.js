"use strict";
const names = ["John", "Paul", "Jones"];

let name_list = "";

for (let i = 0; i < names.length; i++) {
  name_list += `<li>${names[i]}</li>`;
}

document.getElementById("target").innerHTML = name_list;
