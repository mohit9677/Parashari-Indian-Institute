const mongoose = require('mongoose');

const reportSchema = new mongoose.Schema({
    name: { type: String, required: true, trim: true },
    email: { type: String, required: true, lowercase: true, trim: true },
    phone: { type: String, trim: true },
    reportType: {
        type: String,
        required: true,
        enum: ['Life Journey', 'Career Forecast', 'Marriage Compatibility', 'Annual Prediction', 'Gemstone Recommendation', 'Kundli Analysis'],
    },
    dateOfBirth: { type: Date, required: true },
    birthTime: { type: String, required: true },
    birthPlace: { type: String, required: true },
    partnerDOB: { type: Date },    // For compatibility reports
    partnerBirthTime: { type: String },
    partnerBirthPlace: { type: String },
    additionalInfo: { type: String, default: '' },
    status: {
        type: String,
        enum: ['requested', 'processing', 'completed', 'delivered'],
        default: 'requested',
    },
}, { timestamps: true });

reportSchema.index({ status: 1 });

module.exports = mongoose.model('Report', reportSchema);
