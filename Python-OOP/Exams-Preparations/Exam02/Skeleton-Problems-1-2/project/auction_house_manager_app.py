from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector

class AuctionHouseManagerApp():
    def __init__ (self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact (self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type == "RenaissanceArtifact" or artifact_type == "ContemporaryArtifact":
            artifactNameAlreadyPresent = [artifact for artifact in self.artifacts if artifact.name == artifact_name]
            if artifactNameAlreadyPresent:
                raise ValueError("{artifact_name} has been already registered!")
            else:
                #Proceed to adding the artifact
                if artifact_type == "RenaissanceArtifact":
                    newArt = RenaissanceArtifact(artifact_name, artifact_price, artifact_space)
                    self.artifacts.append(newArt)
                elif artifact_type == "ContemporaryArtifact":
                    newArt2 = ContemporaryArtifact(artifact_name, artifact_price, artifact_space)
                    self.artifacts.append(newArt2)
                return f"{artifact_name} is successfully added to the auction as {artifact_type}."
        else:
            raise ValueError ("Unknown artifact type!")
        
    def register_collector (self, collector_type: str, collector_name: str):
        if collector_type == "Museum" or collector_type == "PrivateCollector":
            collectorPresent = [collector for collector in self.collectors if collector.name == collector_name]
            if collectorPresent:
                raise ValueError("{collector_name} has been already registered!")
            else:
                #Proceed to adding the collector
                if collector_type == "Museum":
                    newMuseum = Museum(collector_name)
                    self.collectors.append(newMuseum)
                elif collector_type == "PrivateCollector":
                    newPrivateCollector = PrivateCollector(collector_name)
                    self.collectors.append(newPrivateCollector)
                return f"{collector_name} is successfully registered as a {collector_type}."
        else:
            raise ValueError("Unknown collector type!")
    
    def perform_purchase (self, collector_name: str, artifact_name: str):
        collectorPresent = [collector for collector in self.collectors if collector.name == collector_name]
        artifactPresent = [artifact for artifact in self.artifacts if artifact.name == artifact_name]

        if not collectorPresent:
            raise ValueError("Collector {collector_name} is not registered to the auction!")
        if not artifactPresent:
            raise ValueError("Artifact {artifact_name} is not registered to the auction!")
        
        if collectorPresent[0].can_purchase(artifactPresent[0].price, artifactPresent[0].space_required):
            #Purchase is established
            self.artifacts.remove(artifactPresent[0])
            collectorPresent[0].purchased_artifacts.append(artifactPresent[0])
            collectorPresent[0].available_money -= artifactPresent[0].price
            collectorPresent[0].available_space -= artifactPresent[0].space_required
            return f"{collector_name} purchased {artifact_name} for a price of {artifactPresent[0].price}."

        else:
            return f"Purchase is impossible."

    def remove_artifact (self, artifact_name: str):
        artifactPresent = [artifact for artifact in self.artifacts if artifact.name == artifact_name]

        if not artifactPresent:
            return f"No such artifact."
        else:
            self.artifacts.remove(artifactPresent[0])
            return f"{artifactPresent[0].artifact_information()}"

    def fundraising_campaigns (self, max_money: float):
        totalIncreased = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                totalIncreased += 1
        return f"{totalIncreased} collector/s increased their available money."

    def get_auction_report (self):
        listToOutput = []
        listToOutput.append("**Auction statistics**")
        total_sold = sum(len(collector.purchased_artifacts) for collector in self.collectors)
        available_artifacts = len(self.artifacts)

        listToOutput.append(f"Total number of sold artifacts: {total_sold}")
        listToOutput.append(f"Available artifacts for sale: {available_artifacts}")
        listToOutput.append("***")

        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))

        for collector in sorted_collectors:
            
            artifact_names = [artifact.name for artifact in collector.purchased_artifacts]
            if artifact_names:
                artifact_names.sort()
                artifact_names.reverse()    
                listToOutput.append(f"Collector name: {collector.name}; Money available: {collector.available_money}; Space available: {collector.available_space}; Artifacts: {', '.join(artifact_names)}")
            else:
                 listToOutput.append(f"Collector name: {collector.name}; Money available: {collector.available_money}; Space available: {collector.available_space}; Artifacts: none")

        return '\n'.join(listToOutput)
            
# # Create an instance of AuctionHouseManagerApp
# manager = AuctionHouseManagerApp()
# # Register artifacts
# print(manager.register_artifact("RenaissanceArtifact", "Kohinoor", 5000.0, 10))
# print(manager.register_artifact("RenaissanceArtifact", "Zelda", 5000.0, 10))
# print(manager.register_artifact("RenaissanceArtifact", "Mona Lisa", 10000.0, 100))
# print(manager.register_artifact("ContemporaryArtifact", "The Scream", 2000.0, 1000))
# print(manager.register_artifact("ContemporaryArtifact", "Untitled", 32000.0, 90))
# print()
# # Register collectors
# print(manager.register_collector("PrivateCollector", "Josh Smith"))
# print(manager.register_collector("Museum", "Louvre"))
# print(manager.register_collector("Museum", "Hermitage"))
# print()
# # Perform purchases
# print(manager.perform_purchase("Josh Smith", "Mona Lisa"))
# print(manager.perform_purchase("Louvre", "Kohinoor"))
# print(manager.perform_purchase("Josh Smith", "Zelda"))
# print(manager.perform_purchase("Josh Smith", "The Scream"))
# print(manager.perform_purchase("Josh Smith", "Untitled"))
# print()
# # Remove artifact
# print(manager.remove_artifact("The Scream"))
# print(manager.remove_artifact("Nonexistent"))
# print()
# # Start fund-raising campaigns
# print(manager.fundraising_campaigns(10000.0))
# print()
# # Get auction report
# print(manager.get_auction_report())
# print()
# # Remove artifact
# print(manager.remove_artifact("Untitled"))

