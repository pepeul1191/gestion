/*! layouts/site.js 
	variables : BASE_URL, STATICS_URL, MODULOS_JSON, DATA
*/

$( document ).ready(function() {
	var home_template = $("#template").html();
	var template = Handlebars.compile(home_template);

	Handlebars.registerPartial("header", $("#header-template").html());
	Handlebars.registerPartial("breadcrumb", $("#breadcrumb-template").html());
	Handlebars.registerPartial("contenido", $("#contenido-template").html());
	Handlebars.registerPartial("footer", $("#footer-template").html());

	var data = {
		'BASE_URL' : BASE_URL, 
		'STATICS_URL' : STATICS_URL,
		'DATA' : DATA
	};
	var template_compiled = template(data);

	$("#app").html(template_compiled);

	$(".dropdown").click(function(e) {
		var url = $(e.currentTarget).children().eq(0).attr("href");
		window.location.href = url;
	});
});

Handlebars.registerHelper( "menuModulos", function (){
	var rpta = '';
	/**
			if(menuJsonObject.get("nombre").getAsString().equalsIgnoreCase(nombreModulo)){
				rpta = rpta + "<li class='dropdown active'><a href='" + Urls.getBaseURL() + menuJsonObject.get("url").getAsString() + 
						"' class='dropdown-toggle' data-toggle='dropdown'>" + menuJsonObject.get("nombre").getAsString() + "</a></li>";
			}else{
				rpta = rpta + "<li class='dropdown'><a href='" + Urls.getBaseURL() + menuJsonObject.get("url").getAsString() + 
						"' class='dropdown-toggle' data-toggle='dropdown'>" + menuJsonObject.get("nombre").getAsString() + "</a></li>";
			}
	 
	 */
	MODULOS_JSON.forEach(function(modulo) {
		//rpta = rpta + '<li><a href="' + BASE_URL + modulo['url'] + '">' + modulo['nombre'] + '</a></li>';
		rpta = rpta + "<li class='dropdown'><a href='" + BASE_URL + modulo['url'] + "' class='dropdown-toggle' data-toggle='dropdown'>" + modulo['nombre'] + "</a></li>"; 
	});
	return rpta;    
});

Handlebars.registerHelper( "menuSubmodulos", function (){
	var rpta = '';
	//console.log(SUBMODULOS_JSON);
	ITEMS_JSON.forEach(function(submodulo) {
		//console.log(submodulo);
	    rpta = rpta + "<li class='list-group-item list-group-item-titulo'>" + submodulo.subtitulo + "</li>";
	    //<a href="#" class="list-group-item">Cras justo odio</a>
	    submodulo.items.forEach(function(item){
	    		rpta = rpta + "<li class='list-group-item list-group-elemento'><a href='"+ BASE_URL + item.url  + "'>" + item.item + "</a></li>";
	    });
	});
	return rpta;    
});

Handlebars.registerHelper('getValue', function(obj, key) {
    return obj[key];
});