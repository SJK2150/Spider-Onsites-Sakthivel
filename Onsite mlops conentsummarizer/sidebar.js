chrome.runtime.sendMessage({ type: 'GET_HIGHLIGHTS' }, response => {
    const highlightsContainer = document.getElementById('highlights');
    if (response.highlights.length > 0) {
        response.highlights.forEach(highlight => {
            const highlightElement = document.createElement('div');
            highlightElement.className = 'highlight';
            highlightElement.innerHTML = `
                <strong>Highlighted Text:</strong> ${highlight.highlightedText}<br>
                <strong>Summary:</strong> ${highlight.summary}
            `;
            highlightsContainer.appendChild(highlightElement);
        });
    } else {
        highlightsContainer.innerText = 'No highlights saved.';
    }
});
