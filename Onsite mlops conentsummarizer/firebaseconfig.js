import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.22.1/firebase-app.js';
import { getFirestore, collection, addDoc, getDocs } from 'https://www.gstatic.com/firebasejs/9.22.1/firebase-firestore.js';

const firebaseConfig = {
  apiKey: "AIzaSyDOPxpnsgFc38sbNiPVk0FfeDProIOf6WQ",
  authDomain: "summarizer-65efc.firebaseapp.com",
  databaseURL: "https://summarizer-65efc-default-rtdb.firebaseio.com",
  projectId: "summarizer-65efc",
  storageBucket: "summarizer-65efc.appspot.com",
  messagingSenderId: "416302751701",
  appId: "1:416302751701:web:14376d330f3aa19c4be75c",
  measurementId: "G-0P52HR5K96"
};


const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export { db, collection, addDoc, getDocs };
