// binary.js
function add(a, b) {
  const binaryA = parseInt(a, 2);
  const binaryB = parseInt(b, 2);
  const result = (binaryA + binaryB).toString(2);
  return result;
}

function isValid(value) {
  return /^[01]+$/.test(value);
}

export { add, isValid };
