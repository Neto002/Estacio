let emailLogin = document.getElementById("emailLogin")
let senhaLogin = document.getElementById("senhaLogin")

let emailCadastro = document.getElementById("emailCadastro")
let senhaCadastro = document.getElementById("senhaCadastro")
let confirmaSenha = document.getElementById("confirmaSenha")

let emailInterno = ['antonio@neto.com']
let senhaInterno = ['123']


function validaLogin() {
    if (emailInterno.includes(emailLogin.value) && senhaInterno.includes(senhaLogin.value)) {
        alert("Login realizado com sucesso!")
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