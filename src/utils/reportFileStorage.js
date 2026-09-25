const DB_NAME = 'FireNotifyDB'
const STORE_NAME = 'reportFiles'
const EVIDENCE_STORE_NAME = 'taskActivityEvidence'
const DB_VERSION = 2

const ensureStore = db => {
  if (!db.objectStoreNames.contains(STORE_NAME)) {
    db.createObjectStore(STORE_NAME, { keyPath: 'id' })
  }

  if (!db.objectStoreNames.contains(EVIDENCE_STORE_NAME)) {
    db.createObjectStore(EVIDENCE_STORE_NAME, { keyPath: 'id' })
  }
}

const openDatabase = () => {
  return new Promise((resolve, reject) => {
    if (!('indexedDB' in window)) {
      reject(new Error('IndexedDB is not available in this browser.'))
      return
    }

    const request = window.indexedDB.open(DB_NAME, DB_VERSION)

    request.onupgradeneeded = event => {
      const db = event.target.result
      ensureStore(db)
    }

    request.onsuccess = () => resolve(request.result)
    request.onerror = () => reject(request.error || new Error('Unable to open FireNotifyDB.'))
  })
}

const withStore = async callback => {
  const db = await openDatabase()

  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readwrite')
    const store = tx.objectStore(STORE_NAME)

    tx.oncomplete = () => resolve()
    tx.onerror = () => reject(tx.error || new Error('IndexedDB transaction failed.'))
    tx.onabort = () => reject(tx.error || new Error('IndexedDB transaction aborted.'))

    callback(store)
  })
}

export const saveReportFile = async fileRecord => {
  try {
    const record = {
      id: fileRecord.reportId || fileRecord.id,
      reportId: fileRecord.reportId || fileRecord.id,
      file: fileRecord.file,
      filename: fileRecord.filename || 'report-file',
      mimeType: fileRecord.mimeType || 'application/octet-stream',
      size: Number(fileRecord.size || 0),
      createdAt: fileRecord.createdAt || new Date().toISOString()
    }

    const db = await openDatabase()

    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readwrite')
      const store = tx.objectStore(STORE_NAME)
      const request = store.put(record)

      request.onsuccess = () => resolve(record)
      request.onerror = () => reject(request.error || new Error('Unable to save report file.'))
    })
  } catch (error) {
    console.error('FireNotify: saveReportFile failed', error)
    return null
  }
}

export const getReportFile = async reportId => {
  if (!reportId) return null

  const requestedId = String(reportId)

  try {
    const db = await openDatabase()

    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readonly')
      const store = tx.objectStore(STORE_NAME)
      const request = store.get(requestedId)

      request.onsuccess = () => {
        if (request.result) {
          resolve(request.result)
          return
        }

        const listRequest = store.getAll()
        listRequest.onsuccess = () => {
          const match = (listRequest.result || []).find(record => {
            return String(record?.reportId || record?.id || '') === requestedId
          })

          resolve(match || null)
        }

        listRequest.onerror = () => resolve(null)
      }

      request.onerror = () => reject(request.error || new Error('Unable to fetch report file.'))
    })
  } catch (error) {
    console.error('FireNotify: getReportFile failed', error)
    return null
  }
}

export const deleteReportFile = async reportId => {
  if (!reportId) return false

  const requestedId = String(reportId)

  try {
    const db = await openDatabase()

    const matches = await new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readonly')
      const store = tx.objectStore(STORE_NAME)
      const request = store.getAll()

      request.onsuccess = () => {
        const allRecords = request.result || []

        const matchingRecords = allRecords.filter(record => {
          const recordId = String(record?.id || '')
          const reportIdValue = String(record?.reportId || '')
          return recordId === requestedId || reportIdValue === requestedId
        })

        resolve(matchingRecords)
      }

      request.onerror = () => reject(request.error || new Error('Unable to find report file for deletion.'))
      tx.onerror = () => reject(tx.error || new Error('IndexedDB read transaction failed while locating report file.'))
      tx.onabort = () => reject(tx.error || new Error('IndexedDB read transaction aborted while locating report file.'))
    })

    const idsToDelete = Array.from(
      new Set(
        matches
          .map(record => String(record?.id || '').trim())
          .filter(Boolean)
      )
    )

    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readwrite')
      const store = tx.objectStore(STORE_NAME)

      if (!idsToDelete.length) {
        tx.oncomplete = () => resolve(true)
        tx.onerror = () => reject(tx.error || new Error('IndexedDB delete transaction failed.'))
        tx.onabort = () => reject(tx.error || new Error('IndexedDB delete transaction aborted.'))
        return
      }

      idsToDelete.forEach(id => {
        store.delete(id)
      })

      tx.oncomplete = () => resolve(true)
      tx.onerror = () => reject(tx.error || new Error('IndexedDB delete transaction failed.'))
      tx.onabort = () => reject(tx.error || new Error('IndexedDB delete transaction aborted.'))
    })
  } catch (error) {
    console.error('FireNotify: deleteReportFile failed', error)
    return false
  }
}

export const getAllReportFiles = async () => {
  try {
    const db = await openDatabase()

    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readonly')
      const store = tx.objectStore(STORE_NAME)
      const request = store.getAll()

      request.onsuccess = () => resolve(request.result || [])
      request.onerror = () => reject(request.error || new Error('Unable to list report files.'))
    })
  } catch (error) {
    console.error('FireNotify: getAllReportFiles failed', error)
    return []
  }
}

export const saveTaskActivityEvidence = async ({ recordId, recordType, files = [] }) => {
  if (!recordId || !recordType || !files.length) return []

  try {
    const db = await openDatabase()
    const prefix = `${recordType}:${recordId}:`
    const evidence = files.map((file, index) => ({
      id: `${prefix}${Date.now()}-${index}`,
      recordId: String(recordId),
      recordType,
      file,
      filename: file.name || `evidence-${index + 1}`,
      mimeType: file.type || 'application/octet-stream',
      size: Number(file.size || 0),
      createdAt: new Date().toISOString()
    }))

    return await new Promise((resolve, reject) => {
      const tx = db.transaction(EVIDENCE_STORE_NAME, 'readwrite')
      const store = tx.objectStore(EVIDENCE_STORE_NAME)
      evidence.forEach(item => store.put(item))
      tx.oncomplete = () => resolve(evidence.map(({ file, ...metadata }) => metadata))
      tx.onerror = () => reject(tx.error || new Error('Unable to save task/activity evidence.'))
      tx.onabort = () => reject(tx.error || new Error('Evidence transaction aborted.'))
    })
  } catch (error) {
    console.error('FireNotify: saveTaskActivityEvidence failed', error)
    return []
  }
}

export const getTaskActivityEvidence = async ({ recordId, recordType }) => {
  if (!recordId || !recordType) return []

  try {
    const db = await openDatabase()

    return await new Promise((resolve, reject) => {
      const tx = db.transaction(EVIDENCE_STORE_NAME, 'readonly')
      const request = tx.objectStore(EVIDENCE_STORE_NAME).getAll()
      request.onsuccess = () => resolve((request.result || []).filter(item =>
        String(item.recordId) === String(recordId) && item.recordType === recordType
      ))
      request.onerror = () => reject(request.error || new Error('Unable to load evidence.'))
    })
  } catch (error) {
    console.error('FireNotify: getTaskActivityEvidence failed', error)
    return []
  }
}

export const deleteTaskActivityEvidence = async ({ recordId, recordType }) => {
  if (!recordId || !recordType) return false

  try {
    const db = await openDatabase()
    const records = await getTaskActivityEvidence({ recordId, recordType })

    return await new Promise((resolve, reject) => {
      const tx = db.transaction(EVIDENCE_STORE_NAME, 'readwrite')
      const store = tx.objectStore(EVIDENCE_STORE_NAME)
      records.forEach(record => store.delete(record.id))
      tx.oncomplete = () => resolve(true)
      tx.onerror = () => reject(tx.error || new Error('Unable to delete evidence.'))
      tx.onabort = () => reject(tx.error || new Error('Evidence delete transaction aborted.'))
    })
  } catch (error) {
    console.error('FireNotify: deleteTaskActivityEvidence failed', error)
    return false
  }
}
