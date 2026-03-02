import React from 'react'
import { useParams } from 'react-router-dom'

export default function ArticleDetailPage() {
    const { slug } = useParams()
    return (
        <div className="page-wrapper">
            <div className="container" style={{ padding: '4rem 2rem' }}>
                <h1>Article: {slug}</h1>
                <p>Content coming soon.</p>
            </div>
        </div>
    )
}
