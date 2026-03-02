import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { FiArrowRight } from 'react-icons/fi'
import API from '../api/axios'
import './ServicesPage.css'

const categories = ['All', 'Astrology', 'Numerology', 'Vastu', 'Gemstone', 'Spiritual']

export default function ServicesPage() {
    const [services, setServices] = useState([])
    const [activeCategory, setActiveCategory] = useState('All')
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetchServices()
    }, [activeCategory])

    const fetchServices = async () => {
        try {
            setLoading(true)
            const params = activeCategory !== 'All' ? { category: activeCategory } : {}
            const { data } = await API.get('/services', { params })
            setServices(data.data || [])
        } catch {
            // Fallback static data if API is not running
            setServices([
                { _id: '1', slug: 'vedic-birth-chart-analysis', icon: '🔮', title: 'Vedic Birth Chart Analysis', shortDesc: 'Comprehensive Kundli reading revealing your personality, destiny, and life patterns.', category: 'Astrology', price: '₹2,100', duration: '60 minutes', featured: true },
                { _id: '2', slug: 'relationship-compatibility-reading', icon: '💑', title: 'Relationship & Compatibility', shortDesc: 'Explore cosmic compatibility with your partner through dual-chart analysis.', category: 'Astrology', price: '₹2,500', duration: '75 minutes', featured: true },
                { _id: '3', slug: 'career-finance-forecast', icon: '💼', title: 'Career & Finance Forecast', shortDesc: 'Strategic career and financial guidance aligned with your planetary periods.', category: 'Astrology', price: '₹1,800', duration: '45 minutes' },
                { _id: '4', slug: 'numerology-life-path-reading', icon: '🔢', title: 'Numerology Life Path Reading', shortDesc: 'Discover your core purpose and hidden talents through numerological analysis.', category: 'Numerology', price: '₹1,500', duration: '45 minutes', featured: true },
                { _id: '5', slug: 'business-name-numerology', icon: '🏢', title: 'Business Name Numerology', shortDesc: 'Optimize your business name for success using numerological alignment.', category: 'Numerology', price: '₹2,000', duration: '30 minutes' },
                { _id: '6', slug: 'vastu-home-consultation', icon: '🏠', title: 'Vastu Home Consultation', shortDesc: 'Harmonize your home energy with practical Vastu corrections.', category: 'Vastu', price: '₹3,000', duration: '90 minutes', featured: true },
                { _id: '7', slug: 'vastu-office-commercial', icon: '🏗️', title: 'Vastu Office & Commercial', shortDesc: 'Optimize office energy for productivity and business success.', category: 'Vastu', price: '₹5,000', duration: '120 minutes' },
                { _id: '8', slug: 'gemstone-recommendation', icon: '💎', title: 'Gemstone Recommendation', shortDesc: 'Personalized gemstone prescriptions for planetary harmony.', category: 'Gemstone', price: '₹1,200', duration: '30 minutes' },
                { _id: '9', slug: 'spiritual-healing-session', icon: '🙏', title: 'Spiritual Healing Session', shortDesc: 'Personalized spiritual cleansing with Vedic mantras and energy healing.', category: 'Spiritual', price: '₹1,800', duration: '60 minutes' },
                { _id: '10', slug: 'puja-ritual-guidance', icon: '🕯️', title: 'Puja & Ritual Guidance', shortDesc: 'Expert puja guidance with mantras, muhurat selection, and procedures.', category: 'Spiritual', price: '₹1,500', duration: '45 minutes' },
            ].filter(s => activeCategory === 'All' || s.category === activeCategory))
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="services-page">
            <div className="page-header">
                <h1>Our <span className="gold-text">Services</span></h1>
                <p>Comprehensive cosmic guidance across astrology, numerology, Vastu, and more.</p>
            </div>

            <section className="section">
                <div className="container">
                    <div className="filter-pills">
                        {categories.map(cat => (
                            <button
                                key={cat}
                                className={`filter-pill ${activeCategory === cat ? 'active' : ''}`}
                                onClick={() => setActiveCategory(cat)}
                            >
                                {cat}
                            </button>
                        ))}
                    </div>

                    {loading ? (
                        <div className="loading-state">Loading services...</div>
                    ) : (
                        <div className="grid-3">
                            {services.map((s, i) => (
                                <div key={s._id || i} className="glass-card service-card animate-in" style={{ animationDelay: `${i * 0.08}s` }}>
                                    {s.featured && <div className="service-badge">Featured</div>}
                                    <div className="service-card-icon">{s.icon}</div>
                                    <h3>{s.title}</h3>
                                    <p className="service-card-desc">{s.shortDesc}</p>
                                    <div className="service-card-meta">
                                        <span className="service-price">{s.price}</span>
                                        <span className="service-duration">{s.duration}</span>
                                    </div>
                                    <Link to={`/services/${s.slug}`} className="btn btn-ghost service-card-btn">
                                        Learn More <FiArrowRight />
                                    </Link>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </section>
        </div>
    )
}
