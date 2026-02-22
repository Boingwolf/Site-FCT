// Função para buscar e mostrar os contactos
async function carregarContactos() {
  const contactoList = document.querySelector(".contacto-list");

  try {
    // Mostrar loading
    contactoList.innerHTML = '<p class="loading">A carregar contactos...</p>';

    // Buscar dados da API
    const response = await fetch("https://site-fct.onrender.com/api/contactos");

    if (!response.ok) {
      throw new Error("Erro ao carregar contactos");
    }

    const contactos = await response.json();

    // Limpar loading
    contactoList.innerHTML = "";

    // Se não houver contactos
    if (contactos.length === 0) {
      contactoList.innerHTML =
        '<p class="sem-dados">Ainda não há contactos registados.</p>';
      return;
    }

    // Criar cartões para cada contacto
    contactos.forEach((contacto) => {
      const cartao = criarCartaoContacto(contacto);
      contactoList.appendChild(cartao);
    });
  } catch (error) {
    console.error("Erro:", error);
    contactoList.innerHTML =
      '<p class="erro">Erro ao carregar contactos. Tente novamente.</p>';
  }
}

// Função para criar um cartão de contacto
function criarCartaoContacto(contacto) {
  const cartao = document.createElement("div");
  cartao.className = "cartao-contacto";

  // Formatar data
  const data = new Date(contacto.criado_em);
  const dataFormatada = data.toLocaleDateString("pt-PT", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });

  cartao.innerHTML = `
        <div class="cartao-header">
            <h3>${contacto.nome}</h3>
            <span class="cartao-data">${dataFormatada}</span>
        </div>
        <div class="cartao-body">
            <p class="cartao-email"><strong>Email:</strong> ${
              contacto.email
            }</p>
            ${
              contacto.assunto
                ? `<p class="cartao-assunto"><strong>Assunto:</strong> ${contacto.assunto}</p>`
                : ""
            }
            <p class="cartao-mensagem"><strong>Mensagem:</strong> ${
              contacto.mensagem
            }</p>
        </div>
        <div class="cartao-footer">
            <small>ID: ${contacto.id}</small>
        </div>
    `;

  return cartao;
}

// Função para enviar formulário (opcional - para usar com JavaScript em vez do form action)
async function enviarContacto(event) {
  event.preventDefault();

  const nome = document.getElementById("nome").value;
  const email = document.getElementById("email").value;
  const assunto = document.getElementById("assunto").value;
  const mensagem = document.getElementById("mensagem").value;

  try {
    const response = await fetch("https://site-fct.onrender.com/api/contacto", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nome,
        email,
        assunto,
        mensagem,
      }),
    });

    if (!response.ok) {
      throw new Error("Erro ao enviar contacto");
    }

    const resultado = await response.json();
    alert("Contacto enviado com sucesso!");

    // Limpar formulário
    event.target.reset();

    // Recarregar lista de contactos
    carregarContactos();
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro ao enviar contacto. Tente novamente.");
  }
}

// Carregar contactos quando a página carregar
document.addEventListener("DOMContentLoaded", () => {
  carregarContactos();
  const form = document.querySelector(".form-contacto form");
  form.addEventListener("submit", enviarContacto);
  setInterval(carregarContactos, 30000);
});
