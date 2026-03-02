import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { FiArrowLeft, FiCheck } from 'react-icons/fi'
import API from '../api/axios'
import './ServiceDetailPage.css'

export default function ServiceDetailPage() {
    const { slug } = useParams()
    const [service, setService] = useState(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const fetchService = async () => {
            try {
                const { data } = await API.get(`/services/${slug}`)
                setService(data.data)
            } catch {
                // Fallback dummy data
                const serviceData = {
                    'kundli-matching': {
                        title: 'Kundli Matching',
                        image: 'https://loremflickr.com/800/400/couple,wedding',
                        description: 'Detailed horoscope matching for marriage to ensure harmony and compatibility between partners.',
                        category: 'Vedic Astrology',
                        price: '₹1,100',
                        duration: '45 minutes',
                        benefits: ['Guna Milan', 'Mangal Dosha check', 'Compatibility analysis', 'Remedies for happy marriage']
                    },
                    'janam-kundli': {
                        title: 'Janam Kundli',
                        image: 'https://loremflickr.com/800/400/astrology,chart',
                        description: 'Complete birth chart analysis to understand your personality, life path, and future possibilities.',
                        category: 'Vedic Astrology',
                        price: '₹2,500',
                        duration: '60 minutes',
                        benefits: ['Life predictions', 'Career guidance', 'Health analysis', 'Dasha periods']
                    },
                    'vastu-consultation': {
                        title: 'Vastu Consultation',
                        image: 'https://loremflickr.com/800/400/home,architecture',
                        description: 'Optimize your living and workspace with ancient science of architecture for health, wealth, and prosperity.',
                        category: 'Vastu Shastra',
                        price: '₹5,100',
                        duration: '90 minutes',
                        benefits: ['Home/Office layout check', 'Remedial suggestions', 'Energy balancing', 'Color therapy']
                    },
                    'palmistry': {
                        title: 'Palmistry',
                        image: 'https://loremflickr.com/800/400/hand,palm',
                        description: 'Uncover your destiny through the lines of your hands. A unique insight into your character and future.',
                        category: 'Hast Samudrika',
                        price: '₹1,500',
                        duration: '45 minutes',
                        benefits: ['Life line analysis', 'Career & Wealth lines', 'Relationship indicators', 'Health warnings']
                    },
                    'face-reading': {
                        title: 'Face Reading',
                        image: 'https://loremflickr.com/800/400/face,portrait',
                        description: 'Analyze facial features to determine character, fate, and potential life outcomes.',
                        category: 'Physiognomy',
                        price: '₹1,500',
                        duration: '45 minutes',
                        benefits: ['Personality assessment', 'Hidden talents', 'Future trends', 'Health indicators']
                    }
                };

                const data = serviceData[slug] || {
                    title: slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '),
                    image: 'https://loremflickr.com/800/400/astrology,stars',
                    description: 'Gain deep insights into your life path through our expert consultation.',
                    category: 'Astrology',
                    price: '₹2,100',
                    duration: '60 minutes',
                    benefits: ['Detailed planetary analysis', 'Personalized guidance', 'Remedial measures', 'Follow-up support'],
                };
                setService(data);
            } finally {
                setLoading(false)
            }
        }
        fetchService()
    }, [slug])

    if (loading) return <div className="page-header"><h1>Loading...</h1></div>
    if (!service) return <div className="page-header"><h1>Service Not Found</h1></div>

    return (
        <div className="service-detail-page page-wrapper">
            <div className="page-header">
                <Link to="/services" className="back-link"><FiArrowLeft /> All Services</Link>
                {service.image && (
                    <div style={{ width: '100%', height: '300px', borderRadius: '12px', overflow: 'hidden', marginBottom: '2rem' }}>
                        <img src={service.image} alt={service.title} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                    </div>
                )}
                <h1>{service.title}</h1>
                <p>{service.category} • {service.duration}</p>
            </div>

            <section className="section">
                <div className="container detail-grid">
                    <div className="detail-content">
                        <h2>About This Service</h2>
                        <p className="detail-desc">{service.description}</p>

                        {service.benefits && service.benefits.length > 0 && (
                            <>
                                <h3>What You'll Receive</h3>
                                <ul className="benefits-list">
                                    {service.benefits.map((b, i) => (
                                        <li key={i}><FiCheck className="benefit-icon" /> {b}</li>
                                    ))}
                                </ul>
                            </>
                        )}
                    </div>

                    <div className="detail-sidebar">
                        <div className="glass-card pricing-card">
                            <div className="pricing-price">{service.price}</div>
                            <div className="pricing-duration">{service.duration} session</div>
                            <Link to="/book" className="btn btn-primary" style={{ width: '100%', justifyContent: 'center' }}>
                                Book This Service
                            </Link>
                            <p className="pricing-note">Satisfaction guaranteed. Response within 24 hours.</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
}
