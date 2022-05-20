$.ajax({
    url: 'http://localhost:8080/WebDev/aula10/script.php',
    method: 'POST',

    
})

function definicaoObjeto() {
    this.atributo1 = "testando"
}

function testaJSON() {
    let obj = new definicaoObjeto()
    alert(obj.atributo1)
}