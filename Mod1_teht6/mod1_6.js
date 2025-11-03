const user_query = confirm("Should I calculate the square root?");

const num = prompt("Syötä laskettava numero: ");

const result = Math.sqrt(num);

if (user_query == true && num > 0) {
  const main_result = `Result is ${result}`;
  document.querySelector(".output").textContent = main_result;
} else if (user_query == false) {
  const typo = "The square root is not calculated.";
  document.querySelector(".output").textContent = typo;
} else if (user_query == true && num < 0) {
  const neg_typo = "The square root of a negative number is not defined";
  document.querySelector(".output").textContent = neg_typo;
}
