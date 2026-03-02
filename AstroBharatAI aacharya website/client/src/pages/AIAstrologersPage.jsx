import React from 'react';
import '../App.css';
import ChatInterface from '../components/ChatInterface';

const AIAstrologersPage = () => {
    return (
        <div className="page-wrapper">
            <div className="page-header">
                <h1>AI Astrologer</h1>
                <p>Instant cosmic guidance powered by advanced Vedic algorithms</p>
            </div>

            <section className="container">
                <div className="glass-panel" style={{ height: '600px', maxWidth: '800px', margin: '0 auto', overflow: 'hidden' }}>
                    <ChatInterface />
                </div>
            </section>
        </div>
    );
};

export default AIAstrologersPage;
