function mostraSenha() {
    let senha = document.getElementById("senha")
    let confirmaSenha = document.getElementById("confirmaSenha")
    if (senha.type === "password") {
        senha.type = "text"
    } else {
        senha.type = "password"
    }

    if (confirmaSenha.type === "password") {
        confirmaSenha.type = "text"
    } else {
        confirmaSenha.type = "password"
    }
}