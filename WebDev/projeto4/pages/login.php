<?php
include('../scripts/conexao.php');

$resultado_login = '';

if (isset($_POST['email']) || isset($_POST['senha'])) {
    if (strlen(($_POST['email'])) == 0) {
        echo "Por favor, preencha seu e-mail";
    } else if (strlen(($_POST['senha'])) == 0) {
        echo "Por favor, preencha sua senha";
    } else {
        $email = $mysqli->real_escape_string($_POST['email']);
        $senha = $mysqli->real_escape_string($_POST['senha']);

        $sql_code = "SELECT * FROM usuario WHERE email = '$email' AND senha = '$senha'";
        $sql_query = $mysqli->query($sql_code) or die("Falha na execução do código SQL: " . $mysqli->error);

        $quantidade = $sql_query->num_rows;

        if ($quantidade == 1) {
            $usuario = $sql_query->fetch_assoc();
            if(!isset($_SESSION)) {
                session_start();
            }
            $_SESSION['id'] = $usuario['id'];
            $_SESSION['nome'] = $usuario['nome'];

            header("Location: home.php");
        } else {
            $resultado_login = "Falha ao logar! E-mail e/ou senha inválidos";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
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
        <section class="conteudoPrincipal">
            <div class="conteudoPrincipalDiv">
                <h1 class="conteudoPrincipalTitulo">Login</h1>
            </div>
        </section>
        <section class="secaoForm">
            <div class="formularioDiv">
                <form class="formulario" id="form" action="" method="POST">
                    <div class="formularioDados">
                        <input id="emailLogin" name="email" type="email" required>
                        <label>E-mail</label>
                    </div>
                    <div class="formularioDados">
                        <input type="password" name="senha" id="senhaLogin" required>
                        <label>Senha</label>
                        <input type="checkbox" id="check" onclick="mostraSenhaLogin()">Mostrar Senha
                    </div>
                    <br>
                    <div>
                        <?php echo $resultado_login;?>
                    </div>
                    <a href="#" onclick="submitFormulario()" type="submit">
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        ENTRAR
                    </a>
                </form>
            </div>
        </section>
    </main>
    <footer>
        <a href="home.html">
            <h1 class="tituloFooter">XPTO Componentes de Informática</h1>
        </a>
        <p class="tituloFooter" style="font-size: 20px;">Desenvolvido por: <br>Antonio Gomes Ferreira Neto <br> Lucas de França Carvalho <br> Matheus da Silveira Laxe Tavares <br> Nayany Menegoi Nobre <br> Raphael Leonardo Monteiro de Oliveira</p>
    </footer>
    <script src="../scripts/main.js"></script>
</body>
</html>