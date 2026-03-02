import React from 'react';
import '../App.css';

const MandirPage = () => {
    return (
        <div className="page-wrapper">
            <div className="page-header">
                <h1>Digital Mandir</h1>
                <p>Perform daily rituals and darshan from anywhere</p>
            </div>

            <section className="container">
                <div className="grid-cols-2">
                    <div className="glass-panel" style={{ padding: '2rem', textAlign: 'center' }}>
                        <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>🕉️</div>
                        <h2>Live Darshan</h2>
                        <p>Watch live aarti from major temples across India.</p>
                        <button className="btn btn-primary">Watch Now</button>
                    </div>
                    <div className="glass-panel" style={{ padding: '2rem', textAlign: 'center' }}>
                        <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>🙏</div>
                        <h2>Book Puja</h2>
                        <p>Perform personalized puja with certified pandits online.</p>
                        <button className="btn btn-secondary">Book Service</button>
                    </div>
                </div>

                <div style={{ marginTop: '4rem', textAlign: 'center' }}>
                    <h2 className="section-title">Todays Chants</h2>
                    <div className="glass-panel" style={{ maxWidth: '600px', margin: '2rem auto', padding: '2rem' }}>
                        <p style={{ fontSize: '1.5rem', fontWeight: 'bold', fontStyle: 'italic', marginBottom: '1rem' }}>
                            "Om Bhur Bhuva Swaha, Tat Savitur Varenyam<br />
                            Bhargo Devasya Dheemahi, Dhiyo Yo Nah Prachodayat"
                        </p>
                        <p className="text-gold">Gayatri Mantra - For Wisdom and Enlightenment</p>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default MandirPage;
