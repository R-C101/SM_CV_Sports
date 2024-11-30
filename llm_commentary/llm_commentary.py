import os
from typing import Dict, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

load_dotenv()

class HockeyCommentaryGenerator:
    def __init__(self, g_api_key: str = 'Your API Key'):
        """
        Initialize the Hockey Commentary Generator with Google Gemini
        
        :param api_key: Optional Google AI API key (defaults to environment variable)
        """
        if not g_api_key:
            g_api_key = os.getenv('GOOGLE_API_KEY')
        
        self.llm = ChatGoogleGenerativeAI(
            google_api_key=g_api_key, 
            model='gemini-pro',
            temperature=0.7, 
            max_tokens=500
        )
        
        self.commentary_prompt = PromptTemplate(
            input_variables=[
                'players', 
                'type', 
                'period', 
                'time_remaining', 
                'location', 
                'home_team', 
                'away_team', 
                'score', 
                'playoff_game', 
                'team_histories'
            ],
            template="""
            You are a passionate, dynamic hockey play-by-play and color commentator. 
            Provide an exciting and unique commentary for the following scenario.

            Game Context:
            - Home Team: {home_team}
            - Away Team: {away_team}
            - Current Score: {score}
            - Playoff Game: {playoff_game}

            Event Details:
            - Type: {type}
            - Period: {period}
            - Time Remaining: {time_remaining}
            - Location: {location}

            Players Involved: {players}

            Team Historical Context:
            {team_histories}

            Generate a compelling 3-4 sentence commentary that:
            1. Captures the moment's intensity
            2. Incorporates player and team historical insights
            3. Uses vivid, professional sports terminology
            4. Provides strategic narrative
            """
        )
        
        self.commentary_chain = LLMChain(
            llm=self.llm, 
            prompt=self.commentary_prompt
        )
    
    def generate_commentary(
        self, 
        players: List[str], 
        event_details: Dict[str, str], 
        game_context: Dict[str, str], 
        team_histories: str
    ) -> str:
        """
        Generate hockey commentary based on provided metadata
        
        :param players: List of player names involved
        :param event_details: Dictionary of event specifics
        :param game_context: Dictionary of game-level context
        :param team_histories: Team historical information
        :return: Generated commentary text
        """
        try:
            # Combine all inputs into a single dictionary
            input_dict = {
                'players': ", ".join(players),
                'type': event_details['type'],
                'period': event_details['period'],
                'time_remaining': event_details['time_remaining'],
                'location': event_details['location'],
                'home_team': game_context['home_team'],
                'away_team': game_context['away_team'],
                'score': game_context['score'],
                'playoff_game': str(game_context['playoff_game']),
                'team_histories': team_histories
            }
            
            # Generate commentary
            commentary = self.commentary_chain.run(**input_dict)
            client = ElevenLabs(
            api_key= 'Your API_KEY', # Defaults to ELEVEN_API_KEY
            )

            audio = client.generate(
            text=commentary,
            voice="Daniel",
            model="eleven_multilingual_v2"
            )
            save(audio, "output_commentary/output.mp3")
            print('commentary saved inside output_commentary')
            return commentary
        except Exception as e:
            return f"Commentary generation error: {str(e)}"

