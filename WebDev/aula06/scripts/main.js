let emailInformado = document.getElementById('email')
let senhaInformado = document.getElementById('senha')

let email = 'antonio@neto.com'
let senha = '123'

function validaLogin() {
    if (emailInformado.value == email && senhaInformado.value == senha) {
        alert('Login efetuado com sucesso!')
    } else {
        alert('E-mail e/ou senha incorretos.')
    }
}