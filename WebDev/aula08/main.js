botao = document.getElementById('botao')

botao.onclick = () => {
    let resposta = document.getElementById('resposta').value
    let mes = document.getElementById('mes')
    switch (resposta) {
        case '1':
            mes.innerHTML = 'Janeiro'
            break
        case '2':
            mes.innerHTML = 'Fevereiro'
            break
        case '3':
            mes.innerHTML = 'Março'
            break
        case '4':
            mes.innerHTML = 'Abril'
            break
        case '5':
            mes.innerHTML = 'Maio'
            break
        case '6':
            mes.innerHTML = 'Junho'
            break
        case '7':
            mes.innerHTML = 'Julho'
            break
        case '8':
            mes.innerHTML = 'Agosto'
            break
        case '9':
            mes.innerHTML = 'Setembro'
            break
        case '10':
            mes.innerHTML = 'Outubro'
            break
        case '11':
            mes.innerHTML = 'Novembro'
            break
        case '12':
            mes.innerHTML = 'Dezembro'
            break
        default:
            mes.innerHTML = 'Mês inválido'
            break
    }
}