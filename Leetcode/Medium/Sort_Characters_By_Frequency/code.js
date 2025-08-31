/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    const freqMap = {};

    for (let char of s) {
        freqMap[char] = (freqMap[char] || 0) + 1;
    }

    return Object.entries(freqMap)
        .sort((a, b) => b[1] - a[1])
        .map(([char, freq]) => char.repeat(freq))
        .join('');
};