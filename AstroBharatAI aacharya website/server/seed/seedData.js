require('dotenv').config();
const mongoose = require('mongoose');
const Service = require('../models/Service');
const Article = require('../models/Article');

const services = [
    {
        title: 'Vedic Birth Chart Analysis',
        slug: 'vedic-birth-chart-analysis',
        description: 'Gain deep insights into your personality, strengths, and life path through a comprehensive Vedic birth chart (Kundli) analysis. Our experts interpret planetary positions, houses, and dashas to reveal patterns that shape your destiny. This detailed reading covers career tendencies, relationship dynamics, health indicators, and spiritual growth potential based on ancient Jyotish principles.',
        shortDesc: 'Comprehensive Kundli reading revealing your personality, destiny, and life patterns through Vedic astrology.',
        icon: '🔮',
        category: 'Astrology',
        price: '₹2,100',
        duration: '60 minutes',
        featured: true,
        benefits: ['Detailed planetary analysis', 'Dasha predictions', 'Remedial measures', 'Life path guidance'],
    },
    {
        title: 'Relationship & Compatibility Reading',
        slug: 'relationship-compatibility-reading',
        description: 'Discover the cosmic chemistry between you and your partner. Our compatibility analysis examines both charts to identify areas of harmony and potential challenges. We provide actionable guidance for strengthening your bond, understanding communication styles, and navigating life transitions together. Ideal for couples planning marriage or seeking to deepen their connection.',
        shortDesc: 'Explore cosmic compatibility with your partner through dual-chart analysis and relationship insights.',
        icon: '💑',
        category: 'Astrology',
        price: '₹2,500',
        duration: '75 minutes',
        featured: true,
        benefits: ['Guna Milan scoring', 'Communication insights', 'Conflict resolution guidance', 'Timing for milestones'],
    },
    {
        title: 'Career & Finance Forecast',
        slug: 'career-finance-forecast',
        description: 'Align your professional journey with cosmic timing. Our career forecast identifies favorable periods for job changes, business launches, investments, and skill development. We analyze the 10th and 2nd houses, planetary transits, and dasha periods to provide a strategic roadmap for financial growth and professional fulfillment over the coming year.',
        shortDesc: 'Strategic career and financial guidance aligned with your planetary periods and transits.',
        icon: '💼',
        category: 'Astrology',
        price: '₹1,800',
        duration: '45 minutes',
        featured: false,
        benefits: ['Optimal timing for decisions', 'Investment guidance', 'Career change analysis', 'Wealth period identification'],
    },
    {
        title: 'Numerology Life Path Reading',
        slug: 'numerology-life-path-reading',
        description: 'Unlock the hidden power of numbers in your life. Our numerology reading calculates your Life Path, Expression, Soul Urge, and Destiny numbers to reveal your core purpose, innate talents, and hidden desires. Learn how numerical vibrations influence your daily decisions, relationships, and career choices for a more aligned and purposeful life.',
        shortDesc: 'Discover your core purpose and hidden talents through personalized numerological analysis.',
        icon: '🔢',
        category: 'Numerology',
        price: '₹1,500',
        duration: '45 minutes',
        featured: true,
        benefits: ['Life Path number analysis', 'Name vibration assessment', 'Lucky numbers & colors', 'Yearly cycle predictions'],
    },
    {
        title: 'Business Name Numerology',
        slug: 'business-name-numerology',
        description: 'Choose a business name that resonates with success. Our expert numerologist evaluates potential business names against your personal numbers and industry vibrations. We suggest modifications or alternatives that align with prosperity, growth, and brand recognition, ensuring your business identity vibrates at the frequency of abundance.',
        shortDesc: 'Optimize your business name for success using numerological alignment and vibration analysis.',
        icon: '🏢',
        category: 'Numerology',
        price: '₹2,000',
        duration: '30 minutes',
        featured: false,
        benefits: ['Name vibration scoring', 'Lucky date suggestions', 'Brand color guidance', 'Growth number alignment'],
    },
    {
        title: 'Vastu Home Consultation',
        slug: 'vastu-home-consultation',
        description: 'Transform your living space into a sanctuary of positive energy. Our Vastu consultation examines your home layout, room placements, and directional alignments to identify energy blockages and recommend corrections. From furniture placement to color schemes, we provide practical Vastu-compliant solutions that promote health, harmony, and prosperity without major renovations.',
        shortDesc: 'Harmonize your home energy with practical Vastu corrections for health, wealth, and happiness.',
        icon: '🏠',
        category: 'Vastu',
        price: '₹3,000',
        duration: '90 minutes',
        featured: true,
        benefits: ['Room-by-room analysis', 'Energy flow optimization', 'Remedy suggestions', 'Prosperity zone activation'],
    },
    {
        title: 'Vastu Office & Commercial',
        slug: 'vastu-office-commercial',
        description: 'Boost productivity and profitability in your workplace through Vastu alignment. We analyze your office layout, seating arrangements, entrance placement, and directional flow to optimize the work environment. Our recommendations cover everything from conference room positioning to cash counter placement, creating a space that attracts business success.',
        shortDesc: 'Optimize office energy for productivity, team harmony, and business success with Vastu principles.',
        icon: '🏗️',
        category: 'Vastu',
        price: '₹5,000',
        duration: '120 minutes',
        featured: false,
        benefits: ['Workspace layout design', 'Wealth corner activation', 'Team harmony optimization', 'Business growth alignment'],
    },
    {
        title: 'Gemstone Recommendation',
        slug: 'gemstone-recommendation',
        description: 'Harness the healing power of gemstones tailored to your birth chart. Our gemologist-astrologer analyzes your Kundli to identify which gems can strengthen weak planets, amplify beneficial energies, and mitigate challenging periods. We provide guidance on gem quality, carat weight, metal setting, wearing rituals, and the optimal day to begin wearing your prescribed stone.',
        shortDesc: 'Personalized gemstone prescriptions based on your birth chart for planetary harmony and well-being.',
        icon: '💎',
        category: 'Gemstone',
        price: '₹1,200',
        duration: '30 minutes',
        featured: false,
        benefits: ['Chart-based prescription', 'Quality guidance', 'Wearing ritual instructions', 'Alternative stone options'],
    },
    {
        title: 'Spiritual Healing Session',
        slug: 'spiritual-healing-session',
        description: 'Experience deep spiritual cleansing and energy realignment through our guided healing sessions. Combining Vedic mantras, meditation techniques, and energy work, our practitioners help you release negative patterns, heal emotional wounds, and reconnect with your higher self. Each session is customized to address your specific challenges and spiritual goals.',
        shortDesc: 'Personalized spiritual cleansing with Vedic mantras, meditation, and energy healing techniques.',
        icon: '🙏',
        category: 'Spiritual',
        price: '₹1,800',
        duration: '60 minutes',
        featured: false,
        benefits: ['Energy cleansing', 'Mantra prescription', 'Meditation guidance', 'Chakra balancing'],
    },
    {
        title: 'Puja & Ritual Guidance',
        slug: 'puja-ritual-guidance',
        description: 'Get expert guidance on performing specific pujas and rituals to address life challenges, celebrate auspicious occasions, or seek divine blessings. Our pandit provides detailed instructions including mantras, materials needed, auspicious timing (muhurat), and step-by-step procedures for both home-based and temple rituals aligned with your horoscope.',
        shortDesc: 'Expert puja guidance with mantras, muhurat selection, and step-by-step ritual instructions.',
        icon: '🕯️',
        category: 'Spiritual',
        price: '₹1,500',
        duration: '45 minutes',
        featured: false,
        benefits: ['Muhurat selection', 'Mantra guidance', 'Material list', 'Video call support'],
    },
];

const articles = [
    {
        title: 'Understanding Your Moon Sign: The Key to Emotional Intelligence',
        slug: 'understanding-moon-sign-emotional-intelligence',
        excerpt: 'Your Moon sign reveals your emotional core — how you process feelings, what makes you feel secure, and how you nurture yourself and others.',
        content: `<h2>What is Your Moon Sign?</h2>
<p>While most people know their Sun sign, the Moon sign is equally important in Vedic astrology. It represents your emotional nature, subconscious patterns, and innermost needs. In Jyotish, the Moon sign (Rashi) is actually considered more important than the Sun sign for day-to-day predictions.</p>

<h2>How to Find Your Moon Sign</h2>
<p>Your Moon sign is determined by the position of the Moon at the exact time and place of your birth. Unlike the Sun, which stays in one sign for about 30 days, the Moon changes signs every 2.5 days, making your birth time crucial for an accurate reading.</p>

<h2>The 12 Moon Signs and Their Emotional Qualities</h2>
<p><strong>Aries Moon:</strong> Quick emotional responses, needs independence and action to feel alive.</p>
<p><strong>Taurus Moon:</strong> Seeks stability and comfort, emotionally grounded and loyal.</p>
<p><strong>Gemini Moon:</strong> Processes emotions through communication and intellectual understanding.</p>
<p><strong>Cancer Moon:</strong> Deeply intuitive and nurturing, needs emotional security above all.</p>
<p><strong>Leo Moon:</strong> Warm-hearted with a need for recognition and creative expression.</p>
<p><strong>Virgo Moon:</strong> Finds emotional balance through order, service, and practical care.</p>
<p><strong>Libra Moon:</strong> Seeks harmony in relationships, emotionally attuned to others' needs.</p>
<p><strong>Scorpio Moon:</strong> Intense and transformative emotions, values deep authentic connections.</p>
<p><strong>Sagittarius Moon:</strong> Needs freedom and adventure, optimistic emotional outlook.</p>
<p><strong>Capricorn Moon:</strong> Emotionally reserved but deeply committed, finds security in achievement.</p>
<p><strong>Aquarius Moon:</strong> Values emotional independence, processes feelings through humanitarian ideals.</p>
<p><strong>Pisces Moon:</strong> Highly empathic and imaginative, needs spiritual connection and creative outlets.</p>

<h2>Using Your Moon Sign for Growth</h2>
<p>Understanding your Moon sign helps you recognize your emotional triggers, improve relationships, and develop a self-care routine that truly nourishes you. It is the foundation of emotional intelligence in Vedic astrology.</p>`,
        category: 'Astrology',
        author: 'AstroBharat Team',
        tags: ['moon-sign', 'emotional-intelligence', 'vedic-astrology', 'rashi'],
        readTime: 6,
    },
    {
        title: 'Vastu Tips for a Harmonious Living Room',
        slug: 'vastu-tips-harmonious-living-room',
        excerpt: 'Transform your living room into a space that radiates positive energy with these proven Vastu Shastra principles for furniture, colors, and decor.',
        content: `<h2>Why Vastu Matters for Your Living Room</h2>
<p>The living room is where families gather, guests are welcomed, and social bonds are strengthened. In Vastu Shastra, it represents the social and communal energy of a household. A Vastu-compliant living room promotes harmony, open communication, and positive relationships.</p>

<h2>Direction and Placement</h2>
<p>The ideal living room is located in the north, east, or northeast direction of the home. These directions are associated with positive energy flow and prosperity.</p>

<h2>Furniture Arrangement</h2>
<p><strong>Sofa placement:</strong> The main sofa should face east or north. Avoid placing heavy furniture in the northeast corner — keep it light and open.</p>
<p><strong>TV and electronics:</strong> Place the television in the southeast corner, as this direction is governed by the fire element and aligns with electronic energy.</p>
<p><strong>Center space:</strong> Keep the center of the room (Brahmasthan) as open and clutter-free as possible to allow energy to circulate freely.</p>

<h2>Colors and Decor</h2>
<p>Opt for warm, welcoming colors like light yellow, cream, beige, or soft green. Avoid dark or aggressive colors on the walls. Art and decor should depict positive themes — nature scenes, family harmony, or spiritual symbols work well.</p>

<h2>Lighting</h2>
<p>Natural light is essential. Ensure windows in the north and east are unobstructed. For artificial lighting, use warm tones and avoid harsh fluorescent lights. A well-lit living room energizes the space and uplifts the mood of its occupants.</p>`,
        category: 'Vastu',
        author: 'AstroBharat Team',
        tags: ['vastu', 'living-room', 'home-decor', 'positive-energy'],
        readTime: 5,
    },
    {
        title: 'The Power of Life Path Numbers in Numerology',
        slug: 'power-life-path-numbers-numerology',
        excerpt: 'Your Life Path number is the single most important number in numerology — learn how to calculate it and what it reveals about your destiny.',
        content: `<h2>What is a Life Path Number?</h2>
<p>In numerology, your Life Path number is derived from your full date of birth and represents the journey you are destined to walk in this lifetime. It reveals your natural abilities, challenges, and the overarching theme of your life purpose.</p>

<h2>How to Calculate Your Life Path Number</h2>
<p>Add all the digits of your birth date until you get a single digit (or a Master Number: 11, 22, or 33).</p>
<p><strong>Example:</strong> If born on March 15, 1990 → 3 + 1 + 5 + 1 + 9 + 9 + 0 = 28 → 2 + 8 = 10 → 1 + 0 = <strong>1</strong></p>

<h2>Life Path Number Meanings</h2>
<p><strong>1 — The Leader:</strong> Independent, ambitious, and pioneering. You are meant to forge new paths and lead with confidence.</p>
<p><strong>2 — The Peacemaker:</strong> Diplomatic, sensitive, and cooperative. Your purpose involves creating harmony and partnerships.</p>
<p><strong>3 — The Communicator:</strong> Creative, expressive, and joyful. You light up the world through art, writing, or speaking.</p>
<p><strong>4 — The Builder:</strong> Disciplined, reliable, and hardworking. You create lasting foundations in work and life.</p>
<p><strong>5 — The Adventurer:</strong> Freedom-seeking, versatile, and curious. Your path involves embracing change and diverse experiences.</p>
<p><strong>6 — The Nurturer:</strong> Caring, responsible, and family-oriented. You find fulfillment in service and domestic harmony.</p>
<p><strong>7 — The Seeker:</strong> Introspective, analytical, and spiritual. Your journey is one of inner exploration and wisdom.</p>
<p><strong>8 — The Achiever:</strong> Powerful, goal-oriented, and business-savvy. Material success and authority are natural to you.</p>
<p><strong>9 — The Humanitarian:</strong> Compassionate, idealistic, and generous. You are here to serve the greater good.</p>

<h2>Master Numbers</h2>
<p>If your calculation yields 11, 22, or 33, you carry a Master Number with intensified spiritual significance and potential.</p>`,
        category: 'Numerology',
        author: 'AstroBharat Team',
        tags: ['numerology', 'life-path', 'destiny', 'self-discovery'],
        readTime: 7,
    },
    {
        title: 'Choosing the Right Gemstone Based on Your Birth Chart',
        slug: 'choosing-right-gemstone-birth-chart',
        excerpt: 'Not every gemstone suits everyone. Learn the Vedic principles for selecting a gemstone that aligns with your planetary strengths and challenges.',
        content: `<h2>Gemstones in Vedic Astrology</h2>
<p>In Jyotish Shastra, gemstones are prescribed as remedial measures (upayas) to strengthen weak but beneficial planets in your birth chart. Each of the nine planets (Navagraha) has a corresponding gemstone that channels its energy.</p>

<h2>The Nine Planetary Gemstones</h2>
<p><strong>Sun → Ruby (Manik):</strong> Enhances leadership, vitality, and self-confidence.</p>
<p><strong>Moon → Pearl (Moti):</strong> Promotes emotional stability, intuition, and mental peace.</p>
<p><strong>Mars → Red Coral (Moonga):</strong> Boosts courage, energy, and physical strength.</p>
<p><strong>Mercury → Emerald (Panna):</strong> Sharpens intellect, communication, and business acumen.</p>
<p><strong>Jupiter → Yellow Sapphire (Pukhraj):</strong> Attracts wisdom, prosperity, and spiritual growth.</p>
<p><strong>Venus → Diamond (Heera):</strong> Enhances love, creativity, and material comforts.</p>
<p><strong>Saturn → Blue Sapphire (Neelam):</strong> Provides discipline, protection, and karmic alignment.</p>
<p><strong>Rahu → Hessonite (Gomed):</strong> Protects from illusion and enhances unconventional success.</p>
<p><strong>Ketu → Cat's Eye (Lehsunia):</strong> Supports spiritual liberation and protection from hidden enemies.</p>

<h2>Important Guidelines</h2>
<p>Never wear a gemstone without consulting a qualified astrologer. The wrong stone can amplify negative planetary influences. Quality, weight, and the wearing ritual all matter significantly for the gem to be effective.</p>`,
        category: 'Gemstone',
        author: 'AstroBharat Team',
        tags: ['gemstones', 'vedic-remedies', 'navagraha', 'healing-stones'],
        readTime: 5,
    },
    {
        title: '5 Daily Spiritual Practices for Inner Peace',
        slug: 'daily-spiritual-practices-inner-peace',
        excerpt: 'Discover five simple yet powerful spiritual practices rooted in Vedic tradition that can transform your daily routine and bring lasting tranquility.',
        content: `<h2>Building a Daily Spiritual Routine</h2>
<p>In our fast-paced modern life, taking time for spiritual practice is not a luxury — it is a necessity for mental, emotional, and spiritual well-being. These five practices, rooted in ancient Vedic wisdom, can be adapted to any lifestyle.</p>

<h2>1. Morning Meditation (Dhyana)</h2>
<p>Begin your day with 10-15 minutes of silent meditation. Sit comfortably, close your eyes, and focus on your breath. This simple practice reduces stress, improves focus, and connects you with your inner stillness.</p>

<h2>2. Mantra Chanting (Japa)</h2>
<p>Select a mantra that resonates with you — whether it is the universal "Om," the Gayatri Mantra, or a planetary mantra prescribed for your chart. Chanting 108 times (one mala) creates a powerful vibrational shift in your consciousness.</p>

<h2>3. Gratitude Journaling</h2>
<p>Each evening, write down three things you are grateful for. This practice shifts your focus from scarcity to abundance, aligning your mind with the prosperous energy of Jupiter.</p>

<h2>4. Pranayama (Breathing Exercises)</h2>
<p>Practice Anulom-Vilom (alternate nostril breathing) for 5-10 minutes daily. This balances the solar and lunar energies in your body, calms the nervous system, and enhances mental clarity.</p>

<h2>5. Evening Lamp Lighting (Sandhya Deepam)</h2>
<p>Light a ghee or sesame oil lamp at dusk in your home. This ancient practice dispels negative energy, brings auspiciousness, and creates a sacred atmosphere for the evening hours.</p>`,
        category: 'Spiritual',
        author: 'AstroBharat Team',
        tags: ['spirituality', 'meditation', 'vedic-practices', 'inner-peace'],
        readTime: 4,
    },
    {
        title: 'How Planetary Transits Affect Your Daily Life',
        slug: 'planetary-transits-affect-daily-life',
        excerpt: 'Understand how the movement of planets through the zodiac creates waves of energy that influence your mood, decisions, and life events.',
        content: `<h2>What Are Planetary Transits?</h2>
<p>Planetary transits (Gochar) refer to the real-time movement of planets through the zodiac signs. While your birth chart remains fixed, these ongoing planetary movements create dynamic interactions with your natal planets, triggering events and shifting energies in different areas of your life.</p>

<h2>Fast vs. Slow Transits</h2>
<p><strong>Fast planets (Moon, Mercury, Venus, Sun):</strong> These change signs frequently and affect your day-to-day mood, communication style, and social interactions.</p>
<p><strong>Slow planets (Jupiter, Saturn, Rahu, Ketu):</strong> These stay in one sign for months or years and bring major life themes — career changes, relationship shifts, spiritual awakenings.</p>

<h2>Key Transits to Watch</h2>
<p><strong>Saturn Transit (Sade Sati):</strong> The most discussed transit in Vedic astrology, occurring when Saturn transits through the 12th, 1st, and 2nd houses from your Moon sign. It lasts approximately 7.5 years and brings karmic lessons and maturation.</p>
<p><strong>Jupiter Transit:</strong> Jupiter changes signs roughly every year and brings growth, opportunities, and expansion wherever it transits in your chart.</p>
<p><strong>Rahu-Ketu Transit:</strong> These shadow planets change signs every 18 months and often bring unexpected changes, karmic encounters, and spiritual turning points.</p>

<h2>How to Work With Transits</h2>
<p>Rather than fearing difficult transits, use them as opportunities for growth. Regular consultation with an astrologer helps you anticipate upcoming energies and make informed decisions aligned with cosmic timing.</p>`,
        category: 'Astrology',
        author: 'AstroBharat Team',
        tags: ['transits', 'gochar', 'planetary-movement', 'vedic-astrology'],
        readTime: 6,
    },
];

const seedDB = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI);
        console.log('Connected to MongoDB');

        // Clear existing
        await Service.deleteMany({});
        await Article.deleteMany({});

        // Seed
        await Service.insertMany(services);
        console.log(`✅ ${services.length} services seeded`);

        await Article.insertMany(articles);
        console.log(`✅ ${articles.length} articles seeded`);

        console.log('🌱 Seed complete!');
        process.exit(0);
    } catch (err) {
        console.error('❌ Seed error:', err);
        process.exit(1);
    }
};

seedDB();
