import nltk
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hello|hi|hey|hihi|owo|hewo|helo', ['Hello! Welcome to Qatar Expo 2023. How can I assist you?']),
    (r'where is the event|location of the expo|where is it located', [
        'The Expo 2023 will take place in Doha, Qatar. It\'s located on the west side of Doha city, about 2.5 kilometers from West Bay, 3.5 kilometers from Doha Port, and around 12 kilometers from Hamad International Airport.']),
    (
        r'when does the expo start|when does it end|dates of the event|when is it happening|when will the event take place|when will it take place|datesheet',
        [
            'The Expo 2023 in Doha will start on October 2, 2023, and conclude on March 28, 2024. It\'s a six-month event showcasing horticulture and sustainable development.']),
    (r'what is the theme of the expo|expo theme', [
        'The chosen theme for Doha Expo 2023 is \'Green Desert, Better Environment.\' The event aims to inspire innovative solutions for mitigating desertification and promoting a sustainable future.']),
    (r'what can I expect|what will I see|attractions of the expo', [
        'At the Expo 2023, you\'ll experience innovation, sustainability, culture, and entertainment. The event features ornamental gardens, panel discussions, conferences, live shows, art performances, and culinary experiences. It spans an impressive 1.7 million square meters in Al Bidda Park, offering breathtaking views of the Arabian Gulf.']),
    (r'who is organizing the event|organizers of the expo', [
        'Doha Expo 2023 is happening with the support of Qatar\'s Prime Minister, HE Sheikh Mohammed bin Abdulrahman bin Jassim Al Thani, and it\'s led by the Ministry of Municipality.']),
    (r'how do I get there|how can I visit|visitor information', [
        'The Expo is conveniently located in the heart of Doha, with easy access to Hamad International Airport, Doha Port, and the Business Centre. It\'s expected to attract international visitors, organizers, representatives from various sectors, and the general public.']),
    (r'tell me more|more about the expo|website', [
        'For more detailed information about Doha Expo 2023, you can visit the official website: www.dohaexpo2023.gov.qa.']),
    (r'who is hosting the expo|host country',
     ['The International Horticultural Expo 2023 will be hosted by the State of Qatar.']),
    (r'where is Al Bidda Park|expo venue', [
        'Al Bidda Park is the scenic venue for the Expo 2023. It\'s located in Doha, with breathtaking views of the Arabian Gulf.']),
    (r'Qatar Expo 2023 schedule|event timeline',
     ['The Expo spans from October 2023 to March 2024, offering an extensive 179-day program.']),
    (r'participation countries|how many countries',
     ['Participation is confirmed from 57 countries, with more expected to join.']),
    (r'Qatar Expo 2023 purpose|goals of the event', [
        'The Expo embodies the principles of Qatar National Vision 2030, promoting environmental management and sustainable development.']),
    (r'how big is the event site|size of the venue',
     ['The event site spans an impressive 1.7 million square meters in Al Bidda Park.']),
    (r'partners of the expo|collaborating organizations', [
        'The Expo is in collaboration with the Bureau International Des Expositions (BIE) and the International Association for Horticultural Producers (AIPH).']),
    (r'expected number of visitors|visitor count',
     ['An estimated 3 million visitors are expected to explore the wonders of this remarkable event.']),
    (r'Prime Minister of Qatar|expo leadership',
     ['Qatar\'s Prime Minister HE Sheikh Mohammed bin Abdulrahman bin Jassim Al Thani is supporting the Expo.']),
    (r'how far is the venue from West Bay|distance to West Bay', ['The venue is about 2.5 kilometers from West Bay.']),
    (r'how far is the venue from Doha Port|distance to Doha Port',
     ['The venue is about 3.5 kilometers from Doha Port.']),
    (r'how far is the venue from Hamad International Airport|distance to the airport',
     ['The venue is about 12 kilometers away from Hamad International Airport.']),
    (r'who can attend the expo|visitor eligibility',
     ['The Expo is open to the general public, as well as representatives from the private sector and NGOs.']),
    (r'expo highlights|main attractions', [
        'The Expo highlights include ornamental gardens, panel discussions, live shows, and exquisite art and culinary performances.']),
    (r'Qatar Expo 2023 vision|event mission', [
        'The Expo aims to inspire the international community to adopt innovative solutions for mitigating desertification and promoting a sustainable future.']),
    (r'is there an admission fee|ticket cost',
     ['For detailed information about admission fees and ticket costs, please visit the official website.']),
    (r'how to get tickets|ticket information',
     ['You can find ticket information and purchase options on the official website of Qatar Expo 2023.']),
    # Additional patterns based on user queries about venue
    (r'what is the venue', ['The venue for the Expo 2023 is Al Bidda Park in Doha, Qatar.']),
    (r'where is the venue of the expo', ['The venue of the Expo 2023 is Al Bidda Park in Doha, Qatar.']),
    (r'site of the expo|where is the expo located',
     ['The site of the Expo is located in Al Bidda Park, in the heart of Doha, Qatar.']),
    (r'divided into three areas|zones of the site', [
        'The site is currently divided into three distinctive areas. The Northern portion will host the international event, while the remaining two zones will be used for cultural, entertainment activities, and panel discussions.']),
    (r'international area|international gardens|expo gateway', [
        'The International Area spans 70 hectares and is the focal point for international gardens, exhibitions, and events. The Expo House, designed for the event, includes an open events\' space, a prayer room, a café, a media center, offices, and more.']),
    (r'innovation centre|interactive events|expo sub-themes', [
        'The Innovation Centre, located in the second largest existing building on site, will feature an exhibition space for interactive events. It will embrace the Expo theme and offer an area for children to learn about the sub-themes.']),
    (r'family area|hub for family fun', [
        'The Family Area spans 50 hectares and serves as a hub for family fun, activities, gathering, and outdoor pursuits.']),
    (r'cultural area|traditional activities|historical core', [
        'The Cultural Area spans 50 hectares and is a venue for cultural and traditional activities. It benefits from its proximity to the historical core of Doha and on-site features such as the Old Fort and Old Rocks.']),
    (r'excellent connectivity|metro stations|car-parking facilities', [
        'The site benefits from excellent connectivity, served by two metro stations (Corniche station & Al Bidda station) and five large underground car-parking facilities.']),
    (r'Al Bidda Park|key green public space', [
        'Al Bidda is one of Doha\'s key green public spaces, beautifully designed and overlooking the azure waters of the Arabian Gulf.']),
    (r'pedestrian waterfront promenade|Corniche|Souq Waqif', [
        'The site is moments away from the Corniche and the pedestrianized historical core of Doha - Msheireb and Souq Waqif.']),
    (r'quality landscaping|prestigious international event', [
        'The excellent location, quality landscaping, and ample space for pavilions make Al Bidda a perfect venue to host this prestigious international event.'])

    # Add more patterns for different ways users might ask about the venue
]

chatbot_ = Chat(patterns, reflections)
