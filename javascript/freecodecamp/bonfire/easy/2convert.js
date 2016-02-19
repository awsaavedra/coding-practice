/*
Convert the characters "&", "<", ">", '"' (double quote), 
and "'" (apostrophe), in a string to their corresponding HTML entities.
*/
//just used replace, multiple ways to do this but regex is prob best
function convert(str) {
  
	return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g,'&apos;');
}

convert('Dolce & Gabbana');
