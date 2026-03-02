import { useState, useEffect } from 'react'
import { Link, NavLink } from 'react-router-dom'
import { FiMenu, FiX, FiChevronDown, FiPhone, FiVideo, FiUser } from 'react-icons/fi'
import logo from '../../assets/logo.svg'
import './Navbar.css'

import { useAuth } from '../../context/AuthContext'

export default function Navbar() {
    const [isOpen, setIsOpen] = useState(false)
    const [isScrolled, setIsScrolled] = useState(false)
    const { user, logout } = useAuth() || {}; // Handle potential null context if used outside provider (though unlikely here)

    useEffect(() => {
        const handleScroll = () => {
            setIsScrolled(window.scrollY > 20)
        }
        window.addEventListener('scroll', handleScroll)
        return () => window.removeEventListener('scroll', handleScroll)
    }, [])

    return (
        <header className={`app-header ${isScrolled ? 'scrolled' : ''}`}>
            {/* Top Bar: White - Brand & Actions */}
            <div className="header-top">
                <div className="container header-top-content">
                    {/* Brand */}
                    <Link to="/" className="logo-brand" onClick={() => setIsOpen(false)}>
                        <img src={logo} alt="AstroBharat AI" className="header-logo" />
                        <div className="brand-text-wrapper">
                            <span className="brand-name">AstroBharat<span className="text-maroon">AI</span></span>
                            <span className="brand-tagline">STARS ALIGN DESTINY DIVINE</span>
                        </div>
                    </Link>

                    {/* Desktop Actions */}
                    <div className="header-actions">
                        <nav className="top-nav-items">
                            <div className="nav-dropdown-container">
                                <span className="nav-item">Services <FiChevronDown /></span>
                                <div className="nav-dropdown-menu">
                                    <Link to="/services/kundli-matching" className="dropdown-item">Kundli Matching</Link>
                                    <Link to="/services/janam-kundli" className="dropdown-item">Janam Kundli</Link>
                                    <Link to="/services/vastu-consultation" className="dropdown-item">Vastu Consultation</Link>
                                    <Link to="/services/palmistry" className="dropdown-item">Palmistry</Link>
                                    <Link to="/services/face-reading" className="dropdown-item">Face Reading</Link>
                                </div>
                            </div>

                            <div className="nav-dropdown-container">
                                <span className="nav-item">Horoscope <FiChevronDown /></span>
                                <div className="nav-dropdown-menu">
                                    <Link to="/horoscope/daily" className="dropdown-item">Daily Horoscope</Link>
                                    <Link to="/horoscope/weekly" className="dropdown-item">Weekly Horoscope</Link>
                                    <Link to="/horoscope/monthly" className="dropdown-item">Monthly Horoscope</Link>
                                    <Link to="/horoscope/yearly" className="dropdown-item">Yearly Horoscope</Link>
                                    <Link to="/horoscope/zodiac-signs" className="dropdown-item">Zodiac Signs</Link>
                                </div>
                            </div>

                            <Link to="/panchang" className="nav-item">Daily Panchang</Link>
                            <Link to="/numerology" className="nav-item">Numerology</Link>
                        </nav>

                        <div className="header-buttons">
                            <button className="btn-pill"><FiPhone /> Talk to Astrologers</button>
                            <button className="btn-pill"><FiVideo /> Live Experts</button>
                            {user ? (
                                <div className="user-menu" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                                    <span style={{ fontWeight: 'bold' }}>Hello, {user.name}</span>
                                    <button onClick={logout} className="btn-pill outline">Logout</button>
                                </div>
                            ) : (
                                <Link to="/login">
                                    <button className="btn-pill outline"><FiUser /> Login</button>
                                </Link>
                            )}
                        </div>
                    </div>

                    {/* Mobile Toggle */}
                    <div className="navbar-toggle" onClick={() => setIsOpen(!isOpen)}>
                        {isOpen ? <FiX /> : <FiMenu />}
                    </div>
                </div>
            </div>

            {/* Bottom Bar: Maroon - Main Navigation */}
            <div className={`header-bottom ${isOpen ? 'active' : ''}`}>
                <div className="container">
                    <nav className="main-nav">
                        <NavLink to="/" className={({ isActive }) => `main-link ${isActive ? 'active' : ''}`} onClick={() => setIsOpen(false)}><FiUser className="home-icon" /> Home</NavLink>
                        <NavLink to="/astrologers" className="main-link" onClick={() => setIsOpen(false)}>Astrologers</NavLink>
                        <NavLink to="/learning" className="main-link" onClick={() => setIsOpen(false)}>Digital Learning</NavLink>
                        <NavLink to="/mandir" className="main-link" onClick={() => setIsOpen(false)}>Digital Mandir</NavLink>
                        <NavLink to="/mart" className="main-link" onClick={() => setIsOpen(false)}>Digital Mart</NavLink>
                    </nav>
                </div>
            </div>
        </header>
    )
}
