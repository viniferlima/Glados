
<template>
	<div id="home">
    <div style="height:auto; width:100%;">
		<div style="text-align: center;">
			<h1>Bem-vindo à Gla<span style="color: rgb(90,136,202)">DOS</span></h1>
			<br>
			<h3>A melhor ferramenta para buscar os melhores preços</h3>
		</div>
		<br>
		<div style="text-align: center;">
			<div class="container" id="conteudo">
			{{ info }}
			</div>
		</div>
		
		
	</div>
	

</div>
</template>

<script>

import Vue from 'vue'
import axios from 'axios'
import $ from 'jquery'

		export default {
		  name: 'home',
		  data () {
			return {
			  msg: 'Welcome to Your Vue.js App'
			}
		  },
		  mounted (){
		  axios
			.get('http://localhost:8080')
			.then(response => {
			this.info = response.produto.bpi
			})
			.catch(error => {
			console.log(error)
			this.errored = true
			})
			.finally(() => this.loading = false)
			/*const a = require('../src/teste.json');
			for(let i = 0; i < a.produto.length; i++){
			console.log(a.produto[i].nome);
			}*/
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
	-webkit-box-shadow: 0px 17px 40px 2px rgba(255,153,0,1);
	-moz-box-shadow: 0px 17px 40px 2px rgba(255,153,0,1);
	box-shadow: 0px 17px 40px 2px rgba(255,153,0,1);
}
.produto-b{
	height:350px;
	width:300px;
	margin-left:50px;
	margin-bottom:50px;
	float:left;
	border-radius:40px;
	-webkit-box-shadow: 0px 17px 40px 2px rgba(39,166,216,1);
	-moz-box-shadow: 0px 17px 40px 2px rgba(39,166,216,1);
	box-shadow: 0px 17px 40px 2px rgba(39,166,216,1);
}
.titulo{
	margin-top:40px;
	height:auto;
	width:80%;
	border-radius:10px;
	-webkit-box-shadow: 0px 17px 40px 2px rgba(39,166,216,1);
	-moz-box-shadow: 0px 17px 40px 2px rgba(39,166,216,1);
	box-shadow: 0px 17px 40px 2px rgba(39,166,216,1);
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
</style>
