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
			<div class="container">
				<div class="produto-a"></div>
				<div class="produto-b"></div>
				<div class="produto-a"></div>
			</div>
		</div>
	</div>
	
    <div class="promo-area">
        <div class="container">
            <div class="row">
                <div class="col-md-3 col-sm-6">
                    <div class="single-promo promo1">
                        <i class="fa fa-refresh"></i>
                        <p>Texto1</p>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="single-promo promo2">
                        <i class="fa fa-truck"></i>
                        <p>Texto2</p>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="single-promo promo3">
                        <i class="fa fa-lock"></i>
                        <p>Texto3</p>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="single-promo promo4">
                        <i class="fa fa-gift"></i>
                        <p>Texto4</p>
                    </div>
                </div>
            </div>
        </div>
    </div> <!-- End promo area -->
    


	</div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
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
</style>
