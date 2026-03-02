import { Link } from 'react-router-dom'
import { FiInstagram, FiYoutube, FiTwitter, FiMail } from 'react-icons/fi'
import logo from '../../assets/logo.svg'
import './Footer.css'

export default function Footer() {
    return (
        <footer className="footer">
            <div className="container">
                <div className="footer-content">
                    <div className="footer-brand">
                        <Link to="/" className="footer-logo">
                            <img src={logo} alt="AstroBharat AI" className="footer-logo-img" />
                        </Link>
                        <p className="footer-tagline">
                            Ancient Wisdom, Modern Insight.
                        </p>
                    </div>

                    <div className="footer-links">
                        <Link to="/about">About</Link>
                        <Link to="/services">Services</Link>
                        <Link to="/privacy">Privacy</Link>
                        <Link to="/terms">Terms</Link>
                    </div>

                    <div className="footer-socials">
                        <a href="https://www.instagram.com/astrobharatai" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><FiInstagram /></a>
                        <a href="#" aria-label="Twitter"><FiTwitter /></a> {/* Twitter not found, kept as placeholder */}
                        <a href="https://www.youtube.com/@AstroBharatAI" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><FiYoutube /></a>
                        <a href="mailto:support@astrobharatai.com" aria-label="Email"><FiMail /></a>
                    </div>
                </div>

                <div className="footer-bottom">
                    <p>&copy; {new Date().getFullYear()} AstroBharat AI. All rights reserved.</p>
                </div>
            </div>
        </footer>
    )
}
