const router = require('express').Router();
const { getAllArticles, getArticleBySlug } = require('../controllers/articleController');

// GET /api/articles — List (with pagination + category filter)
router.get('/', getAllArticles);

// GET /api/articles/:slug — Full article
router.get('/:slug', getArticleBySlug);

module.exports = router;
