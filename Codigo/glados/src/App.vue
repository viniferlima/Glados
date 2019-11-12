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
  }
}


</script>
