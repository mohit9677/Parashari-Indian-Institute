const fs = require('fs');
const html = fs.readFileSync('courses.html', 'utf8');

const categories = {};
const regex = /data-category=\"(.*?)\"[^>]*>[\s\S]*?<img src=\"(.*?)\"[^>]*alt=\"(.*?)\"[^>]*>[\s\S]*?<div class=\"card-header-icon\">(.*?)<\/div>[\s\S]*?<h3 class=\"card-title\">(.*?)<\/h3>[\s\S]*?<a href=\"(.*?)\"/g;

let match;
while ((match = regex.exec(html)) !== null) {
  const cat = match[1];
  if (!categories[cat]) categories[cat] = [];
  categories[cat].push({
    image: match[2],
    alt: match[3],
    icon: match[4],
    title: match[5].trim(),
    url: match[6]
  });
}

fs.writeFileSync('categories.json', JSON.stringify(categories, null, 2));
