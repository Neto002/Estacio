let dados = new FormData()
dados.append('nome', 'Antonio')
dados.append('idade', 19)
dados.append('matricula', '202102570735')

$.ajax({
    url: 'http://localhost:8080/aula10/script.php',
    method: 'POST',
    data: dados,
    processData: false,
    contentType: false,
    // success: function(resposta) {
    //     alert(resposta)
    // }
}).done(function(resposta) {
    $('#main').text(resposta)
    //window.alert(resposta)
})