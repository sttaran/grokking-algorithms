const binarySearch = (list, item) => {
  let low = 0;
  let high = list.length - 1;
  while (low <= high) {
    const middle = Math.trunc((low + high) / 2);
    const guess = list[middle];
    if (item > guess) {
      low = middle + 1;
      console.log(`Number > then  ${guess}, range = ${low}-${high}`);
    } else if (item < guess) {
      high = middle - 1;
      console.log(`Number < then  ${guess}, range = ${low}-${high}`);
    } else {
      console.log(`Number was found - ${guess}`);
      return list.indexOf(middle);
    }
    console.log("НОВАЯ ПОПЫТКА!");
  }
};

const myArr = [
  0,
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  20,
  21,
  22,
  23,
  24,
  25,
];

binarySearch(myArr, 8);
