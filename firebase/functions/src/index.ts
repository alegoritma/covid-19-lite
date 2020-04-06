import * as functions from 'firebase-functions';
import {getMainTable} from './Firestore';
const express = require("express");
const cors = require("cors")({origin: true});

const app = express();
app.use(cors);

app.get("/", async (req:any, res:any) => {
  const data = await getMainTable()
  res.json(data)
})


export const totalSummary = functions.https.onRequest(app);
