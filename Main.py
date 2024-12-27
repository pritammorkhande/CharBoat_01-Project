import nltk
from nltk.chat.util import Chat, reflections
import requests
from googleapiclient.discovery import build

# Define conversational patterns and responses
pairs = [
    [
        r"(hi|hello|hey|hola|howdy)(.*)",
        ["Hello! How can I assist you today?", "Hi there! How can I help?"]
    ],
    [
        r"(what is your name|who are you)(.*)",
        ["I am a chatbot created using Python and NLP techniques!", "My name is NLPBot. How can I assist you?"]
    ],
    [
        r"(how are you|how are you doing)(.*)",
        ["I'm just a program, so I don't have feelings, but thank you for asking! How can I help you?", "I'm doing great! What's on your mind?"]
    ],
    [
        r"(.*) weather(.*)",
        ["I'm not equipped to check the weather, but you can try asking a weather app or website!"]
    ],
    [
        r"(tell me a joke|make me laugh)(.*)",
        ["Why don't programmers like nature? It has too many bugs!", "How many programmers does it take to change a light bulb? None, that's a hardware issue!"]
    ],
    [
        r"(.*) current affairs(.*)",
        ["Sure, let me fetch the latest news for you.", "Let me provide you with the most recent current affairs."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "Bye! Feel free to return if you need more help."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase?", "Can you elaborate on that?"]
    ]
]

# Enhanced reflections dictionary to handle more user input cases
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Function to fetch current affairs using a news API
def get_current_affairs():
    print("Fetching the latest news...")
    try:
        # Replace 'your_api_key' with a valid API key
        api_key = "a6fe90c64194488eb11964deebb7d7cd"  # Use your actual NewsAPI key
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        news_data = response.json()
        articles = news_data.get("articles", [])
        if articles:
            print("Here are the latest news headlines:")
            for article in articles[:5]:
                print(f"- {article['title']}")
        else:
            print("No news available at the moment.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching news: {e}")

# Function to perform a Google search using Custom Search API
def google_search(query):
    print(f"Searching for {query} on Google...")
    try:
        # Replace 'your_api_key' and 'your_cx' with your actual API key and Custom Search Engine ID
        api_key = "AIzaSyAQikVRFkvidq8iIIKC-lwi-PgN6vWKIeA"
        cx = "4590854a6cd8a4627"
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cx).execute()
        if 'items' in res:
            for item in res['items'][:5]:  # Show top 5 results
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}\n")
        else:
            print("No results found.")
    except Exception as e:
        print(f"An error occurred while searching: {e}")

# Function to enhance user experience
def start_chatbot():
    print("Welcome to the Chatbot Project!")
    print("I am your chatbot, here to assist you with various queries.")
    print("Type 'quit' to exit the conversation at any time.")
    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("> ").lower()
        if "current affairs" in user_input:
            get_current_affairs()
        elif "google" in user_input:
            query = input("What would you like to search for on Google? ")
            google_search(query)
        elif user_input == "quit":
            print("Thank you for using the chatbot. Goodbye!")
            break
        else:
            print(chatbot.respond(user_input))

# Start the chatbot program
if __name__ == "__main__":
    start_chatbot()
