var languages = {
    english: "Hello!",
    french: "Bonjour!",
    notALanguage: 4,
    spanish: "Hola!"
};

// print hello in the 3 different languages
for( var greet in languages){
		
    if( typeof languages[greet] === "string"){
        console.log(languages[greet]); 
		}
    
}
