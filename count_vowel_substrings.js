// cuaieuouac 7

function countVowelSubstrings(str) {
  let count = 0;
  const vowels = new Set('aeiou');

  for (let i = 0; i < str.length; i++) {
    const subset = new Set();

    for (const next of str.slice(i)) {
      if (!vowels.has(next)) {
        break;
      }

      subset.add(next);

      if (subset.size === 5) {
        count += 1;
      }
    }
  }

  return count;
}

console.log(countVowelSubstrings('cuaieuouac')); // 7
console.log(countVowelSubstrings('aeiouu')); // 2
console.log(countVowelSubstrings('unicornarihan')); // 0
console.log(countVowelSubstrings('bbaeixoubb')); // 0
