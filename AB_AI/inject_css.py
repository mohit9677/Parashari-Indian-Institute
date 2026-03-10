import codecs

css_to_add = """
/* --- HIGHLIGHTS GRID (Uniform Card Grid) --- */
.highlights-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    padding: 2rem 0;
}

.highlights-card {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    height: 380px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.highlights-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(212, 175, 55, 0.25);
}

.highlights-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center top;
    display: block;
    border-radius: 12px;
    transition: transform 0.5s ease, filter 0.5s ease;
}

.highlights-card:hover img {
    transform: scale(1.05);
    filter: brightness(0.4) saturate(0.5);
}

.highlights-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 2rem;
    background: linear-gradient(transparent, rgba(0, 0, 0, 0.95));
    color: #ffffff;
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: 2;
}

.highlights-overlay h4 {
    color: #D4AF37;
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
}

.highlights-overlay p {
    color: #ffffff;
    font-size: 0.9rem;
    line-height: 1.5;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
}

/* Force overlay visible constantly for 'stand out' cards */
.highlights-card .highlights-overlay {
    opacity: 1; 
}

@media (max-width: 900px) {
    .highlights-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {
    .highlights-grid {
        grid-template-columns: 1fr;
    }
    .highlights-card {
        height: 320px;
    }
}
"""

with codecs.open(r'D:\ParashariTeam\AB_AI\assets\css\main.css', 'a', 'utf-8') as f:
    f.write(css_to_add)

print("CSS appended successfully.")
