let emailLogin = document.getElementById("emailLogin")
let senhaLogin = document.getElementById("senhaLogin")

let emailCadastro = document.getElementById("emailCadastro")
let senhaCadastro = document.getElementById("senhaCadastro")
let confirmaSenha = document.getElementById("confirmaSenha")

let emailInterno = ['antonio@neto.com', 'lucas@franca.com', 'matheus@laxe.com', 'nayany@menegoi.com', 'raphael@monteiro.com']
let senhaInterno = ['123']


function validaLogin() {
    if (emailInterno.includes(emailLogin.value) && senhaInterno.includes(senhaLogin.value)) {
        alert("Login realizado com sucesso!")
        window.location.href = "home.html"
    } else {
        alert("E-mail e/ou senha incorretos.")
    }
}

function mostraSenhaLogin() {
    if (senhaLogin.type === "password") {
        senhaLogin.type = "text"
    } else {
        senhaLogin.type = "password"
    }

    if (confirmaSenha.type === "password") {
        confirmaSenha.type = "text"
    } else {
        confirmaSenha.type = "password"
    }
}

function efetuaCadastro() {
    alert('Cadastro realizado com sucesso!')
    window.location.href = "login.html"
}

function mostraSenhaCadastro() {
    if (senhaCadastro.type === "password") {
        senhaCadastro.type = "text"
    } else {
        senhaCadastro.type = "password"
    }

    if (confirmaSenha.type === "password") {
        confirmaSenha.type = "text"
    } else {
        confirmaSenha.type = "password"
    }
}