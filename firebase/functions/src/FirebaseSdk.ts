import * as admin from 'firebase-admin';
const serviceAccount = require("./serviceAccount.json");


admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://covid-19-l.firebaseio.com"
});
export const store = admin.firestore();
export const auth = admin.auth;
