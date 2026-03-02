import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import '../App.css';

const HoroscopePage = () => {
    const { type } = useParams();
    const [content, setContent] = useState(null);

    useEffect(() => {
        // Dummy data for different horoscope types
        const horoscopeData = {
            'daily': {
                title: 'Daily Horoscope',
                subtitle: 'Your celestial guidance for today',
                description: 'Plan your day with the help of the stars. Discover what the cosmos has in store for love, career, and health.',
                cards: ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
            },
            'weekly': {
                title: 'Weekly Horoscope',
                subtitle: 'Insights for the week ahead',
                description: 'Prepare for the week with detailed predictions. Know when to act and when to pause.',
                cards: ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
            },
            'monthly': {
                title: 'Monthly Horoscope',
                subtitle: 'Your month at a glance',
                description: 'A comprehensive overview of the month. Key dates and planetary movements affecting your sign.',
                cards: ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
            },
            'yearly': {
                title: 'Yearly Horoscope 2024',
                subtitle: 'The year of transformation',
                description: 'Detailed yearly predictions covering all aspects of life: Career, Finance, Health, and Relationships.',
                cards: ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
            },
            'zodiac-signs': {
                title: 'Zodiac Signs',
                subtitle: 'Unlock the mysteries of the 12 signs',
                description: 'Deep dive into the traits, compatibility, and secrets of each zodiac sign.',
                cards: ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
            },
        };

        setContent(horoscopeData[type] || horoscopeData['daily']);
    }, [type]);

    if (!content) return <div>Loading...</div>;

    const getIcon = (sign) => {
        const icons = {
            'Aries': '♈', 'Taurus': '♉', 'Gemini': '♊', 'Cancer': '♋',
            'Leo': '♌', 'Virgo': '♍', 'Libra': '♎', 'Scorpio': '♏',
            'Sagittarius': '♐', 'Capricorn': '♑', 'Aquarius': '♒', 'Pisces': '♓'
        };
        return icons[sign] || '⭐';
    };

    return (
        <div className="page-wrapper">
            <div className="page-header">
                <h1>{content.title}</h1>
                <p>{content.subtitle}</p>
            </div>

            <section className="container">
                <div className="glass-panel" style={{ textAlign: 'center', marginBottom: '3rem', maxWidth: '800px', margin: '0 auto 3rem' }}>
                    <p style={{ fontSize: '1.2rem', color: '#555' }}>{content.description}</p>
                </div>

                <div className="grid-cols-3" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '2rem' }}>
                    {content.cards.map((sign) => (
                        <div key={sign} className="glass-panel hover-scale" style={{ textAlign: 'center', padding: '2rem', cursor: 'pointer' }}>
                            <div style={{ fontSize: '3rem', marginBottom: '1rem', color: 'var(--color-primary)' }}>{getIcon(sign)}</div>
                            <h3 style={{ marginBottom: '0.5rem' }}>{sign}</h3>
                            <p style={{ fontSize: '0.9rem', color: '#666' }}>
                                {type === 'zodiac-signs'
                                    ? `Traits & Personality`
                                    : `Read your ${type} forecast`}
                            </p>
                            <button className="btn btn-secondary" style={{ marginTop: '1rem', padding: '0.5rem 1.5rem', fontSize: '0.8rem' }}>Read Now</button>
                        </div>
                    ))}
                </div>
            </section>
        </div>
    );
};

export default HoroscopePage;
