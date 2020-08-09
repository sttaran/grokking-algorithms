const getSmallest = (arr) => {
  let smallest = arr[0];
  let indexOfSmallest = 0;
  for (let idx = 1; idx < arr.length; idx += 1) {
    if (arr[idx] < smallest) {
      smallest = arr[idx];
      indexOfSmallest = idx;
    }
  }
  return indexOfSmallest;
};

const selectionSort = (arr) => {
  const sortedArr = [];
  const length = arr.length;
  for (let idx = 0; idx < length; idx += 1) {
    const smallest = arr.splice(getSmallest(arr), 1);
    sortedArr.push(...smallest);
  }
  return sortedArr;
};

console.log(selectionSort([2, 5, 6, 7, 10, 11, 14, 54, 37, 89, 4, 1]));
