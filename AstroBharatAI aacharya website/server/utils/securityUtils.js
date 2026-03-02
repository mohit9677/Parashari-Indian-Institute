const crypto = require('crypto');

// Check if encryption key is properly set
if (!process.env.ENCRYPTION_KEY || process.env.ENCRYPTION_KEY.length !== 64) {
    console.warn('WARNING: ENCRYPTION_KEY is not set or not 32 bytes (64 hex chars). Using a fallback for development (NOT SECURE). Set a valid 32-byte hex key in .env');
}

const algorithm = 'aes-256-cbc';
// Use provided key or a fallback (ONLY for dev/test if key missing - ideally should error out in prod)
// Key must be 32 bytes.
const key = process.env.ENCRYPTION_KEY
    ? Buffer.from(process.env.ENCRYPTION_KEY, 'hex')
    : crypto.scryptSync('astro-bharat-fallback-secret', 'salt', 32);

const ivLength = 16; // For AES, this is always 16

exports.encryptToken = (text) => {
    const iv = crypto.randomBytes(ivLength);
    const cipher = crypto.createCipheriv(algorithm, key, iv);
    let encrypted = cipher.update(text);
    encrypted = Buffer.concat([encrypted, cipher.final()]);
    return iv.toString('hex') + ':' + encrypted.toString('hex');
};

exports.decryptToken = (text) => {
    const textParts = text.split(':');
    const iv = Buffer.from(textParts.shift(), 'hex');
    const encryptedText = Buffer.from(textParts.join(':'), 'hex');
    const decipher = crypto.createDecipheriv(algorithm, key, iv);
    let decrypted = decipher.update(encryptedText);
    decrypted = Buffer.concat([decrypted, decipher.final()]);
    return decrypted.toString();
};
