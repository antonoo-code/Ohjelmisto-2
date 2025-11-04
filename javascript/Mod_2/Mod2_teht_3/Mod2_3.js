const num_of_dogs = 6;

let dogs_list = [];

for (i = 0; i < 6; i++) {
  let name = prompt("Syötä koiran nimi: ");
  dogs_list.push(name);
}
dogs_list.sort();

let sorted_dogs_list = dogs_list.reverse();

const ul = document.querySelector(".output");
sorted_dogs_list.forEach((dog) => {
  const li = document.createElement("li");
  li.textContent = dog;
  ul.appendChild(li);
});
