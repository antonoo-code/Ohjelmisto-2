document.addEventListener("DOMContentLoaded", () => {
  //lisää kuuntelijan joka huomaa kun documentti on ladattu ja suorittaa tän lamdafunktion.
  //tallennetaan tarvittavat elementit muuttujiin.
  const form = document.querySelector("form");
  const input = document.getElementById("query");
  const resultsDiv = document.getElementById("results");

  form.addEventListener("submit", async (event) => {
    // kun Search nappia on painettu.
    event.preventDefault(); // ei suoriteta oletustoimintoa eventille.

    const value = input.value;
    if (!value) return;

    const url = `https://api.tvmaze.com/search/shows?q=${value}`;

    try {
      const response = await fetch(url); // await pysäyttää ja odottaa promisea.
      const data = await response.json();

      resultsDiv.innerHTML = ""; // tyhjentää vanhan tuloksen

      data.forEach((item) => {
        // taas uus lambda funktio
        const tv = item.show; // viitataan json objektin show elementtiin/avaimeen.

        const article = document.createElement("article");

        const title = document.createElement("h2");
        title.textContent = tv.name;

        const link = document.createElement("a");
        link.href = tv.url;
        link.target = "_blank";
        link.textContent = "Details page";

        const img = document.createElement("img");
        img.src = tv.image?.medium || ""; //Ei aiheuta errorria jos ei kuvaa. https://www.w3schools.com/jsref/jsref_oper_optional.asp
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
