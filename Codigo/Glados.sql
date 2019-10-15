
--cria tabela
create database glados

--cria tabela produtos
CREATE TABLE `produtos` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `preco` double DEFAULT NULL,
  `preco_desconto` double DEFAULT NULL,
  `porcentagem_desconto` float DEFAULT NULL,
  `data_consulta` datetime DEFAULT NULL,
  `site` varchar(50) DEFAULT NULL,
  `disponivel` varchar(50) DEFAULT NULL,
  `imagem` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--altera tabela adicionando chave primaria
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`id`);


--define 'id' para se auto-completar
ALTER TABLE `produtos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;