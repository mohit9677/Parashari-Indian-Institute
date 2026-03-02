import { FiAward, FiBookOpen, FiHeart, FiStar } from 'react-icons/fi'
import './AboutPage.css'

const timeline = [
    { year: '2008', title: 'Began Vedic Studies', desc: 'Started formal training under renowned Jyotish gurus in Varanasi, diving deep into classical texts.' },
    { year: '2012', title: 'First 1000 Consultations', desc: 'Reached the milestone of helping over 1000 individuals through personalized astrological guidance.' },
    { year: '2016', title: 'Expanded to Numerology & Vastu', desc: 'Integrated numerology and Vastu Shastra into the practice to offer holistic life solutions.' },
    { year: '2020', title: 'Digital Presence Launched', desc: 'Brought Vedic wisdom to a global audience through online consultations and digital reports.' },
    { year: '2024', title: 'AstroBharat AI Founded', desc: 'Established AstroBharat AI to combine traditional expertise with modern technology for accessible cosmic guidance.' },
]

const expertise = [
    { icon: <FiStar />, title: 'Vedic Astrology', desc: 'Classical Jyotish with Parashari and Jaimini systems' },
    { icon: <FiBookOpen />, title: 'Numerology', desc: 'Pythagorean and Chaldean numerological analysis' },
    { icon: <FiHeart />, title: 'Vastu Shastra', desc: 'Residential and commercial space energy optimization' },
    { icon: <FiAward />, title: 'Gemology', desc: 'Vedic gemstone prescription and planetary remedies' },
]

export default function AboutPage() {
    return (
        <div className="about-page">
            <div className="page-header">
                <h1>Our <span className="gold-text">Story</span></h1>
                <p>Bridging ancient Vedic wisdom with modern seekers — a journey of cosmic dedication.</p>
            </div>

            <section className="section about-intro">
                <div className="container">
                    <div className="about-grid">
                        <div className="about-image-wrapper">
                            <div className="about-image-placeholder">
                                <span>🔮</span>
                                <p>Expert Astrologer</p>
                            </div>
                        </div>
                        <div className="about-text">
                            <h2>Dedicated to <span className="gold-text">Cosmic Truth</span></h2>
                            <p>
                                At AstroBharat AI, we believe that the ancient science of Vedic astrology holds the keys to
                                understanding life's deepest questions. Our founder began this journey over 15 years ago,
                                studying under traditional gurus in Varanasi and Kashi, immersing in the classical texts of
                                Brihat Parashara Hora Shastra and Jataka Parijata.
                            </p>
                            <p>
                                Today, our team of certified astrologers, numerologists, and Vastu experts serves thousands
                                of clients worldwide. We combine rigorous classical training with a compassionate, modern
                                approach — making cosmic wisdom accessible, actionable, and relevant to contemporary life.
                            </p>
                            <p>
                                Every reading we conduct is rooted in authentic Vedic methodology. We never use automated
                                predictions or generic reports — each consultation is a personalized dialogue between our
                                expert and your unique celestial blueprint.
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <section className="section expertise-section">
                <div className="container">
                    <h2 className="section-title">Areas of <span>Expertise</span></h2>
                    <div className="grid-2" style={{ maxWidth: '900px', margin: '2rem auto 0' }}>
                        {expertise.map((e, i) => (
                            <div key={i} className="glass-card expertise-card">
                                <div className="expertise-icon">{e.icon}</div>
                                <h3>{e.title}</h3>
                                <p>{e.desc}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            <section className="section timeline-section">
                <div className="container">
                    <h2 className="section-title">Our <span>Journey</span></h2>
                    <p className="section-subtitle">Over a decade of growth, learning, and cosmic exploration.</p>
                    <div className="timeline">
                        {timeline.map((t, i) => (
                            <div key={i} className={`timeline-item ${i % 2 === 0 ? 'left' : 'right'}`}>
                                <div className="timeline-dot" />
                                <div className="glass-card timeline-card">
                                    <div className="timeline-year">{t.year}</div>
                                    <h3>{t.title}</h3>
                                    <p>{t.desc}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>
        </div>
    )
}
