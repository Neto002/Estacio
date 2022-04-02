let imagem = document.getElementById("imagem")
let paragrafoImg = document.getElementById("paragrafoImg")

function trocaImagem() {
    if (imagem.src.match("bulbon")) {
        imagem.src = "https://www-w3schools-com.translate.goog/js/pic_bulboff.gif"
        paragrafoImg.innerText = "Clique para acender a lâmpada."
    } else {
        imagem.src = "https://www-w3schools-com.translate.goog/js/pic_bulbon.gif"
        paragrafoImg.innerText = "Clique para apagar a lâmpada."
    }
}

let botao = document.getElementById("botao")
let paragrafo = document.getElementById("demo")

botao.onclick = () => {
    if (paragrafo.style.color == "blue") {
        paragrafo.style.color = "black"
        paragrafo.style.fontSize = "16px"
    } else {
        paragrafo.style.color = "blue"
        paragrafo.style.fontSize = "30px"
    }
}