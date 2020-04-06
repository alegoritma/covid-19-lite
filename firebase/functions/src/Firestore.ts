import {store} from './FirebaseSdk';

export async function getMainTable(){
  try {

  const data = (await store.collection("main").doc("total").get()).data()
    if (data){
      return data
    } else {
      throw new Error("Internal server error!");
    }
  } catch (e) {
    console.error(e);
    throw e
  }
}
