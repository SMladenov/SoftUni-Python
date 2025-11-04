from project.campaigns.base_campaign import BaseCampaign

class HighBudgetCampaign (BaseCampaign):
    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, 5000.0, required_engagement)
    
    def check_eligibility(self, engagement_rate):
        currentRequiredRate = self.required_engagement * 1.20
        if engagement_rate >= currentRequiredRate:
            return True
        return False
    
    