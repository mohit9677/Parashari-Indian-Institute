import { Routes, Route } from 'react-router-dom'
import Navbar from './components/layout/Navbar'
import Footer from './components/layout/Footer'
import HomePage from './pages/HomePage'
import AboutPage from './pages/AboutPage'
import ServicesPage from './pages/ServicesPage'
import ServiceDetailPage from './pages/ServiceDetailPage'
import BookingPage from './pages/BookingPage'
import ReportsPage from './pages/ReportsPage'
import BlogPage from './pages/BlogPage'
import ArticleDetailPage from './pages/ArticleDetailPage'
import ContactPage from './pages/ContactPage'
import NotFoundPage from './pages/NotFoundPage'

import { AuthProvider } from './context/AuthContext'
import LoginPage from './pages/LoginPage'
import SignupPage from './pages/SignupPage'
import HoroscopePage from './pages/HoroscopePage'
import PanchangPage from './pages/PanchangPage'
import NumerologyPage from './pages/NumerologyPage'
import AstrologersPage from './pages/AstrologersPage'
import AIAstrologersPage from './pages/AIAstrologersPage'
import LearningPage from './pages/LearningPage'
import MandirPage from './pages/MandirPage'
import MartPage from './pages/MartPage'

import FloatingChatbot from './components/FloatingChatbot'

function App() {
    return (
        <AuthProvider>
            <Navbar />
            <FloatingChatbot />
            <main>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/services" element={<ServicesPage />} />
                    <Route path="/services/:slug" element={<ServiceDetailPage />} />
                    <Route path="/horoscope/:type" element={<HoroscopePage />} />
                    <Route path="/panchang" element={<PanchangPage />} />
                    <Route path="/numerology" element={<NumerologyPage />} />
                    <Route path="/astrologers" element={<AstrologersPage />} />
                    <Route path="/ai-astrologers" element={<AIAstrologersPage />} />
                    <Route path="/learning" element={<LearningPage />} />
                    <Route path="/mandir" element={<MandirPage />} />
                    <Route path="/mart" element={<MartPage />} />
                    <Route path="/book" element={<BookingPage />} />
                    <Route path="/reports" element={<ReportsPage />} />
                    <Route path="/blog" element={<BlogPage />} />
                    <Route path="/blog/:slug" element={<ArticleDetailPage />} />
                    <Route path="/contact" element={<ContactPage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/signup" element={<SignupPage />} />
                    <Route path="*" element={<NotFoundPage />} />
                </Routes>
            </main>

            <Footer />
        </AuthProvider>
    )
}

export default App
