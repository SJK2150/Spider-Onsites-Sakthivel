async function fetchRedditComments(subreddit, postId) {
    try {
        const response = await fetch(`https://www.reddit.com/r/${subreddit}/comments/${postId}.json`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data[1].data.children.map(comment => comment.data.body); 
    } catch (error) {
        console.error('Failed to fetch Reddit comments:', error);
        return [];
    }
}

function getYouTubeTranscript() {
    const transcript = [];
    document.querySelectorAll('.ytd-transcript-segment-renderer .style-scope').forEach(line => {
        transcript.push(line.innerText);
        console.log("got")
    });
    return transcript;
}

function sendExtractedData() {
    if (window.location.hostname === 'www.reddit.com') {
        const subreddit = window.location.pathname.split('/')[2];
        console.log(subreddit)
        const postId = window.location.pathname.split('/')[4];
        fetchRedditComments(subreddit, postId).then(comments => {
            chrome.runtime.sendMessage({ type: 'STORE_DATA', data: comments });
        });
    } else if (window.location.hostname === 'www.youtube.com') {
        const transcript = getYouTubeTranscript();
        chrome.runtime.sendMessage({ type: 'STORE_DATA', data: transcript });
    }
}

document.addEventListener('mouseup', () => {
    const selection = window.getSelection().toString().trim();
    if (selection) {
        chrome.runtime.sendMessage({ type: 'STORE_DATA', data: [selection] });
    }
});

sendExtractedData();
