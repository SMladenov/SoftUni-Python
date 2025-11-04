from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign

class PremiumInfluencer (BaseInfluencer):
    def __init__ (self, username, followers, engagement_rate):
        super().__init__ (username, followers, engagement_rate)
    
    def calculate_payment(self, campaign: BaseCampaign):
        currentPayment = campaign.budget * 0.85
        return currentPayment

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            currentReachedFollowers = (self.followers * self.engagement_rate) * 1.5
            return int(currentReachedFollowers)
        
        if campaign_type == "LowBudgetCampaign":
            currentReachedFollowers = (self.followers * self.engagement_rate) * 0.8
            return int(currentReachedFollowers)