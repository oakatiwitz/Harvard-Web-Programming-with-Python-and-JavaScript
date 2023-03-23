// let counter = 0;
// ! mean not 
// if ther is no value in counter so set the value to 0
if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count(){
    // let the counter equal to the value of local counter
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    // save the latest value of counter to counter variable
    localStorage.setItem('counter', counter);

    if (counter % 10 === 0){
        // ` and $ is the same as f{} in python 
        alert(`Count is now ${counter}`);
    }
}

// addEventListener is function that takes 2 arguments, one is the event and the second is the function
// DOMContentLoaded is the event for read all the document before run the function 
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count; 

    // run the count function every 1000 ms
    setInterval(count, 1000);
});

            