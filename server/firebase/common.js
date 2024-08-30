// firebase-config.js
import { cert, initializeApp, getApp } from 'firebase-admin/app';
import {} from "firebase-admin/auth"
import fs from "fs"


const serviceAccount = JSON.parse(
    fs.readFileSync('./privateKey.json', 'utf8')
);

initializeApp({
    credential: cert(serviceAccount),
});

console.log(getApp().name);