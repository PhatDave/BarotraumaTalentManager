const {app, BrowserWindow} = require('electron');
const path = require("path");

const webPath = './web';
const templatesPath = path.join(webPath, 'templates');
const scriptPath = path.join(webPath, 'scripts');

function createWindow() {
	const win = new BrowserWindow({
		width: 1600,
		height: 800,
		webPreferences: {
			preload: path.join(__dirname, 'preload.js'),
			nodeIntegration: true
		}
	})
	win.loadFile(path.join(templatesPath, 'index.html'))
}

app.whenReady().then(() => {
	createWindow()
})

app.on('window-all-closed', () => {
	app.quit()
})