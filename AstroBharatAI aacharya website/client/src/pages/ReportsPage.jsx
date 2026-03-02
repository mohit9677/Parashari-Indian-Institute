import toast from 'react-hot-toast'
import API from '../api/axios'
import useFormValidation from '../hooks/useFormValidation'
import './ReportsPage.css'

const reportTypes = [
    'Life Journey',
    'Career Forecast',
    'Marriage Compatibility',
    'Annual Prediction',
    'Gemstone Recommendation',
    'Kundli Analysis',
]

export default function ReportsPage() {
    const {
        values,
        errors,
        isSubmitting,
        setIsSubmitting,
        handleChange,
        validate,
        resetForm,
    } = useFormValidation(
        {
            name: '',
            email: '',
            phone: '',
            reportType: '',
            dateOfBirth: '',
            birthTime: '',
            birthPlace: '',
            partnerDOB: '',
            partnerBirthTime: '',
            partnerBirthPlace: '',
            additionalInfo: '',
        },
        {
            name: { required: true, requiredMsg: 'Please enter your name' },
            email: { required: true, email: true },
            reportType: { required: true, requiredMsg: 'Please select a report type' },
            dateOfBirth: { required: true, requiredMsg: 'Please provide your date of birth' },
            birthTime: { required: true, requiredMsg: 'Please provide your birth time' },
            birthPlace: { required: true, requiredMsg: 'Please provide your birth place' },
        }
    )

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!validate()) return

        setIsSubmitting(true)
        try {
            // Prepare payload matching backend expectations
            const payload = {
                name: values.name,
                email: values.email,
                phone: values.phone,
                reportType: values.reportType,
                dateOfBirth: values.dateOfBirth,
                birthTime: values.birthTime,
                birthPlace: values.birthPlace,
                partnerDOB: values.partnerDOB || undefined,
                partnerBirthTime: values.partnerBirthTime || undefined,
                partnerBirthPlace: values.partnerBirthPlace || undefined,
                additionalInfo: values.additionalInfo,
            }

            await API.post('/reports', payload)
            toast.success('Report request submitted! You will receive it within 3-5 business days.')
            resetForm()
        } catch (err) {
            const errorMessage =
                err?.response?.data?.error ||
                err?.response?.data?.errors?.[0]?.message ||
                'Failed to submit report request. Please try again.'
            toast.error(errorMessage)
        } finally {
            setIsSubmitting(false)
        }
    }

    return (
        <div className="reports-page page-wrapper">
            <div className="page-header">
                <h1>Personalized <span className="gold-text">Life Reports</span></h1>
                <p>Request in-depth Vedic astrology reports tailored to your journey.</p>
            </div>

            <section className="section">
                <div className="container reports-container">
                    <form className="glass-card reports-form" onSubmit={handleSubmit}>
                        <h2>Your Details</h2>

                        <div className="form-row">
                            <div className="form-group">
                                <label className="form-label">Full Name *</label>
                                <input
                                    className="form-input"
                                    name="name"
                                    value={values.name}
                                    onChange={handleChange}
                                    placeholder="Enter your full name"
                                />
                                {errors.name && <p className="form-error">{errors.name}</p>}
                            </div>
                            <div className="form-group">
                                <label className="form-label">Email Address *</label>
                                <input
                                    className="form-input"
                                    name="email"
                                    type="email"
                                    value={values.email}
                                    onChange={handleChange}
                                    placeholder="your@email.com"
                                />
                                {errors.email && <p className="form-error">{errors.email}</p>}
                            </div>
                        </div>

                        <div className="form-row">
                            <div className="form-group">
                                <label className="form-label">Phone Number (optional)</label>
                                <input
                                    className="form-input"
                                    name="phone"
                                    value={values.phone}
                                    onChange={handleChange}
                                    placeholder="+91 98765 43210"
                                />
                            </div>
                            <div className="form-group">
                                <label className="form-label">Report Type *</label>
                                <select
                                    className="form-select"
                                    name="reportType"
                                    value={values.reportType}
                                    onChange={handleChange}
                                >
                                    <option value="">Choose a report...</option>
                                    {reportTypes.map(r => (
                                        <option key={r} value={r}>{r}</option>
                                    ))}
                                </select>
                                {errors.reportType && <p className="form-error">{errors.reportType}</p>}
                            </div>
                        </div>

                        <h3>Birth Details</h3>
                        <div className="form-row">
                            <div className="form-group">
                                <label className="form-label">Date of Birth *</label>
                                <input
                                    className="form-input"
                                    name="dateOfBirth"
                                    type="date"
                                    value={values.dateOfBirth}
                                    onChange={handleChange}
                                />
                                {errors.dateOfBirth && <p className="form-error">{errors.dateOfBirth}</p>}
                            </div>
                            <div className="form-group">
                                <label className="form-label">Time of Birth *</label>
                                <input
                                    className="form-input"
                                    name="birthTime"
                                    type="time"
                                    value={values.birthTime}
                                    onChange={handleChange}
                                />
                                {errors.birthTime && <p className="form-error">{errors.birthTime}</p>}
                            </div>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Place of Birth *</label>
                            <input
                                className="form-input"
                                name="birthPlace"
                                value={values.birthPlace}
                                onChange={handleChange}
                                placeholder="City, Country"
                            />
                            {errors.birthPlace && <p className="form-error">{errors.birthPlace}</p>}
                        </div>

                        <h3>Partner Details (for compatibility reports)</h3>
                        <div className="form-row">
                            <div className="form-group">
                                <label className="form-label">Partner Date of Birth</label>
                                <input
                                    className="form-input"
                                    name="partnerDOB"
                                    type="date"
                                    value={values.partnerDOB}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="form-group">
                                <label className="form-label">Partner Time of Birth</label>
                                <input
                                    className="form-input"
                                    name="partnerBirthTime"
                                    type="time"
                                    value={values.partnerBirthTime}
                                    onChange={handleChange}
                                />
                            </div>
                        </div>

                        <div className="form-group">
                            <label className="form-label">Partner Place of Birth</label>
                            <input
                                className="form-input"
                                name="partnerBirthPlace"
                                value={values.partnerBirthPlace}
                                onChange={handleChange}
                                placeholder="City, Country"
                            />
                        </div>

                        <div className="form-group">
                            <label className="form-label">Additional Information</label>
                            <textarea
                                className="form-textarea"
                                name="additionalInfo"
                                value={values.additionalInfo}
                                onChange={handleChange}
                                placeholder="Share any specific questions, focus areas, or background you'd like us to consider..."
                                rows="4"
                            />
                        </div>

                        <button
                            type="submit"
                            className="btn btn-primary reports-submit"
                            disabled={isSubmitting}
                        >
                            {isSubmitting ? 'Submitting...' : 'Request Report'}
                        </button>
                    </form>

                    <div className="reports-info">
                        <div className="glass-card info-card">
                            <h3>What you will receive</h3>
                            <ul className="reports-list">
                                <li>Detailed PDF report prepared by experienced astrologers</li>
                                <li>Practical remedies and guidance tailored to your chart</li>
                                <li>Timeline of key life events and planetary periods</li>
                                <li>Follow-up email support for report clarifications</li>
                            </ul>
                        </div>
                        <div className="glass-card info-card">
                            <h3>Delivery timeline</h3>
                            <p>Most reports are delivered within <strong>3–5 business days</strong>. Complex compatibility and life-journey reports may take up to 7 days.</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
}
