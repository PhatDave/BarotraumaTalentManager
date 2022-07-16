const {app, BrowserWindow} = require('electron');
const path = require("path");

function createWindow() {
	const win = new BrowserWindow({
		width: 1600,
		height: 800,
		webPreferences: {
			preload: path.join(__dirname, 'preload.js')
		}
	})
	win.loadFile('templates/index.html')
}

app.whenReady().then(() => {
	createWindow()
})

app.on('window-all-closed', () => {
	app.quit()
})