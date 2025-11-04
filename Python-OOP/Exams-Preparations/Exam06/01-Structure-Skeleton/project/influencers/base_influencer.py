from abc import ABC, abstractmethod
from project.campaigns.base_campaign import BaseCampaign

class BaseInfluencer (ABC):
    def __init__ (self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: list[BaseCampaign] = []
    
    @property
    def username (self):
        return self.__username
    @username.setter
    def username (self, username: str):
        usernameStrip = username.strip()
        if usernameStrip == "":
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.__username = usernameStrip
    
    @property
    def followers (self):
        return self.__followers
    @followers.setter
    def followers (self, followers: int):
        if followers < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = followers
    
    @property
    def engagement_rate (self):
        return self.__engagement_rate
    @engagement_rate.setter
    def engagement_rate (self, engagement_rate: float):
        if 0.0 <= engagement_rate <= 5.0:
            self.__engagement_rate = engagement_rate
        else:
            raise ValueError("Engagement rate should be between 0 and 5.")
    
    @abstractmethod
    def calculate_payment (self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def reached_followers (self, campaign_type: str):
        pass

    def display_campaigns_participated (self):
        listToOutput = []

        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."
        
        listToOutput.append(f"{self.__class__.__name__} :) {self.username} :) participated in the following campaigns:)")

        for campaign in self.campaigns_participated:
            campaign_type = campaign.__class__.__name__
            reached_followers = self.reached_followers(campaign_type)
            listToOutput.append(f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {reached_followers}")
        
        return "\n".join(listToOutput)