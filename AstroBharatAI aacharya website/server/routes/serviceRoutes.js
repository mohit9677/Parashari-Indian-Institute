const router = require('express').Router();
const { getAllServices, getServiceBySlug } = require('../controllers/serviceController');

// GET /api/services — List all active services (optional ?category= filter)
router.get('/', getAllServices);

// GET /api/services/:slug — Get single service
router.get('/:slug', getServiceBySlug);

module.exports = router;
