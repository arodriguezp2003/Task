module.exports = function(grunt) {
	grunt.initConfig({
		bb_generate: {
			options: {
				appname       : "RS",
				appsrc        : "js/backbone",
				routersrc     : "js/backbone/routers/",
				modelsrc      : "js/backbone/models/",
				viewsrc       : "js/backbone/views/",
				collectionsrc : "js/backbone/collections/",
				templatesrc   : "js/backbone/templates/"
			},
			router:{},
			view:{},
			collection:{},
			model:{},
			template:{}
		},
		uglify : {
			options : {
				compress:true,
				report:true,
				banner:'/*!<%= grunt.template.date() %> */\n'
			},
			app : {
				files: {
					'app.min.js' : [
						'js/init.js',
						'js/backbone/models/article.js',
						'js/backbone/collections/articles.js',
						'js/backbone/routers/base.js',
						'js/backbone/views/article.js',
						'js/backbone/views/articleNew.js',
						'js/main.js'
					]
				}
			}
		}
	});

	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-bb-generate');

	grunt.registerTask('default',['uglify']);
};