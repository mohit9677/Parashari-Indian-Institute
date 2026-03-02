const jwt = require('jsonwebtoken');
const User = require('../models/User');
const { decryptToken } = require('../utils/securityUtils');

exports.protect = async (req, res, next) => {
    let token;

    if (
        req.headers.authorization &&
        req.headers.authorization.startsWith('Bearer')
    ) {
        // Set token from Bearer token in header
        token = req.headers.authorization.split(' ')[1];
    }
    // else if (req.cookies.token) {
    //     // Set token from cookie
    //     token = req.cookies.token;
    // }

    // Make sure token exists
    if (!token) {
        return res.status(401).json({ success: false, error: 'Not authorized to access this route' });
    }

    try {
        // Decrypt token
        const decryptedToken = decryptToken(token);

        // Verify token
        const decoded = jwt.verify(decryptedToken, process.env.JWT_SECRET);

        req.user = await User.findById(decoded.id);

        next();
    } catch (err) {
        console.error('Auth middleware error:', err);
        return res.status(401).json({ success: false, error: 'Not authorized to access this route' });
    }
};
