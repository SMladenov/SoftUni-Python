from abc import ABC, abstractmethod

class BaseCampaign (ABC):
    list_used_ids = []

    def __init__ (self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers: list = []
    
    @property
    def campaign_id (self):
        return self.__campaign_id
    @campaign_id.setter
    def campaign_id (self, campaign_id: int):
        if campaign_id < 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        
        if campaign_id in BaseCampaign.list_used_ids:
            raise ValueError(f"Campaign with ID {campaign_id} already exists. Campaign IDs must be unique.")
        
        self.__campaign_id = campaign_id
        BaseCampaign.list_used_ids.append(campaign_id)
    
    @abstractmethod
    def check_eligibility (self, engagement_rate: float):
        pass


        