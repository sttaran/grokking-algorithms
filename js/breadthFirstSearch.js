const graph = {};

// FIRST CHAIN LINK. You are Adam and you search a seller
graph["Adam"] = ["Avram", "Bollet"];

// CHAIN FROM ADAM
graph["Avram"] = ["Sandra", "Late Seller"];
graph["Bollet"] = ["Valera Seller"];

graph["Sandra"] = [];
graph["Late Seller"] = [];
graph["Valera Seller"] = [];

const getIsSeller = (name) => (name.includes("Seller") ? true : false);

const searchOfSeller = (name) => {
  const searchQueue = [];
  searchQueue.push(...graph[name]);
  const searchedPerson = [];

  while (searchQueue.length > 0) {
    const person = searchQueue.shift();

    if (!searchedPerson.includes(person)) {
      if (getIsSeller(person)) {
        console.log(`i got it. ${person} is a seller!`);
        return true;
      } else if (graph[person]) {
        searchQueue.push(...graph[person]);
        searchedPerson.push(person);
        console.log(`${person} is not a seller!`);
      } else continue;
    }
  }
  return false;
};

console.log(searchOfSeller("Adam"));
