import { Link } from 'react-router-dom'
import { FiArrowRight, FiShield, FiTrendingUp, FiCheck, FiStar, FiUser, FiGlobe } from 'react-icons/fi'
import { RiStarSFill, RiDoubleQuotesL } from 'react-icons/ri'
import './HomePage.css'

export default function HomePage() {
    return (
        <div className="home-page">
            {/* ── 1. Hero Section ── */}
            <section className="hero-section">
                <div className="container hero-container">
                    <div className="hero-content">
                        <div className="hero-badge animate-in">
                            <RiStarSFill /> AI-Powered Vedic Astrology
                        </div>
                        <h1 className="animate-in" style={{ animationDelay: '0.1s' }}>
                            Unlock Your <span className="text-gradient">Cosmic Path</span>
                        </h1>
                        <p className="hero-subtitle animate-in" style={{ animationDelay: '0.2s' }}>
                            Gain instant clarity on your career, relationships, and destiny with
                            precision Vedic astrology readings powered by advanced AI.
                        </p>
                        <div className="hero-actions animate-in" style={{ animationDelay: '0.3s' }}>
                            <Link to="/book" className="btn btn-primary">
                                Get Your Reading <FiArrowRight />
                            </Link>
                            <Link to="/reports" className="btn btn-secondary">
                                View Sample Report
                            </Link>
                        </div>
                        <p className="hero-note animate-in" style={{ animationDelay: '0.4s' }}>
                            <FiStar className="text-gold" /> No birth time? We can help rectify it.
                        </p>
                    </div>
                    {/* Visual: Subtle Zodiac Wheel (CSS/SVG) */}
                    <div className="hero-visual animate-in" style={{ animationDelay: '0.5s' }}>
                        <div className="zodiac-wheel">
                            <div className="zodiac-inner-glow"></div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ── 2. How It Works ── */}
            <section className="steps-section">
                <div className="container">
                    <h2 className="section-title">How It Works</h2>
                    <div className="steps-grid">
                        <div className="step-card glass-panel">
                            <div className="step-number">01</div>
                            <h3>Enter Details</h3>
                            <p>Share your birth date, time, and location to generate your unique chart.</p>
                        </div>
                        <div className="step-card glass-panel">
                            <div className="step-number">02</div>
                            <h3>AI Analysis</h3>
                            <p>Our AI analyzes planetary positions, dashas, and yogas instantly.</p>
                        </div>
                        <div className="step-card glass-panel">
                            <div className="step-number">03</div>
                            <h3>Get Guidance</h3>
                            <p>Receive a detailed, easy-to-understand report with actionable remedies.</p>
                        </div>
                    </div>
                </div>
            </section>

            {/* ── 3. Trust Section ── */}
            <section className="trust-section">
                <div className="container">
                    <div className="trust-grid">
                        <div className="trust-item">
                            <FiUser className="trust-icon" />
                            <div className="trust-text">
                                <h4>10,000+</h4>
                                <p>Happy Users</p>
                            </div>
                        </div>
                        <div className="trust-item">
                            <FiShield className="trust-icon" />
                            <div className="trust-text">
                                <h4>Privacy First</h4>
                                <p>Data Not Stored</p>
                            </div>
                        </div>
                        <div className="trust-item">
                            <FiGlobe className="trust-icon" />
                            <div className="trust-text">
                                <h4>Vedic Accuracy</h4>
                                <p>Ancient Wisdom</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ── 4. Product Preview ── */}
            <section className="preview-section">
                <div className="container">
                    <div className="preview-layout">
                        <div className="preview-content">
                            <h2 className="text-left">Crystal Clear Insights</h2>
                            <p>Most astrology reports are confusing. Ours are designed for clarity.</p>
                            <ul className="benefits-list">
                                <li><FiCheck className="text-gold" /> <strong>Plain English:</strong> No complex jargon without explanation.</li>
                                <li><FiCheck className="text-gold" /> <strong>Actionable Remedies:</strong> Simple rituals and gemstones.</li>
                                <li><FiCheck className="text-gold" /> <strong>5-Year Forecast:</strong> Know what's coming next.</li>
                            </ul>
                            <Link to="/reports" className="btn btn-primary">
                                See Detailed Features
                            </Link>
                        </div>
                        <div className="preview-visual glass-panel">
                            {/* Mockup UI representation */}
                            <div className="mockup-header">
                                <div className="mockup-dot red"></div>
                                <div className="mockup-dot yellow"></div>
                                <div className="mockup-dot green"></div>
                            </div>
                            <div className="mockup-body">
                                <div className="mockup-line title"></div>
                                <div className="mockup-line"></div>
                                <div className="mockup-line"></div>
                                <div className="mockup-chart-placeholder">
                                    <div className="mockup-pie"></div>
                                </div>
                                <div className="mockup-line"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ── 5. Pricing ── */}
            <section className="pricing-section">
                <div className="container">
                    <h2 className="section-title">Simple Pricing</h2>
                    <div className="pricing-grid">
                        <div className="pricing-card glass-panel">
                            <h3>Basic Report</h3>
                            <div className="price">₹499</div>
                            <ul className="features-list">
                                <li><FiCheck /> Birth Chart Analysis</li>
                                <li><FiCheck /> Personality Insights</li>
                                <li><FiCheck /> Basic Remedies</li>
                            </ul>
                            <Link to="/book" className="btn btn-secondary width-full">Choose Basic</Link>
                        </div>
                        <div className="pricing-card glass-panel popular">
                            <div className="popular-tag">Most Popular</div>
                            <h3>Premium Guidance</h3>
                            <div className="price">₹999</div>
                            <ul className="features-list">
                                <li><FiCheck /> <strong>Everything in Basic</strong></li>
                                <li><FiCheck /> 5-Year Life Predictions</li>
                                <li><FiCheck /> Career & Love Analysis</li>
                                <li><FiCheck /> Detailed Gemstone Report</li>
                                <li><FiCheck /> Ask 3 Specific Questions</li>
                            </ul>
                            <Link to="/book" className="btn btn-primary width-full">Get Premium</Link>
                        </div>
                    </div>
                </div>
            </section>

            {/* ── 6. Final CTA ── */}
            <section className="final-cta-section">
                <div className="container text-center">
                    <h2 className="cta-title">Start Your Cosmic Journey</h2>
                    <p className="cta-subtitle">
                        Don't leave your destiny to chance. Get the guidance you need today.
                    </p>
                    <Link to="/book" className="btn btn-primary btn-large">
                        Get Your Reading Now
                    </Link>
                    <p className="cta-guarantee">
                        <FiShield size={14} /> 100% Satisfaction Guarantee
                    </p>
                </div>
            </section>
        </div>
    )
}
