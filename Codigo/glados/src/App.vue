<template>
  <div id="app">
    <hello></hello>
	<home></home>
	<div class="container">
		<div class="produto-a" v-for="nomes in info" v-bind:key="nomes.id">
			<center><div class="img_product"><img src="./src/img/icone.png" class="img-generic"></div></center>
			<center><p class="titulo">{{nomes.nome}}</p></center>
			
			<div class="dropdown">
			  <span style="margin-left:50px; margin-top:15px;"><img src="./src/img/info.png" style="max-height:20px;">Ver detalhes</span>
			  <div class="dropdown-content">
			  <p>
			  Categoria: {{nomes.categoria}}<br>
			  Preço cheio: R$ {{nomes.preco_cheio}}<br>
			  Desconto: R$ {{nomes.preco_desconto}}<br>
			  Disponibilidade: {{nomes.disponibilidade}}<br>
			  Site: {{nomes.site}}
			  </p>
			 </div>
		</div>
		</div>
	</div>
	
	<bye></bye>
	
  </div>
</template>

<script>
import Vue from 'vue'
import hello from './components/Hello.vue'
import bye from './components/bye.vue'
import home from './components/home.vue'
import axios from 'axios'
import $ from 'jquery'

export default {
	name: 'app',
	components: {
		hello,
		bye,
		home
		 },
	data () {
	return {
		info: null
	}
	},
	mounted() {
	axios
		.get('./src/dados.json')
		.then(response => {
			this.info = response.data.produto
		})
		.catch(error => {
			console.log(error)
			this.errored = true
		})
		.finally(() => this.loading = false)
	}
}
</script>
<style>
.produto-a{
	height:350px;
	width:300px;
	margin-left:50px;
	margin-bottom:50px;
	float:left;
	border-radius:40px;
	-webkit-box-shadow: -12px 159px 249px 0px rgba(39,167,216,0.75);
	-moz-box-shadow: -12px 159px 249px 0px rgba(39,167,216,0.75);
	box-shadow: -12px 159px 249px 0px rgba(39,167,216,0.75);
}
.titulo{
	margin-top:40px;
	height:auto;
	width:80%;
	border-radius:10px;
	-webkit-box-shadow: -15px 98px 246px -68px rgba(39,167,216,1);
	-moz-box-shadow: -15px 98px 246px -68px rgba(39,167,216,1);
	box-shadow: -15px 98px 246px -68px rgba(39,167,216,1);
	margin-left:auto;
	margin-right:auto;
	font-size:18px;
}
.img_product{
	margin-top:40px;
}
.img-generic{
	height:auto;
	width:auto;
	max-height: 150px;
}
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  padding: 12px 16px;
  z-index: 1;
}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>
