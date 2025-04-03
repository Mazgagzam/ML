import string
import sys

STOP_WORDS = {
    "the", "have", "he", "she", "it", "on", "to", "i", "was", "not", "or", "and", "will", "are", "your",
    "you", "we", "how", "our", "what", "as", "be", "a", "my", "an", "in", "at", "of", "for", "is", "this",
    "that", "with", "by", "from", "where", "its", "all", "their", "them", "these", "there", "so", "if",
    "can", "one", "some", "just", "any", "many", "also", "but", "such", "when", "do", "does", "did", "has",
    "about", "into", "over", "up", "down", "out", "why", "because", "only", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "don't", "dont", "didnt", "did'nt", "to", "had"
}

def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    tokens = [token for token in tokens if token not in STOP_WORDS]  # Remove stop words
    return tokens

def predict_tag(text, tag_keywords):
    tag_scores = {tag: 0 for tag in tag_keywords}
    tokens = tokenize(text)

    for token in tokens:
        for tag, keywords in tag_keywords.items():
            if token in keywords:
                tag_scores[tag] += 1
    best_tag = max(tag_scores, key=tag_scores.get)
    return best_tag

input_data = sys.stdin.read()
lines = input_data.splitlines()
input_texts = []
for line in lines:
    input_texts.append(line.lower())

tag_keywords = {'ai': ['ai', 'chatbot', 'artificial', 'bots', 'tech', 'business', 'may', 'future', 'technology', 'robot'], 'android': ['android', 'app', 'download', 'apk', 'google', 'apps', 'mobile', 'hack', 'kotlin', 'game'], 'apple': ['iphone', 'apple', 'macbook', 'ios', 'repair', 'phone', 'x', 'ipad', 'app', 'get'], 'architecture': ['architecture', 'home', 'design', 'roof', 'building', 'construction', 'architects', 'house', 'best', 'architectural'], 'art': ['art', 'painting', 'artist', 'people', 'artists', 'work', 'world', 'paintings', 'paint', 'make'], 'artificial-intelligence': ['ai', 'intelligence', 'artificial', 'technology', 'future', 'human', 'google', 'voice', 'world', 'machine'], 'big-data': ['big', 'analytics', 'business', 'using', 'world', 'cloud', 'analysis', 'every', 'apache', 'large'], 'bitcoin': ['bitcoin', 'blockchain', 'crypto', 'cryptocurrency', 'cryptocurrencies', 'market', 'ico', 'trading', 'technology', 'digital'], 'blacklivesmatter': ['black', 'white', 'people', 'police', 'history', 'world', 'shirt', 'america', 'american', 'many'], 'blockchain': ['blockchain', 'token', 'ico', 'community', 'team', 'technology', 'platform', 'sale', 'crypto', 'tokens'], 'blog': ['blog', 'world', 'protein', 'back', 'people', 'life', 'much', 'need', 'best', 'today'], 'blogging': ['blog', 'blogging', 'money', 'content', 'marketing', 'writing', 'blogs', 'start', 'business', 'want'], 'books': ['books', 'book', 'read', 'reading', 'pdf', 'review', 'https', 'tinyurl', 'year', 'best'], 'branding': ['brand', 'branding', 'business', 'logo', 'marketing', 'brands', 'company', 'identity', 'design', 'people'], 'business': ['business', 'company', 'need', 'many', 'people', 'services', 'businesses', 'make', 'best', 'online'], 'college': ['college', 'students', 'school', 'student', 'university', 'life', 'year', 'many', 'get', 'high'], 'computer-science': ['computer', 'science', 'ugc', 'world', 'university', 'computing', 'system', 'cyber', 'lambda', 'chandigarh'], 'creativity': ['creativity', 'creative', 'writing', 'life', 'ideas', 'people', 'write', 'want', 'get', 'work'], 'cryptocurrency': ['crypto', 'blockchain', 'ico', 'cryptocurrency', 'bitcoin', 'token', 'platform', 'team', 'cryptocurrencies', 'world'], 'culture': ['culture', 'world', 'people', 'life', 'many', 'cultural', 'part', 'american', 'love', 'story'], 'data': ['business', 'gdpr', 'information', 'protection', 'privacy', 'blockchain', 'big', 'technology', 'using', 'us'], 'data-science': ['science', 'analysis', 'project', 'analytics', 'scientist', 'using', 'post', 'work', 'world', 'model'], 'data-visualization': ['visualization', 'chart', 'chapter', 'week', 'many', 'best', 'information', 'analytics', 'analysis', 'd3'], 'deep-learning': ['learning', 'deep', 'neural', 'gpu', 'tensorflow', 'networks', 'docker', 'started', 'ai', 'bullying'], 'design': ['design', 'best', 'designer', 'week', 'work', 'app', 'designers', 'make', 'home', 'designing'], 'dogs': ['dog', 'dogs', 'pet', 'best', 'pets', 'life', 'training', 'love', 'animals', 'puppy'], 'donald-trump': ['trump', 'donald', 'president', 'people', 'trumps', 'us', 'news', 'american', 'said', 'russia'], 'economics': ['economic', 'economy', 'market', 'us', 'economics', 'income', 'world', 'markets', 'financial', 'india'], 'education': ['school', 'students', 'education', 'learning', 'year', 'schools', 'best', 'online', 'exam', 'college'], 'energy': ['energy', 'power', 'market', 'solar', 'electricity', 'heating', 'oil', 'home', 'system', 'renewable'], 'entrepreneurship': ['business', 'people', 'life', 'start', 'startup', 'entrepreneur', 'company', 'entrepreneurship', 'work', 'entrepreneurs'], 'environment': ['plastic', 'waste', 'environment', 'environmental', 'people', 'world', 'water', 'climate', 'pollution', 'change'], 'ethereum': ['blockchain', 'ethereum', 'token', 'crypto', 'smart', 'ico', 'cryptocurrency', 'platform', 'bitcoin', 'tokens'], 'feminism': ['women', 'men', 'feminism', 'feminist', 'people', 'sexual', 'gender', 'metoo', 'harassment', 'womens'], 'fiction': ['story', 'would', 'chapter', 'could', 'part', 'back', 'life', 'every', 'man', 'always'], 'food': ['food', 'best', 'restaurant', 'people', 'eat', 'many', 'make', 'indian', 'get', 'restaurants'], 'football': ['football', 'world', 'cup', 'nfl', 'league', 'week', 'team', 'season', 'game', 'top'], 'google': ['google', 'search', 'business', 'seo', 'googles', 'website', 'marketing', 'make', 'top', 'service'], 'government': ['government', 'digital', 'state', 'public', 'many', 'people', 'year', 'news', 'week', 'service'], 'happiness': ['happiness', 'life', 'happy', 'people', 'things', 'world', 'success', 'want', 'make', 'feel'], 'health': ['health', 'people', 'body', 'life', 'pain', 'healthy', 'weight', 'many', 'best', 'get'], 'history': ['history', 'years', 'world', 'people', 'historical', 'war', 'john', 'story', 'life', 'us'], 'humor': ['people', 'get', 'make', 'life', 'best', 'years', 'way', 'things', 'good', 'many'], 'inspiration': ['life', 'people', 'get', 'love', 'today', 'world', 'go', 'year', 'would', 'things'], 'investing': ['investing', 'investment', 'market', 'financial', 'money', 'invest', 'stock', 'people', 'trading', 'funds'], 'ios': ['ios', 'app', 'swift', 'apple', 'development', 'apps', 'code', 'using', 'mobile', 'game'], 'javascript': ['javascript', 'js', 'using', 'angular', 'web', 'code', 'node', 'post', 'react', 'get'], 'jobs': ['job', 'jobs', 'interview', 'career', 'get', 'people', 'work', 'many', 'make', 'looking'], 'journalism': ['news', 'media', 'journalism', 'social', 'journalists', 'fake', 'journalist', 'local', 'many', 'world'], 'leadership': ['leadership', 'leaders', 'leader', 'people', 'business', 'team', 'work', 'change', 'great', 'things'], 'life': ['life', 'people', 'things', 'get', 'never', 'good', 'something', 'want', 'make', 'think'], 'life-lessons': ['life', 'people', 'things', 'thing', 'think', 'years', 'always', 'get', 'really', 'year'], 'love': ['love', 'life', 'people', 'always', 'never', 'many', 'would', 'heart', 'want', 'things'], 'machine-learning': ['learning', 'machine', 'using', 'ai', 'model', 'neural', 'ml', 'deep', 'us', 'post'], 'marketing': ['marketing', 'business', 'advertising', 'sales', 'brand', 'best', 'customer', 'media', 'social', 'customers'], 'medium': ['medium', 'blog', 'read', 'publications', 'story', 'post', 'get', 'posts', 'writing', 'stories'], 'mobile': ['mobile', 'phone', 'app', 'apps', 'cell', 'phones', 'market', 'way', 'devices', 'smartphones'], 'motivation': ['life', 'motivation', 'get', 'self', 'things', 'year', 'people', 'success', 'work', 'good'], 'movies': ['movie', 'film', 'movies', 'review', 'watch', 'films', 'year', 'best', 'online', 'full'], 'music': ['music', 'song', 'album', 'best', 'people', 'songs', 'live', 'year', 'get', 'world'], 'nba': ['nba', 'coins', 'game', 'season', 'live', 'lebron', 'three', 'team', 'players', 'draft'], 'news': ['news', 'year', 'bar', 'people', 'cryptocurrency', 'crypto', 'years', 'resolutions', 'us', 'world'], 'nutrition': ['food', 'health', 'nutrition', 'weight', 'diet', 'healthy', 'benefits', 'body', 'people', 'many'], 'parenting': ['baby', 'child', 'kids', 'children', 'parents', 'life', 'need', 'parenting', 'parent', 'best'], 'personal-development': ['life', 'people', 'things', 'want', 'personal', 'get', 'year', 'years', 'make', 'going'], 'photography': ['photography', 'wedding', 'photo', 'camera', 'photographer', 'best', 'photos', 'photographers', 'get', 'make'], 'poem': ['poem', 'love', 'life', 'world', 'every', 'words', 'could', 'poetry', 'want', 'heart'], 'poetry': ['love', 'life', 'see', 'heart', 'way', 'eyes', 'feel', 'poem', 'words', 'every'], 'politics': ['people', 'political', 'trump', 'us', 'years', 'election', 'state', 'president', 'politics', 'may'], 'product-design': ['product', 'design', 'ux', 'products', 'make', 'great', 'managers', 'team', 'research', 'customer'], 'productivity': ['work', 'life', 'things', 'get', 'productivity', 'year', 'people', 'make', 'every', 'business'], 'programming': ['programming', 'code', 'c', 'java', 'language', 'learning', 'part', 'using', 'software', 'go'], 'psychology': ['people', 'life', 'us', 'many', 'world', 'things', 'something', 'make', 'good', 'psychology'], 'python': ['python', 'using', 'django', 'web', 'project', 'many', 'used', 'code', 'learning', 'started'], 'racism': ['white', 'people', 'black', 'racism', 'race', 'american', 'racist', 'many', 'us', 'years'], 'react': ['react', 'redux', 'app', 'native', 'using', 'graphql', 'development', 'components', 'ui', 'create'], 'relationships': ['love', 'relationship', 'life', 'relationships', 'people', 'get', 'someone', 'things', 'us', 'marriage'], 'science': ['science', 'world', 'research', 'space', 'scientists', 'life', 'years', 'earth', 'part', 'light'], 'self-improvement': ['life', 'self', 'people', 'get', 'something', 'feel', 'year', 'positive', 'mind', 'things'], 'social-media': ['social', 'media', 'facebook', 'instagram', 'marketing', 'business', 'twitter', 'people', 'online', 'world'], 'software-engineering': ['software', 'development', 'code', 'engineering', 'work', 'engineer', 'technology', 'part', 'developers', 'company'], 'sports': ['sports', 'game', 'week', 'season', 'football', 'team', 'year', 'vs', 'last', 'live'], 'startup': ['startup', 'business', 'company', 'team', 'people', 'product', 'startups', 'make', 'things', 'companies'], 'tech': ['support', 'number', 'tech', 'phone', 'technology', 'service', 'people', 'best', 'computer', 'get'], 'technology': ['technology', 'people', 'world', 'repair', 'service', 'tech', 'printer', 'future', 'phone', 'best'], 'travel': ['travel', 'best', 'city', 'trip', 'india', 'world', 'visit', 'get', 'car', 'places'], 'trump': ['trump', 'president', 'trumps', 'us', 'donald', 'american', 'people', 'north', 'america', 'right'], 'ux': ['design', 'ux', 'user', 'experience', 'app', 'project', 'research', 'product', 'mobile', 'users'], 'venture-capital': ['venture', 'capital', 'investment', 'startup', 'vc', 'fund', 'business', 'company', 'investors', 'team'], 'web-design': ['web', 'design', 'website', 'business', 'company', 'designing', 'services', 'best', 'websites', 'online'], 'web-development': ['web', 'website', 'development', 'business', 'company', 'design', 'best', 'services', 'developer', 'online'], 'women': ['women', 'womens', 'woman', 'life', 'gender', 'many', 'years', 'men', 'world', 'hair'], 'wordpress': ['wordpress', 'website', 'woocommerce', 'best', 'plugins', 'site', 'plugin', 'themes', 'content', 'web'], 'work': ['work', 'life', 'job', 'people', 'good', 'workplace', 'working', 'way', 'make', 'year'], 'writing': ['writing', 'write', 'writer', 'writers', 'story', 'something', 'every', 'many', 'things', 'good']}

print(", ".join(predict_tag(i, tag_keywords) for i in input_texts))
