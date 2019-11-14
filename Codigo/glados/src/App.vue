<template>
  <div id="app">
    <hello></hello>
	<home></home>
	<bye></bye>
  </div>
</template>

<script>
import hello from './components/Hello.vue'
import bye from './components/bye.vue'
import home from './components/home.vue'
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
		.get('http://localhost:5000')
		.then(response => {
			this.info = response.data.bpi
		})
		.catch(error => {
			console.log(error)
			this.errored = true
		})
		.finally(() => this.loading = false)
		/* const a = require('./.json');
		console.log('a');
		console.log(a.data);*/
	}
}
		

</script>
