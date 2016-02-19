//map transforms objects...

var animals = [
  { name: 'Fluffykins', species: 'rabbit' },
  { name: 'Caro',       species: 'dog' },
  { name: 'Hamilton',   species: 'dog' },
  { name: 'Harold',     species: 'fish' },
  { name: 'Ursula',     species: 'cat' },
  { name: 'Jimmy',      species: 'fish' }
]

/* using a for loop for what map does... */
/*
var names = [];

for( var i = 0; i < animals.length; i++){
	names.push(animals[i].name);
}
console.log(names); */

var names = animals.map(function(animal){
	return animal.name; //NOTE: you could return a completely new object in the callback
	//return animal.name + ' is a ' + animal.species;
})

console.log(names);
