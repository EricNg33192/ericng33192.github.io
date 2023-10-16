// hex.js
function add(a, b) {
  const hexA = parseInt(a, 16);
  const hexB = parseInt(b, 16);
  const result = (hexA + hexB).toString(16);
  return result;
}

function isValid(value) {
  return /^[0-9a-fA-F]+$/.test(value);
}

export { add, isValid };
