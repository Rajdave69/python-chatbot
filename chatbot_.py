try:
    import random
    from nltk.chat.util import Chat, reflections
except ImportError:
    import sys
    import subprocess

    print("Installing nltk...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])

    import random
    from nltk.chat.util import Chat, reflections

patterns = [
    (r'^hello|^hi|^hey', ['Hello! Welcome to Qatar Expo 2023. How can I assist you?']),
    (r'(location|venue|Al Bidda Park|located)', [
        'Al Bidda Park is the scenic venue for the Expo 2023. It\'s located on the west side of Doha city, about 2.5 kilometers from West Bay, 3.5 kilometers from Doha Port, and around 12 kilometers from Hamad International Airport.']),
    (r'(start|starting|begin|beginning|commence)', [
        'The Expo 2023 in Doha will start on October 2, 2023, and conclude on March 28, 2024. It\'s a six-month event showcasing horticulture and sustainable development.']),
    (r'(theme)', [
        'The chosen theme for Doha Expo 2023 is \'Green Desert, Better Environment.\' The event aims to inspire innovative solutions for mitigating desertification and promoting a sustainable future.']),
    (r'(about).*?expect|(?:what|attractions)', [
        'At the Expo 2023, you\'ll experience innovation, sustainability, culture, and entertainment. The event features ornamental gardens, panel discussions, conferences, live shows, art performances, and culinary experiences. It spans an impressive 1.7 million square meters in Al Bidda Park, offering breathtaking views of the Arabian Gulf.']),
    (r'(organizing|organizers)', [
        "Doha Expo 2023 is happening with the support of Qatar's Prime Minister, HE Sheikh Mohammed bin Abdulrahman bin Jassim Al Thani, and it's led by the Ministry of Municipality."]),
    (r'(?:how|get).*?there|(?:how|visit).*?visitor information', [
        'The Expo is conveniently located in the heart of Doha, with easy access to Hamad International Airport, Doha Port, and the Business Centre. It\'s expected to attract international visitors, organizers, representatives from various sectors, and the general public.']),
    (r'more .*expo|website', [
        'For more detailed information about Doha Expo 2023, you can visit the official website: www.dohaexpo2023.gov.qa.']),
    (r'(?:hosting|host country|host|country)', [
        'The International Horticultural Expo 2023 will be hosted by the State of Qatar.']),
    (r'(far).*?West Bay', ['The venue is about 2.5 kilometers from West Bay.']),
    (r'(far).*?Doha Port', ['The venue is about 3.5 kilometers from Doha Port.']),
    (r'(far).*?Hamad International Airport|HIA',
     ['The venue is about 12 kilometers away from Hamad International Airport.']),
    (r'(?:participation|how many|participating|participant) .*?countries', [
        'Participation is confirmed from 57 countries, with more expected to join.']),
    (r'(?:Prime Minister|expo leadership|leadership)', [
        'Qatar\'s Prime Minister HE Sheikh Mohammed bin Abdulrahman bin Jassim Al Thani is supporting and leading the Expo.']),
    (r'(big|size) .*?site|site', [
        'The event site spans an impressive 1.7 million square meters in Al Bidda Park.']),
    (r'(?:partners|collaborating organizations) ', [  # todo done till here
        'The Expo is in collaboration with the Bureau International Des Expositions (BIE) and the International Association for Horticultural Producers (AIPH).']),
    (r'(?:expected number|how many).*?visitors', [
        'An estimated 3 million visitors are expected to explore the wonders of this remarkable event.']),
    (r'Qatar Expo 2023 (?:vision|event mission)', [
        'The Expo aims to inspire the international community to adopt innovative solutions for mitigating desertification and promoting a sustainable future.']),
    (r'partners', [
        'As our partner, you will have access to numerous resources and the opportunity to foster connections with like-minded organisations and institutions. Whether you participate in existing conferences or organise your own related to our theme or sub-themes, the Congress Centre provides a robust platform for knowledge exchange, conversation, and collaboration.']),
    # Additional patterns based on user queries about venue
    (r'(?:what|where) .*?venue', ['The venue for the Expo 2023 is Al Bidda Park in Doha, Qatar.']),
    (r'site', [
        'The site of the Expo is located in Al Bidda Park, in the heart of Doha, Qatar.']),
    (r'(?:divided into|zones) .*?site', [
        'The site is currently divided into three distinctive areas. The Northern portion will host the international event, while the remaining two zones will be used for cultural, entertainment activities, and panel discussions.']),
    (r'international (?:area|gardens)', [
        'The International Area spans 70 hectares and is the focal point for international gardens, exhibitions, and events. The Expo House, designed for the event, includes an open events\' space, a prayer room, a café, a media center, offices, and more.']),
    (r'innovation centre|interactive events', [
        'The Innovation Centre, located in the second largest existing building on site, will feature an exhibition space for interactive events. It will embrace the Expo theme and offer an area for children to learn about the sub-themes.']),
    (r'family (?:area|fun)', [
        'The Family Area spans 50 hectares and serves as a hub for family fun, activities, gathering, and outdoor pursuits.']),
    (r'cultural (?:area|activities)', [
        'The Cultural Area spans 50 hectares and is a venue for cultural and traditional activities. It benefits from its proximity to the historical core of Doha and on-site features such as the Old Fort and Old Rocks.']),
    (r'excellent (?:connectivity|location)', [
        'The site benefits from excellent connectivity, served by two metro stations (Corniche station & Al Bidda station) and five large underground car-parking facilities.']),
    (r'Al Bidda Park|key green public space', [
        'Al Bidda is one of Doha\'s key green public spaces, beautifully designed and overlooking the azure waters of the Arabian Gulf.']),
    (r'pedestrian (?:waterfront promenade|Corniche|Souq Waqif)', [
        'The site is moments away from the Corniche and the pedestrianized historical core of Doha - Msheireb and Souq Waqif.']),
    (r'quality landscaping|prestigious international event', [
        'The excellent location, quality landscaping, and ample space for pavilions make Al Bidda a perfect venue to host this prestigious international event.'])
    # Add more patterns for different ways users might ask about the venue
]


# Create a custom chatbot class which uses pattern.search() instead of pattern.match()
class CustomChat(Chat):
    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.search(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp


chatbot_ = CustomChat(pairs=patterns, reflections=reflections)
