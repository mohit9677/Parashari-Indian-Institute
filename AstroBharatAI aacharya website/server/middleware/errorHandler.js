const errorHandler = (err, req, res, next) => {
    console.error('❌ Error:', err.message);

    if (process.env.NODE_ENV === 'development') {
        console.error(err.stack);
    }

    // Mongoose validation error
    if (err.name === 'ValidationError') {
        const messages = Object.values(err.errors).map(e => e.message);
        return res.status(400).json({ success: false, error: messages.join(', ') });
    }

    // Mongoose duplicate key
    if (err.code === 11000) {
        return res.status(400).json({ success: false, error: 'Duplicate entry found.' });
    }

    // Mongoose cast error (bad ObjectId)
    if (err.name === 'CastError') {
        return res.status(400).json({ success: false, error: 'Invalid ID format.' });
    }

    res.status(err.statusCode || 500).json({
        success: false,
        error: err.message || 'Internal Server Error',
    });
};

module.exports = errorHandler;
