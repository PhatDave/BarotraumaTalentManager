document.addEventListener("DOMContentLoaded", function(event) {
	const electron = require('electron');
	const ipcRenderer = electron.ipcRenderer;

	ipcRenderer.on('version', (event, version) => {
		console.log(version);
		document.querySelector('#node-version').innerText = version.node;
		document.querySelector('#chrome-version').innerText = version.chrome;
		document.querySelector('#electron-version').innerText = version.electron;
		document.querySelector('#pogs').innerText = version.pogs;
	});
});
