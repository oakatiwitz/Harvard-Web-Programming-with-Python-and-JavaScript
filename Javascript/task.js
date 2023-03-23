// Read all the content in HTML file
document.addEventListener('DOMContentLoaded', () => {

    // By default, submit button is disabled
    document.querySelector('#submit').disabled = true;

    // When user typing submit button is enabled
    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0){
            document.querySelector('#submit').disabled = false;    
        } 
        // When the content in input task is empty, set the submit button to disabled
        else {
            document.querySelector('#submit').disabled = true; 
        }  
    }

    // When click submit in form
    document.querySelector('form').onsubmit = () => {
        // Give the variable task equal to the input on form
        const task = document.querySelector('#task').value;
        
        // Show in console
        console.log(task);

        // Create a new variable name 'li' and give it equal to the variable task 
        const li = document.createElement('li');
        li.innerHTML = task;

        // Append list in unorder list which has id="tasks"
        document.querySelector('#tasks').append(li);

        // Set the value in select form to empty
        document.querySelector('#task').value = '';

        // Set the submit button to disabled
        document.querySelector('#submit').disabled = true;

        // Stop form from submitting
        return false;
    }
});