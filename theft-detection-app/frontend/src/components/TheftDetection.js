import React, { useState } from 'react';
import axios from 'axios';

const TheftDetection = () => {
    const [videoFeed, setVideoFeed] = useState('');
    const [alertMessage, setAlertMessage] = useState('');

    const handleVideoFeedChange = (event) => {
        setVideoFeed(event.target.value);
    };

    const startDetection = async () => {
        try {
            const response = await axios.post('/api/detect-theft', { videoFeed });
            if (response.data.alert) {
                setAlertMessage('Theft detected! Alert has been sent.');
            } else {
                setAlertMessage('No theft detected.');
            }
        } catch (error) {
            console.error('Error during theft detection:', error);
            setAlertMessage('Error during detection. Please try again.');
        }
    };

    return (
        <div className="theft-detection">
            <h2>Theft Detection</h2>
            <input
                type="text"
                placeholder="Enter video feed URL"
                value={videoFeed}
                onChange={handleVideoFeedChange}
            />
            <button onClick={startDetection}>Start Detection</button>
            {alertMessage && <p>{alertMessage}</p>}
        </div>
    );
};

export default TheftDetection;