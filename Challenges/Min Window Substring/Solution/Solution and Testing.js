
function MinWindowSubstring(strArr) {
  const [N, K] = strArr;
  const charCount = {}; // Keep track of characters in K and their counts
  let left = 0; // Left pointer for sliding window
  let count = 0; // Count of characters in K found in the current window
  let minLength = Infinity; // Length of smallest substring found
  let result = ""; // Smallest substring found

  // Count the characters in K
  for (let i = 0; i < K.length; i++) {
    const char = K[i];
    charCount[char] = (charCount[char] || 0) + 1;
  }

  // Iterate over N to find the smallest substring
  for (let right = 0; right < N.length; right++) {
    const char = N[right];

    if (charCount[char] !== undefined) {
      charCount[char]--;

      if (charCount[char] >= 0) {
        // Count the character if it's needed
        count++;
      }

      // Shrink the window from the left if all characters in K are found
      while (count === K.length) {
        const windowLength = right - left + 1;

        if (windowLength < minLength) {
          minLength = windowLength;
          result = N.slice(left, right + 1);
        }

        const leftChar = N[left];
        if (charCount[leftChar] !== undefined) {
          charCount[leftChar]++;

          if (charCount[leftChar] > 0) {
            // Update the count if the character is needed
            count--;
          }
        }

        left++;
      }
    }
  }

  return result;
}

console.log(MinWindowSubstring(["aaabaaddae", "aed"])); // Output: "dae"
console.log(MinWindowSubstring(["aabdccdbcacd", "aad"])); // Output: "aabd"
