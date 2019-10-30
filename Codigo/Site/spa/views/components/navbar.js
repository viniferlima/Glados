let Navbar = {
    render: async () => {
        let view =  /*html*/`
             <div class="site-branding-area">
				<div class="container">
					<div class="row">
						<div class="col-sm-6">
							<div class="logo">
								<h1><a href="./"><img src="img/logo.png" style="margin-top: -40px"></a></h1>
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
								<li class="active"><a href="/#/">Menu1</a></li>
								<li><a href="#">Menu2</a></li>
								<li><a href="#">Menu3</a></li>
								<li><a href="#">Menu4</a></li>
								<li><a href="#">Menu5</a></li>
								<li>
									<div style="width:450px; margin-left:50%;">
										<input type="text" class="form-control" placeholder="O que deseja procurar?" style="width: 100%;">
									</div>
								</li>
							</ul>
						</div>  
					</div>
				</div>
			</div> <!-- End mainmenu area -->
        `
        return view
    },
    after_render: async () => { }

}

export default Navbar;