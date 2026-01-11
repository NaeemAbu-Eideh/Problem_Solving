/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    const data = new Promise((data) => setTimeout(data, millis));
    return data;

}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */