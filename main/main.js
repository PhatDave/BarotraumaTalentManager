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
				label: 'Pogramn\'t',
				accelerator: 'Ctrl+Q',
				click: function() {
					app.quit()
				}
			},
			{
				label: 'Pogram',
				// Looks like you cannot override some default hotkeys
				accelerator: 'Ctrl+A',
				click: createNewWindow
			}
		]
	}
]

if (process.env.NODE_ENV !== 'production') {
	mainMenuTemplate.push({
		label: 'Developer',
		submenu: [
			{
				label: 'Reload',
				accelerator: 'Ctrl+R',
				click: function(item, focusedWindow) {
					focusedWindow.reload();
				}
			},
			{
				label: 'Force Reload',
				accelerator: 'Ctrl+Shift+R',
				click: function(item, focusedWindow) {
					focusedWindow.webContents.reloadIgnoringCache();
				}
			},
			{
				label: 'Toggle',
				accelerator: 'Ctrl+Shift+I',
				click: function(item, focusedWindow) {
					focusedWindow.toggleDevTools();
				}
			}
		]
	});
}

function createNewWindow() {
	let newWindow = new BrowserWindow({
		width: 800,
		height: 400,
		webPreferences: {
			// preload: path.join(__dirname, 'preload.js'),
			nodeIntegration: true
		}
	})

	newWindow.loadFile(path.join(templatesPath, 'newPogram.html'));
	newWindow.on('close', function() {
		newWindow = null;
	});
}

app.whenReady().then(() => {
	mainWindow = new BrowserWindow({
		width: 1600,
		height: 800,
		webPreferences: {
			preload: path.join(__dirname, 'preload.js'),
			nodeIntegration: true
		}
	})

	mainWindow.on('closed', () => {
		app.quit();
	});
	Menu.setApplicationMenu(Menu.buildFromTemplate(mainMenuTemplate))
	mainWindow.loadFile(path.join(templatesPath, 'index.html'))
})

app.on('window-all-closed', () => {
	app.quit()
})
