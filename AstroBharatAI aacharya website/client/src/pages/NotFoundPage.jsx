
import { Link } from 'react-router-dom'
import { FiHome, FiArrowLeft } from 'react-icons/fi'

export default function NotFoundPage() {
    return (
        <div className="page-wrapper">
            <div className="container not-found-container animate-in">
                <h1 className="error-code">404</h1>
                <h2 className="text-gold">Page Not Found</h2>
                <p className="text-muted" style={{ maxWidth: '400px', margin: '1rem auto 2rem' }}>
                    The stars have not aligned for this path. It seems the page you are looking for has vanished into the cosmos.
                </p>
                <div className="flex-center" style={{ gap: '1rem' }}>
                    <button onClick={() => window.history.back()} className="btn btn-secondary">
                        <FiArrowLeft style={{ marginRight: '0.5rem' }} /> Go Back
                    </button>
                    <Link to="/" className="btn btn-primary">
                        <FiHome style={{ marginRight: '0.5rem' }} /> Return Home
                    </Link>
                </div>
            </div>
        </div>
    )
}
