function enviarFormulario() {
  const formulario = document.querySelector("form");
  const nome = formulario.elements["nome"].value;
  const email = formulario.elements["email"].value;
  const assunto = formulario.elements["assunto"].value;
  const mensagem = formulario.elements["mensagem"].value;
  const URL = "https://site-fct.onrender.com/api/contacto";
  fetch(URL, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nome: nome,
      email: email,
      assunto: assunto,
      mensagem: mensagem,
    }),
  })
    .then((resposta) => {
      if (resposta.ok) {
        return resposta.json();
      } else {
        console.log("Deu erro!");
      }
    })
    .then((json) => console.log(json))
    .catch((erro) => console.log(erro));
}
