const Service = require('../models/Service');

// @desc    List all active services
// @route   GET /api/services
// @access  Public
exports.getAllServices = async (req, res, next) => {
    try {
        const filter = { isActive: true };
        if (req.query.category && req.query.category !== 'All') {
            filter.category = req.query.category;
        }
        const services = await Service.find(filter).sort({ featured: -1, createdAt: -1 });
        res.json({ success: true, count: services.length, data: services });
    } catch (err) {
        next(err);
    }
};

// @desc    Get single service by slug
// @route   GET /api/services/:slug
// @access  Public
exports.getServiceBySlug = async (req, res, next) => {
    try {
        const service = await Service.findOne({ slug: req.params.slug, isActive: true });
        if (!service) return res.status(404).json({ success: false, error: 'Service not found' });
        res.json({ success: true, data: service });
    } catch (err) {
        next(err);
    }
};
