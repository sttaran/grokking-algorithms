const quickSort = (arr) => {
  if (arr.length < 2) {
    return arr;
  } else {
    const pivotPosition = Math.floor(Math.random() * arr.length);
    const pivot = arr[pivotPosition];

    let less = [];
    let greater = [];
    for (let i = 0; i < arr.length; i++) {
      const isPivot = i === pivotPosition;
      if (arr[i] <= pivot && !isPivot) {
        less.push(arr[i]);
      } else if (arr[i] > pivot) {
        greater.push(arr[i]);
      }
    }
    return [...quickSort(less), pivot, ...quickSort(greater)];
  }
};

const myArr = [1, 213, 3, 5, 2, 8, 7];
console.log(quickSort(myArr));
