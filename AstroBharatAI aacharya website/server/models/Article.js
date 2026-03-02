const mongoose = require('mongoose');

const articleSchema = new mongoose.Schema({
    title: { type: String, required: true, trim: true },
    slug: { type: String, required: true, unique: true, lowercase: true },
    excerpt: { type: String, required: true, maxlength: 300 },
    content: { type: String, required: true },
    category: {
        type: String,
        required: true,
        enum: ['Astrology', 'Numerology', 'Vastu', 'Gemstone', 'Spiritual', 'Lifestyle'],
    },
    author: { type: String, default: 'AstroBharat Team' },
    coverImage: { type: String, default: '' },
    tags: [String],
    published: { type: Boolean, default: true },
    readTime: { type: Number, default: 5 }, // minutes
    views: { type: Number, default: 0 },
}, { timestamps: true });

articleSchema.index({ category: 1 });
articleSchema.index({ published: 1, createdAt: -1 });

module.exports = mongoose.model('Article', articleSchema);
