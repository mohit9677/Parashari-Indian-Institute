const router = require('express').Router();
const { body } = require('express-validator');
const validate = require('../middleware/validate');
const { createReport } = require('../controllers/reportController');

const reportValidation = [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('reportType').trim().notEmpty().withMessage('Report type is required'),
    body('dateOfBirth').isISO8601().withMessage('Valid date of birth is required'),
    body('birthTime').trim().notEmpty().withMessage('Birth time is required'),
    body('birthPlace').trim().notEmpty().withMessage('Birth place is required'),
];

// POST /api/reports — Request a report
router.post('/', reportValidation, validate, createReport);

module.exports = router;
