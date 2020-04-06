from FirebaseSdk import db

def updateData(collectionName, data, doc=None):
    doc_ref = db.collection(collectionName).document(doc)
    doc_ref.set(data)
    return doc_ref.id
