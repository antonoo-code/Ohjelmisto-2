document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const input = document.getElementById("query");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const value = input.value;
    const url = `https://api.tvmaze.com/search/shows?q=${value}`;

    try {
      const response = await fetch(url);
      const data = await response.json();

      console.log("Result:", data);
    } catch (error) {
      console.error("Error:", error);
    }
  });
});
