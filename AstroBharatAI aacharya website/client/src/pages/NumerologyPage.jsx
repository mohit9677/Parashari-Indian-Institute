import React, { useState } from 'react';
import '../App.css';

const NumerologyPage = () => {
    const [name, setName] = useState('');
    const [date, setDate] = useState('');
    const [result, setResult] = useState(null);

    const calculateNumerology = (e) => {
        e.preventDefault();
        // Dummy calculation logic
        setResult({
            lifePath: Math.floor(Math.random() * 9) + 1,
            destiny: Math.floor(Math.random() * 9) + 1,
            soulUrge: Math.floor(Math.random() * 9) + 1
        });
    };

    return (
        <div className="page-wrapper">
            <div className="page-header">
                <h1>Numerology</h1>
                <p>Unlock the secrets hidden in your numbers</p>
            </div>

            <section className="container">
                <div className="grid-cols-2">
                    <div className="glass-panel" style={{ padding: '2rem' }}>
                        <h2 style={{ marginBottom: '1.5rem' }}>Free Numerology Calculator</h2>
                        <form onSubmit={calculateNumerology}>
                            <div style={{ marginBottom: '1rem' }}>
                                <label style={{ display: 'block', marginBottom: '0.5rem' }}>Full Name</label>
                                <input
                                    type="text"
                                    placeholder="Enter your full name"
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                    required
                                />
                            </div>
                            <div style={{ marginBottom: '1.5rem' }}>
                                <label style={{ display: 'block', marginBottom: '0.5rem' }}>Date of Birth</label>
                                <input
                                    type="date"
                                    value={date}
                                    onChange={(e) => setDate(e.target.value)}
                                    required
                                />
                            </div>
                            <button type="submit" className="btn btn-primary" style={{ width: '100%' }}>Calculate</button>
                        </form>
                    </div>

                    <div>
                        {result ? (
                            <div className="glass-panel animate-in" style={{ padding: '2rem', height: '100%' }}>
                                <h2 className="text-center text-gold">Your Numbers</h2>
                                <div style={{ marginTop: '2rem' }}>
                                    <div style={{ marginBottom: '1.5rem', textAlign: 'center' }}>
                                        <span style={{ fontSize: '3rem', fontWeight: 'bold', color: 'var(--gold-dark)', display: 'block' }}>{result.lifePath}</span>
                                        <h3>Life Path Number</h3>
                                        <p style={{ fontSize: '0.9rem', color: '#666' }}>The Life Path Number represents who you are at birth and the native traits that you will carry with you through life.</p>
                                    </div>
                                    <div style={{ display: 'flex', justifyContent: 'space-around', textAlign: 'center' }}>
                                        <div>
                                            <span style={{ fontSize: '2rem', fontWeight: 'bold', display: 'block' }}>{result.destiny}</span>
                                            <h4>Destiny</h4>
                                        </div>
                                        <div>
                                            <span style={{ fontSize: '2rem', fontWeight: 'bold', display: 'block' }}>{result.soulUrge}</span>
                                            <h4>Soul Urge</h4>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ) : (
                            <div className="glass-panel" style={{ padding: '2rem', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', textAlign: 'center' }}>
                                <h3>Why Numerology?</h3>
                                <p>Numerology is the study of the spiritual meaning of numbers. It helps you uncover your strengths, weaknesses, and life purpose.</p>
                                <p>Enter your details to get a free instant reading.</p>
                            </div>
                        )}
                    </div>
                </div>
            </section>
        </div>
    );
};

export default NumerologyPage;
