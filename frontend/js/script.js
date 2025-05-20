async function loadNews() {
  try {
    const response = await fetch('./data/noticias.json');
    const data = await response.json();

    const container = document.getElementById('noticias');

    data.forEach((news) => {
      const titulo = document.createElement('h2');
      titulo.classList.add('news');
      titulo.textContent = news.title;

      container.appendChild(titulo);
    });
  } catch (err) {
    document.getElementById('noticias').textContent =
      'Erro ao carregar notícias.';
    console.error(err);
  }
}

loadNews();
