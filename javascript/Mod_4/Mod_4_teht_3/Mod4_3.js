document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const input = document.getElementById("query");
  const resultsDiv = document.getElementById("results");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const value = input.value;
    if (!value) return;

    const url = `https://api.tvmaze.com/search/shows?q=${value}`;

    try {
      const response = await fetch(url);
      const data = await response.json();

      resultsDiv.innerHTML = "";

      data.forEach((item) => {
        const tv = item.show;

        const article = document.createElement("article");

        const title = document.createElement("h2");
        title.textContent = tv.name;

        const link = document.createElement("a");
        link.href = tv.url;
        link.target = "_blank";
        link.textContent = "Details page";

        const img = document.createElement("img");
        img.src = tv.image?.medium || "";
        img.alt = tv.name;

        const summary = document.createElement("div");
        summary.innerHTML = tv.summary || "No summary available";

        article.appendChild(title);
        article.appendChild(link);
        article.appendChild(img);
        article.appendChild(summary);

        resultsDiv.appendChild(article);
      });
    } catch (error) {
      console.error("Error:", error);
    }
  });
});
