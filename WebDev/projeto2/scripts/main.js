function mostraSenha() {
    let senha = document.getElementById("senha")
    let confirmaSenha = document.getElementById("confirmaSenha")
    if (senha.type === "password" || confirmaSenha.type === "password") {
        senha.type = "text"
        confirmaSenha.type = "text"
    } else {
        senha.type = "password"
        confirmaSenha.type = "password"
    }
}