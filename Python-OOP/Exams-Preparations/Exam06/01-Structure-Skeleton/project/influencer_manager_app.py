from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer

class InfluencerManagerApp ():
    def __init__ (self):
        self.influencers: list[BaseInfluencer] = []
        self.campaigns: list[BaseCampaign] = []
    
    def register_influencer (self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in ["PremiumInfluencer", "StandardInfluencer"]:
            return f"{influencer_type} is not an allowed influencer type."
        
        if [influencer for influencer in self.influencers if influencer.username == username]:
            return f"{username} is already registered."
        
        if influencer_type == "PremiumInfluencer":
            newInf = PremiumInfluencer(username, followers, engagement_rate)
            self.influencers.append(newInf)
        elif influencer_type == "StandardInfluencer":
            newInf = StandardInfluencer(username, followers, engagement_rate)
            self.influencers.append(newInf)
        return f"{username} is successfully registered as a {influencer_type}."
    
    def create_campaign (self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in ["HighBudgetCampaign", "LowBudgetCampaign"]:
            return f"{campaign_type} is not a valid campaign type."
        
        if [campaign for campaign in self.campaigns if campaign.campaign_id == campaign_id]:
            return f"Campaign ID {campaign_id} has already been created."
        
        if campaign_type == "HighBudgetCampaign":
            newCamp = HighBudgetCampaign(campaign_id, brand, required_engagement)
            self.campaigns.append(newCamp)
        elif campaign_type == "LowBudgetCampaign":
            newCamp = LowBudgetCampaign(campaign_id, brand, required_engagement)
            self.campaigns.append(newCamp)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."
    
    def participate_in_campaign (self, influencer_username: str, campaign_id: int):
        influencerFound = [inf for inf in self.influencers if inf.username == influencer_username]
        campFound = [camp for camp in self.campaigns if camp.campaign_id == campaign_id]
        
        if not influencerFound:
            return f"Influencer '{influencer_username}' not found."
        
        if not campFound:
            return f"Campaign with ID {campaign_id} not found."
        
        if not campFound[0].check_eligibility(influencerFound[0].engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
        
        payment = influencerFound[0].calculate_payment(campFound[0])
        if payment > 0.0:
            campFound[0].approved_influencers.append(influencerFound[0])
            campFound[0].budget -= payment
            influencerFound[0].campaigns_participated.append(campFound[0])
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."
    
    def calculate_total_reached_followers (self):
        reached_followers_per_campaign = {}

        for campaign in self.campaigns:
            total_followers = sum(
                influencer.reached_followers(campaign.__class__.__name__)
                for influencer in campaign.approved_influencers
            )
            if total_followers > 0:
                reached_followers_per_campaign[campaign] = total_followers

        return reached_followers_per_campaign
    
    def influencer_campaign_report(self, username: str):
        influencerFound = [inf for inf in self.influencers if inf.username == username]
        if not influencerFound:
            return f"{username} has not participated in any campaigns."
        return influencerFound[0].display_campaigns_participated()

    def campaign_statistics(self):
        if not self.campaigns:
            return "$$ Campaign Statistics $$\nNo campaigns available."
        
        listToOutput = []

        reached_followers_per_campaign = self.calculate_total_reached_followers()

        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget),)
        listToOutput.append("$$ Campaign Statistics $$")

        for campaign in sorted_campaigns:
            total_reached_followers = reached_followers_per_campaign.get(campaign, 0)
            listToOutput.append(f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
            f"Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}")
        return "\n".join(listToOutput)

# manager = InfluencerManagerApp()

# # Register influencers
# print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 50000, 4.2))
# print(manager.register_influencer("StandardInfluencer", "JaneSmith", 10000, 3.5))
# print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 80000, 4.2))
# print(manager.register_influencer("InvalidInfluencer", "JohnDoe", 50000, 4.2))
# print(manager.register_influencer("StandardInfluencer", "AliceJohnson", 20000, 3.8))
# print(manager.register_influencer("PremiumInfluencer", "OliviaBennett", 80000, 4.5))
# print(manager.register_influencer("PremiumInfluencer", "DanielRodriguez", 90000, 4.8))
# print(manager.register_influencer("PremiumInfluencer", "EmilyTurner", 1000000, 5.0))

# # Create campaigns
# print(manager.create_campaign("LowBudgetCampaign", 1, "TechGurus", 4.0))
# print(manager.create_campaign("HighBudgetCampaign", 2, "FashionTrendz", 3.0))
# print(manager.create_campaign("LowBudgetCampaign", 1, "FashionTrendz", 3.0))
# print(manager.create_campaign("LowBudgetCampaign", 3, "QuantumFusion", 3.0))
# print(manager.create_campaign("InvalidCampaign", 4, "FoodieDelights", 2.5))

# # Participate in campaigns
# print(manager.participate_in_campaign("JohnDoe", 1))
# print(manager.participate_in_campaign("JaneSmith", 2))
# print(manager.participate_in_campaign("AliceJohnson", 2))
# print(manager.participate_in_campaign("AliceJohnson", 1))
# print(manager.participate_in_campaign("NonExistentInfluencer", 1))
# print(manager.participate_in_campaign("AliceJohnson", 3))
# print(manager.participate_in_campaign("JohnDoe", 2))
# print(manager.participate_in_campaign("JaneSmith", 4))
# print(manager.participate_in_campaign("JaneSmith", 1))
# print(manager.participate_in_campaign("OliviaBennett", 3))
# print(manager.participate_in_campaign("DanielRodriguez", 3))
# print(manager.participate_in_campaign("EmilyTurner", 3))

# # Print influencer campaign reports and campaign statistics
# print(manager.influencer_campaign_report("JohnDoe"))
# print(manager.influencer_campaign_report("JaneSmith"))
# print(manager.campaign_statistics())