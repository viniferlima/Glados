--cria tabela
create database glados

--cria tabela produtos
CREATE TABLE `produtos` (
  `id` int(11) NOT NULL,
  `nome` varchar(1000) DEFAULT NULL,
  `categoria` varchar(1000) DEFAULT NULL,
  `preco_cheio` double DEFAULT NULL,
  `preco_desconto` double DEFAULT NULL,
  `porcentagem_desconto` float DEFAULT NULL,
  `data_consulta` timestamp DEFAULT CURRENT_TIMESTAMP,
  `site` varchar(1000) DEFAULT NULL,
  `disponibilidade` varchar(1000) DEFAULT NULL
)ENGINE=INNODB DEFAULT CHARSET=latin1;


--altera tabela adicionando chave primaria
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`id`);


--define 'id' para se auto-completar
ALTER TABLE `produtos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;