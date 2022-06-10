function submitFormulario() {
    document.getElementById('form').submit()
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