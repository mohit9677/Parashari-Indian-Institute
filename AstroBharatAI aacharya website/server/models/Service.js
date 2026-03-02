const mongoose = require('mongoose');

const serviceSchema = new mongoose.Schema({
    title: { type: String, required: true, trim: true },
    slug: { type: String, required: true, unique: true, lowercase: true },
    description: { type: String, required: true },
    shortDesc: { type: String, required: true, maxlength: 160 },
    icon: { type: String, default: '✨' },
    category: {
        type: String,
        required: true,
        enum: ['Astrology', 'Numerology', 'Vastu', 'Gemstone', 'Spiritual', 'Other'],
    },
    price: { type: String, default: 'Contact for pricing' },
    duration: { type: String, default: '45-60 minutes' },
    featured: { type: Boolean, default: false },
    benefits: [String],
    isActive: { type: Boolean, default: true },
}, { timestamps: true });

serviceSchema.index({ category: 1 });
serviceSchema.index({ featured: 1 });

module.exports = mongoose.model('Service', serviceSchema);
