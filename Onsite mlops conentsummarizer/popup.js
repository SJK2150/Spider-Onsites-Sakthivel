document.getElementById('summarizeButton').addEventListener('click', () => {
    chrome.tabs.executeScript({
        code: "window.getSelection().toString();"
    }, selection => {
        const highlightedText = selection[0];

        if (highlightedText.trim() === '') {
            document.getElementById('status').innerText = 'No text highlighted.';
        } else {
            chrome.runtime.sendMessage({ type: 'SUMMARIZE', text: highlightedText }, response => {
                const highlightsContainer = document.getElementById('highlights');
                if (response.summary) {
                    document.getElementById('status').innerText = '';
                    const highlightElement = document.createElement('div');
                    highlightElement.className = 'highlight';
                    highlightElement.innerHTML = `
                        <strong>Highlighted Text:</strong> ${highlightedText}<br>
                        <strong>Summary:</strong> ${response.summary}
                    `;
                    highlightsContainer.appendChild(highlightElement);
                }
            });
        }
    });
});
