import React from 'react';
import './styles/App.css';
import TheftDetection from './components/TheftDetection';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Theft Detection Application</h1>
            </header>
            <main>
                <TheftDetection />
            </main>
        </div>
    );
}

export default App;