import { FiStar, FiPhone, FiMessageCircle } from 'react-icons/fi';
import hemantBarua from '../assets/hemant_barua.png';
import knRao from '../assets/kn_rao.png';
import sanjayJumaani from '../assets/sanjay_jumaani.png';
import ajaiBhambi from '../assets/ajai_bhambi.png';
import sandeepKochar from '../assets/sandeep_kochar.png';
import gdVashist from '../assets/gd_vashist.png';
import deepakKapoor from '../assets/deepak_kapoor.png';
import induPrakash from '../assets/indu_prakash.png';
import premSharma from '../assets/prem_sharma.png';
import sohiniShastri from '../assets/sohini_shastri.png';

const AstrologersPage = () => {
    const astrologers = [
        { id: 1, name: "Dr. Hemant Barua", specialty: "Vedic Astrology", exp: "25+ Years", language: "English, Hindi", rating: 4.9, image: hemantBarua },
        { id: 2, name: "Shri K.N. Rao", specialty: "Vedic Astrology", exp: "50+ Years", language: "English, Hindi", rating: 5.0, image: knRao },
        { id: 3, name: "Sanjay B Jumaani", specialty: "Numerology", exp: "20+ Years", language: "English, Hindi", rating: 4.8, image: sanjayJumaani },
        { id: 4, name: "Pt. Ajai Bhambi Ji", specialty: "Vedic Astrology", exp: "40+ Years", language: "Hindi, English", rating: 4.9, image: ajaiBhambi },
        { id: 5, name: "Dr. Sandeep Kochar", specialty: "Vastu & Astrology", exp: "20+ Years", language: "English, Hindi, Punjabi", rating: 4.7, image: sandeepKochar },
        { id: 6, name: "Pt. GD Vashist", specialty: "Lal Kitab", exp: "30+ Years", language: "Hindi, English", rating: 4.8, image: gdVashist },
        { id: 7, name: "Shri Deepak Kapoor", specialty: "Vedic Astrology", exp: "35+ Years", language: "Hindi, English", rating: 4.8, image: deepakKapoor },
        { id: 8, name: "Acharya Indu Prakash", specialty: "Vastu & Astrology", exp: "25+ Years", language: "Hindi", rating: 4.9, image: induPrakash },
        { id: 9, name: "Dr. Prem Kumar Sharma", specialty: "Vedic Astrology", exp: "20+ Years", language: "English, Hindi", rating: 4.8, image: premSharma },
        { id: 10, name: "Dr. Sohini Shastri", specialty: "KP Astrology", exp: "15+ Years", language: "English, Bengali", rating: 4.9, image: sohiniShastri },
    ];

    return (
        <div className="page-wrapper">
            <div className="page-header">
                <h1>Talk to Astrologers</h1>
                <p>Connect with India's top certified astrologers for instant guidance</p>
            </div>

            <section className="container">
                <div className="grid-cols-3" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '2rem' }}>
                    {astrologers.map(astro => (
                        <div key={astro.id} className="glass-panel" style={{ padding: '1.5rem', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                            <div style={{ width: '100px', height: '100px', borderRadius: '50%', background: '#eee', marginBottom: '1rem', overflow: 'hidden', border: '3px solid var(--primary-gold)' }}>
                                <img
                                    src={astro.image}
                                    alt={astro.name}
                                    style={{
                                        width: '100%',
                                        height: '100%',
                                        objectFit: 'cover',
                                        objectPosition: 'top center' // Ensures face is visible
                                    }}
                                />
                            </div>
                            <h3 style={{ margin: '0.5rem 0' }}>{astro.name}</h3>
                            <p className="text-gold" style={{ fontWeight: '600', marginBottom: '0.5rem' }}>{astro.specialty}</p>
                            <div style={{ fontSize: '0.9rem', color: '#666', marginBottom: '1rem', width: '100%' }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.25rem' }}>
                                    <span>Experience:</span>
                                    <span>{astro.exp}</span>
                                </div>
                                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.25rem' }}>
                                    <span>Language:</span>
                                    <span>{astro.language}</span>
                                </div>
                                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                    <span>Rating:</span>
                                    <span>⭐ {astro.rating}</span>
                                </div>
                            </div>
                            <div style={{ display: 'flex', gap: '1rem', width: '100%' }}>
                                <button className="btn btn-secondary" style={{ flex: 1, padding: '0.5rem' }}>Chat</button>
                                <button className="btn btn-primary" style={{ flex: 1, padding: '0.5rem' }}>Call</button>
                            </div>
                        </div>
                    ))}
                </div>
            </section>
        </div>
    );
};

export default AstrologersPage;
