// GLOBAL VARIABLES
var checkboxes = document.querySelectorAll("input");
var dogs = document.querySelectorAll(".items-to-filter li");


// TESTING EVENT.TARGET
function alertTest(event) {
    if (event.target.value == 'test') {
        alert("Testing!");
    }
}

// RESET VISIBILITY
function makeInvisible() {
    for (var i = 0; i<dogs.length; i++) {
        dogs[i].style.display = "";
    }
}
        

// MAIN FUNCTION
function filterItems(event) {
    var current_checkbox = event.target;
    
    // Initialize variables for currently visible dogs
    var visible_dogs = [];
    var visible_dogs_index = 0;

    // Populate visible_dogs (Array)
    for (var dog_index = 0; dog_index < dogs.length; dog_index++) {
        if (dogs[dog_index].style.display == "") {
            visible_dogs[visible_dogs_index] = dogs[dog_index];
            visible_dogs_index = visible_dogs_index + 1;
        }
    }

    // When user SELECTS an option
    if (current_checkbox.checked) {
        // Cycle through visible_dog (Array)
        for (var item_index = 0; item_index < visible_dogs.length; item_index++) {

            // Create array of tags from dog's "data-type" attribute
            var tags = visible_dogs[item_index].getAttribute("data-type").split(" ");
            
            // Obtain the checkbox's "value" attribute
            var wanted_tag = current_checkbox.value;

            // Check if wanted_tag is in tags
            if (tags.includes(wanted_tag) == true) {
                visible_dogs[item_index].style.display = ""; //show when checked
            } else {
                visible_dogs[item_index].style.display = "none"; //hide when checked

            }
        }
    } 
    // When user DESELECTS an option
    else { 
        // Cycle through dogs (Array)
        for (var item_index = 0; item_index < dogs.length; item_index++) {

            // Create array of tags from "data-type"
            var tags = dogs[item_index].getAttribute("data-type").split(" ");
            
            // Obtain the checkbox's "value" attribute
            var wanted_tag = current_checkbox.value;

            // Check if wanted_tags is NOT in tags
            if (tags.includes(wanted_tag) == false) {
                dogs[item_index].style.display = ""; //show when unchecked
            }
        }
    }
}

