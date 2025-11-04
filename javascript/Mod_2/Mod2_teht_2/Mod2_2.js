const num_of_names = prompt("Syötä nimien määrä: ");

let names_list = [];

for (i = 0; i < num_of_names; i++) {
  let name = prompt("Syötä nimi: ");
  names_list.push(name);
}

let sorted_names_list = names_list.sort();

document.querySelector(".output").textContent = sorted_names_list;
