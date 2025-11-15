"use strict";
const students = [
  {
    name: "John",
    id: "2345768",
  },
  {
    name: "Paul",
    id: "2134657",
  },
  {
    name: "Jones",
    id: "5423679",
  },
];

const t = document.getElementById("target");

for (let i = 0; i < students.length; i++) {
  const sn = students[i].name;
  const si = students[i].id;

  const op = document.createElement("option");
  op.value = si;
  op.text = sn;

  t.appendChild(op);
}
