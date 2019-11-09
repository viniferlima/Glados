<?php
$host = "localhost"; 
$user = "root"; 
$pass = ""; 
$database = "glados"; 
$conexao = mysql_connect($host,$user,$pass) or die ("Não foi possível conectar com o banco de dados");
     mysql_select_db($database,$conexao) or die ("Não foi possível selecionar o banco");
?>