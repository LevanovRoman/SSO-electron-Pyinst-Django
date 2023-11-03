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
  // Create the browser window.
  window = new BrowserWindow({
    width: 1600,
    height: 600,
    show: false,
    webPreferences: {
      nodeIntegration: true,
    },
  });

 const appURL = "http://127.0.0.1:8000/";
 window.loadURL(appURL);
};

app.on('ready', () => {
  createWindow();
  createTray();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

