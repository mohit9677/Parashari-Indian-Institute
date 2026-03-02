import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css';

const BlogPage = () => {
    const posts = [
        {
            id: 1,
            title: "Understanding Mercury Retrograde 2024",
            excerpt: "How the upcoming transit will affect communication and technology...",
            date: "May 15, 2024",
            author: "Pt. Ram Shastri",
            slug: "mercury-retrograde-2024",
            image: "https://loremflickr.com/600/400/planet,space"
        },
        {
            id: 2,
            title: "The Power of Gemstones",
            excerpt: "Discover which gemstone aligns with your zodiac sign for maximum benefit...",
            date: "May 10, 2024",
            author: "Dr. Sunita Sharma",
            slug: "power-of-gemstones",
            image: "https://loremflickr.com/600/400/gemstone,jewelry"
        },
        {
            id: 3,
            title: "Vastu Tips for Home Office",
            excerpt: "Boost productivity and wealth by aligning your workspace correctly...",
            date: "May 05, 2024",
            author: "Acharya Vivek",
            slug: "vastu-home-office",
            image: "https://loremflickr.com/600/400/office,interior"
        },
        {
            id: 4,
            title: "Solar Eclipse Effects on Aries",
            excerpt: "What the solar eclipse means for Aries natives this year...",
            date: "April 28, 2024",
            author: "Ms. Ananya Singh",
            slug: "solar-eclipse-aries",
            image: "https://loremflickr.com/600/400/eclipse,moon"
        }
    ];

    return (
        <div className="page-wrapper">
            <div className="page-header">
                <h1>Blog & Insights</h1>
                <p>Latest articles and cosmic wisdom from our experts</p>
            </div>

            <section className="container">
                <div className="grid-cols-2" style={{ gap: '3rem' }}>
                    {posts.map(post => (
                        <div key={post.id} className="glass-panel" style={{ display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
                            <div style={{ height: '200px', overflow: 'hidden' }}>
                                <img src={post.image} alt={post.title} style={{ width: '100%', height: '100%', objectFit: 'cover', transition: 'transform 0.3s' }} className="hover-scale-img" />
                            </div>
                            <div style={{ padding: '2rem', flex: 1, display: 'flex', flexDirection: 'column' }}>
                                <div style={{ fontSize: '0.8rem', color: '#666', marginBottom: '0.5rem' }}>{post.date} • By {post.author}</div>
                                <h2 style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>{post.title}</h2>
                                <p style={{ flex: 1 }}>{post.excerpt}</p>
                                <Link to={`/blog/${post.slug}`} className="btn btn-secondary" style={{ alignSelf: 'flex-start', marginTop: '1rem' }}>Read More</Link>
                            </div>
                        </div>
                    ))}
                </div>
            </section>
        </div>
    );
};

export default BlogPage;
