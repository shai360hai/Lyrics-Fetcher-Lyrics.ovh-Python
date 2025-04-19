function getLyrics() {
  const artist = document.getElementById("artist").value.trim();
  const song = document.getElementById("song").value.trim();
  const output = document.getElementById("output");

  if (!artist || !song) {
    output.innerText = "Please enter both artist and song name.";
    return;
  }

  const url = `https://api.lyrics.ovh/v1/${encodeURIComponent(artist)}/${encodeURIComponent(song)}`;

  output.innerText = "Fetching lyrics...";

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Lyrics not found.");
      }
      return response.json();
    })
    .then((data) => {
      const lyrics = data.lyrics || "Lyrics not found.";
      const formatted = lyrics.replace(/\n/g, "<br>");
      output.innerHTML = formatted;
    })
    .catch((error) => {
      output.innerText = `Error: ${error.message}`;
    });
}
