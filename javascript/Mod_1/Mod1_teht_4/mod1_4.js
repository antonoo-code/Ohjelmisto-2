alert("nyt toimii");

const student = prompt("Syötä opiskelijan nimi: ");

const rand_no = Math.ceil(Math.random() * 4);

if (rand_no == 1) {
  const result = `${student} you are ravenclaw`;
  document.querySelector(".output").textContent = result;
} else if (rand_no == 2) {
  const result = `${student} you are slytherin`;
  document.querySelector(".output").textContent = result;
} else if (rand_no == 3) {
  const result = `${student} you are gryffindor`;
  document.querySelector(".output").textContent = result;
} else if (rand_no == 4) {
  const result = `${student} you are huffelpuff`;
  document.querySelector(".output").textContent = result;
}
