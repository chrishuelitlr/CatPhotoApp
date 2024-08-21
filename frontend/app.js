document.getElementById('getCatImageButton').addEventListener('click', getRandomCat);

async function getRandomCat() {
    try {
        // Make a GET request to The Cat API
        const response = await fetch('https://api.thecatapi.com/v1/images/search');
        
        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response as JSON
        const data = await response.json();
        
        // Display the cat image by setting the src attribute of the img element
        document.getElementById('catImage').src = data[0].url;
    } catch (error) {
        console.error('Error fetching the cat image:', error);
    }
}

// Load a cat image on page load
getRandomCat();
