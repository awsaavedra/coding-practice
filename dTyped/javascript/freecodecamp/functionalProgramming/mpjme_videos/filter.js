var triple = function(x){
	return x * 3;
}

var waffle = triple;

waffle(30);

// filter example\\\\\\\\\

var animals = [
  { name: 'Fluffykins', species: 'rabbit' },
  { name: 'Caro',       species: 'dog' },
  { name: 'Hamilton',   species: 'dog' },
  { name: 'Harold',     species: 'fish' },
  { name: 'Ursula',     species: 'cat' },
  { name: 'Jimmy',      species: 'fish' }
];


//normal way to filter without the filter method
/*
var dogs = [];

for( var i = 0; i < animals.length; i++){
	if( animals[i].species === 'dog')
		dogs.push(animals[i]);
}
console.log(dogs);
*/

//functional programming using filter function
var dogs = animals.filter(function(animal){
	return animal.species == 'dog';
});

console.log(dogs);
