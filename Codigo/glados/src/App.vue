<template>
  <div id="app">
    <hello></hello>
	<home></home>
	<div class="container">
		<div class="produto-a" v-for="nomes in info" v-bind:key="nomes.id">
			<center><div class="img_product"><img src="./src/img/icone.png" class="img-generic"></div></center>
			<center><p class="titulo">{{nomes.nome}}</p></center>
			<center><button>{{nomes.id}}</button></center>
		</div>
	</div>
	<bye></bye>
  </div>
</template>

<script>
import hello from './components/Hello.vue'
import bye from './components/bye.vue'
import home from './components/home.vue'
import axios from 'axios'
import $ from 'jquery'

import carousel from 'vue-owl-carousel'

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
		.get('./src/teste.json')
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
	-webkit-box-shadow: 0px 17px 40px 2px rgba(255,153,0,1);
	-moz-box-shadow: 0px 17px 40px 2px rgba(255,153,0,1);
	box-shadow: 0px 17px 40px 2px rgba(255,153,0,1);
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
