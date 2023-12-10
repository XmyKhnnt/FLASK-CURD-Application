function removeQueryParameters() {
    // Get the current URL
    var url = window.location.href;

    // Check if the URL contains a query string
    if (url.includes('?')) {
        // Remove the query string and everything after it
        url = url.split('?')[0];

        // Use history.replaceState to update the URL without reloading the page
        history.replaceState(null, '', url);
    }
}

// Call the function when the page is loaded or reloaded
window.addEventListener('load', removeQueryParameters);
