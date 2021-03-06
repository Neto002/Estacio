<?php
if(!isset($_SESSION)) {
    session_start();
}
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Inicial</title>
    <link rel="stylesheet" href="../styles/style.css">
</head>
<body>
    <header class="cabecalho">
        <nav class="menuSuperior">
            <a class="menuItem" href="home.php">Página Inicial</a>
            <a class="menuItem" href="produtos.html">Produtos</a>
            <a class="menuItem" href="fale-conosco.html">Fale Conosco</a>
            <a class="menuItem" href="login.php">Entrar</a>
        </nav>
    </header>
    <main class="conteudo">
        <br>
        <h2>Bem vindo ao XPTO Componentes de Informática, <span style="color: yellow;"><?php echo $_SESSION['nome'];?></span>.</h2>
        <section class="conteudoPrincipal">
            <div class="conteudoPrincipalDiv">
                <h1 class="conteudoPrincipalTitulo">XPTO Componentes de Informática</h1>
                <p class="apresentacaoParagrafo">Nossa loja é especializada em vendas de componentes para computadores, com um estoque completo e de qualidade.</p>
            </div>
        </section>
        <section class="secaoForm">
            <div class="formularioDiv">
                <form class="formulario">
                    <h2>Fale Conosco</h2>
                    <div class="formularioDados">
                        <input type="text" required>
                        <label>Nome</label>
                    </div>
                    <div class="formularioDados">
                        <select>
                            <option disabled selected>Selecione o sexo</option>
                            <option>Masculino</option>
                            <option>Feminino</option>
                            <option>Prefiro não dizer</option>
                        </select>
                    </div>
                    <div class="formularioDados">
                        <input type="email" required>
                        <label>E-mail</label>
                    </div>
                    <div class="formularioDados">
                        <textarea cols="30" rows="3" required></textarea>
                        <label>Mensagem</label>
                    </div>
                    <a href="#" onclick="alert('Mensagem enviada com sucesso')">
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        Enviar
                    </a>
                </form>
            </div>
        </section>
    </main>
    <footer>
        <a href="home.html">
            <h1 class="tituloFooter">XPTO Componentes de Informática</h1>
        </a>
        <p class="tituloFooter" style="font-size: 20px;">Desenvolvido por: <br> Antonio Gomes Ferreira Neto <br> Lucas de França Carvalho <br> Matheus da Silveira Laxe Tavares <br> Nayany Menegoi Nobre <br> Raphael Leonardo Monteiro de Oliveira</p>
    </footer>
</body>
</html>