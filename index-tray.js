const { app, BrowserWindow, Tray, Menu} = require('electron');
const positioner = require('electron-traywindow-positioner');
const path = require('path');

let window = null;
let tray = null;

const showWindow = () => {
  positioner.position(window, tray.getBounds());
  window.show();
};

const toggleWindow = () => {
  if (window.isVisible()) return window.hide();
  return showWindow();
};

const createTray = () => {
  tray = new Tray('icon.ico');
  const contextMenu = Menu.buildFromTemplate([
    {label: 'Show App', click: function () {
                showWindow()}},
    {label: 'Quit', click: function () {
                app.isQuiting = true
                app.quit()}}
  ]);
  tray.setToolTip('SSO-auth');
  tray.setContextMenu(contextMenu);
  tray.on('click', () => {
    toggleWindow();
  });
};

const createWindow = () => {
  window = new BrowserWindow({
    width: 1600,
    height: 600,
    show: false,
	title: "SSO - auth",
    webPreferences: {
      nodeIntegration: true,
    },
  });
 window.removeMenu()
 const appURL = "http://127.0.0.1:8000/";
 window.loadURL(appURL);
 
 window.on('close', function (event) {
    if(!app.isQuiting){
        event.preventDefault();
        window.hide();
        event.returnValue = false;
    }
});
};

app.on('ready', () => {
  createWindow();
  createTray();
});

app.on('before-quit', function () {
  isQuiting = true;
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

