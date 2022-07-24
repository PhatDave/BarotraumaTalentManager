const {app, BrowserWindow, Menu} = require('electron');
const path = require("path");

const webPath = './web';
const templatesPath = path.join(webPath, 'templates');

let mainWindow;
const mainMenuTemplate = [
	{
		label: 'File',
		submenu: [
			{
				label: 'Test pogram',
				accelerator: 'Ctrl+Q',
				click: function() {
					app.quit()
				}
			}
		]
	}
]


app.whenReady().then(() => {
	mainWindow = new BrowserWindow({
		width: 1600,
		height: 800,
		webPreferences: {
			preload: path.join(__dirname, 'preload.js'),
			nodeIntegration: true
		}
	})

	Menu.setApplicationMenu(Menu.buildFromTemplate(mainMenuTemplate))
	mainWindow.loadFile(path.join(templatesPath, 'index.html'))
})

app.on('window-all-closed', () => {
	app.quit()
})
