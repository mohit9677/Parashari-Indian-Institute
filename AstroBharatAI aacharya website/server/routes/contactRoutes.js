const router = require('express').Router();
const { body } = require('express-validator');
const validate = require('../middleware/validate');
const { submitContactForm } = require('../controllers/contactController');

const contactValidation = [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('subject').trim().notEmpty().withMessage('Subject is required'),
    body('message').trim().isLength({ min: 10 }).withMessage('Message must be at least 10 characters'),
];

// POST /api/contact — Submit contact form
router.post('/', contactValidation, validate, submitContactForm);

module.exports = router;
