importScripts('firebaseconfig.js');

const COHERE_API_KEY = 'PG5e48b6tFbavuqu4mRN2KwqGc6yXomEgCUxfSuz';

chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
    try {
        if (message.type === 'STORE_DATA') {
            const userId = await getUserId(); 
            for (const text of message.data) {
                const summary = await summarizeText(text);
                await db.collection('highlights').add({
                    userId: userId,
                    highlightedText: text,
                    summary: summary,
                    timestamp: firebase.firestore.FieldValue.serverTimestamp()
                });
                showNotification('Highlight Saved', 'Your highlighted text has been summarized and saved.');
            }
        } else if (message.type === 'GET_HIGHLIGHTS') {
            const userId = await getUserId();
            const highlights = await getHighlights(userId);
            sendResponse({ highlights: highlights });
        }
    } catch (error) {
        console.error('Error handling message:', error);
        showNotification('Error', 'There was an issue processing your request.');
    }
    return true;
});

async function getHighlights(userId) {
    const querySnapshot = await db.collection('highlights').where('userId', '==', userId).get();
    const highlights = [];
    querySnapshot.forEach((doc) => {
        highlights.push(doc.data());
    });
    return highlights;
}

function showNotification(title, message) {
    chrome.notifications.create({
        type: 'basic',
        iconUrl: 'icon.png', 
        title: title,
        message: message
    });
}

async function summarizeText(text) {
    try {
        const response = await fetch('https://api.cohere.ai/v1/summarize', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${COHERE_API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text, length: 'short' })
        });
        const data = await response.json();
        return data.summary;
    } catch (error) {
        console.error('Summarization API error:', error);
        return 'Error generating summary';
    }
}

async function getUserId() {
    const user = firebase.auth().currentUser;
    return user ? user.uid : 'anonymous'; 
}
