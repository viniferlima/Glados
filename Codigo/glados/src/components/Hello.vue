<template>
  <div id="hello">
    <title>GlaDOS</title>
    
    <!-- Google Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Titillium+Web:400,200,300,700,600' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Roboto+Condensed:400,700,300' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Raleway:400,100' rel='stylesheet' type='text/css'>
    
    <!-- Bootstrap -->
    <link rel="stylesheet" href="src/css/bootstrap.min.css">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="src/css/font-awesome.min.css">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="src/css/owl.carousel.css">
    <link rel="stylesheet" href="src/style.css">
    <link rel="stylesheet" href="src/css/responsive.css">
	
	<div class="site-branding-area">
				<div class="container">
					<div class="row">
						<div class="col-sm-6">
							<div class="logo" style="margin-top: -100px;">
								<h1><a href="./"><img src="src/img/logo.png"></a></h1>
							</div>
						</div>
					</div>
				</div>
			</div>
			
			<div class="mainmenu-area">
				<div class="container">
					<div class="row">
						<div class="navbar-header">
							<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
								<span class="sr-only">Toggle navigation</span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
							</button>
						</div> 
						<div class="navbar-collapse collapse">
							<ul class="nav navbar-nav">
								<li class="active"><a href="/#/">Home</a></li>
								<li><a href="#">Produtos</a></li>
								<li>
									<div style="width:450px; margin-left:50%;">
										<input type="text" class="form-control" placeholder="O que deseja procurar?" style="width: 100%;">
									</div>
								</li>
								
							</ul>
							<ul>
								<li>
									<a href="#" class="myButton">Pesquisar</a>
								</li>
							</ul>
						</div>  
					</div>
				</div>
			</div> <!-- End mainmenu area -->
	</div>
	
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>
#hello {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
.myButton{
top: 31.3%;
float: right;
position: absolute;
box-shadow:inset 0px 1px 0px 0px #dcecfb;
background:linear-gradient(to bottom, #bddbfa 5%, #80b5ea 100%);
background-color:#bddbfa;
border-radius:6px;
border:1px solid #84bbf3;
display:inline-block;
cursor:pointer;
color:#ffffff;
font-family: Helvetica;
font-size:14px;
font-weight:bold;
padding:6px 24px;
text-decoration:none;
text-shadow:0px 1px 0px #528ecc;
}
.myButton:hover {
	background:linear-gradient(to bottom, #80b5ea 5%, #bddbfa 100%);
	background-color:#80b5ea;
}


</style>
