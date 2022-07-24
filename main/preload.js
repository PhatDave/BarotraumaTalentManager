const path = require("path");
window.addEventListener('DOMContentLoaded', function() {
	const head = document.querySelector('head');

	const bootstrapCss = document.createElement('link');
	bootstrapCss.rel = 'stylesheet';
	bootstrapCss.href = path.join(process.cwd(), 'node_modules/bootstrap/dist/css/bootstrap.css');
	const bootstrapJs = document.createElement('script');
	bootstrapJs.src = path.join(process.cwd(), 'node_modules/bootstrap/dist/js/bootstrap.js');
	const jqueryJs = document.createElement('script');
	jqueryJs.src = path.join(process.cwd(), 'node_modules/jquery/dist/jquery.js');

	head.appendChild(bootstrapCss);
	head.appendChild(bootstrapJs);
})
