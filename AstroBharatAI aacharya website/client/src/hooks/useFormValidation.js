import { useState } from 'react'

export default function useFormValidation(initialState, validationRules) {
    const [values, setValues] = useState(initialState)
    const [errors, setErrors] = useState({})
    const [isSubmitting, setIsSubmitting] = useState(false)

    const handleChange = (e) => {
        const { name, value } = e.target
        setValues(prev => ({ ...prev, [name]: value }))
        if (errors[name]) {
            setErrors(prev => ({ ...prev, [name]: '' }))
        }
    }

    const validate = () => {
        const newErrors = {}
        for (const [field, rules] of Object.entries(validationRules)) {
            const value = values[field]
            if (rules.required && (!value || !value.toString().trim())) {
                newErrors[field] = rules.requiredMsg || `${field} is required`
            } else if (rules.email && value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
                newErrors[field] = 'Please enter a valid email'
            } else if (rules.minLength && value && value.length < rules.minLength) {
                newErrors[field] = `Minimum ${rules.minLength} characters required`
            } else if (rules.phone && value && !/^[+]?[\d\s()-]{10,15}$/.test(value)) {
                newErrors[field] = 'Please enter a valid phone number'
            }
        }
        setErrors(newErrors)
        return Object.keys(newErrors).length === 0
    }

    const resetForm = () => {
        setValues(initialState)
        setErrors({})
    }

    return { values, errors, isSubmitting, setIsSubmitting, handleChange, validate, resetForm, setValues }
}
