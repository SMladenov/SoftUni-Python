from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish

class NauticalCatchChallengeApp:
    def __init__ (self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []
    
    def dive_into_competition (self, diver_type: str, diver_name: str):
        if diver_type not in ["FreeDiver", "ScubaDiver"]:
            return f"{diver_type} is not allowed in our competition."
        
        diverFound = [diver for diver in self.divers if diver.name == diver_name]

        if diverFound:
            return f"{diver_name} is already a participant."
        
        if diver_type == "FreeDiver":
            newDiver = FreeDiver(diver_name)
            self.divers.append(newDiver)
        elif diver_type == "ScubaDiver":
            newDiver = ScubaDiver(diver_name)
            self.divers.append(newDiver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition (self, fish_type: str, fish_name: str, points: float):
        if fish_type not in ["PredatoryFish", "DeepSeaFish"]:
            return f"{fish_type} is forbidden for chasing in our competition."
        
        fishFound = [fish for fish in self.fish_list if fish.name == fish_name]

        if fishFound:
            return f"{fish_name} is already permitted."
        
        if fish_type == "PredatoryFish":
            newFish = PredatoryFish(fish_name, points)
            self.fish_list.append(newFish)
        elif fish_type == "DeepSeaFish":
            newFish = DeepSeaFish(fish_name, points)
            self.fish_list.append(newFish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish (self, diver_name: str, fish_name: str, is_lucky: bool):
        diverFound = [diver for diver in self.divers if diver.name == diver_name]
        if not diverFound:
            return f"{diver_name} is not registered for the competition."
        
        fishFound = [fish for fish in self.fish_list if fish.name == fish_name]
        if not fishFound:
            return f"The {fish_name} is not allowed to be caught in this competition."
        
        diver = diverFound[0]
        fish = fishFound[0]

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        
        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            elif not is_lucky:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."
        
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

    def health_recovery (self):
        diversWithHealthIssues = [diver for diver in self.divers if diver.has_health_issue == True]
        for diver in diversWithHealthIssues:
            diver.update_health_status()
            diver.renew_oxy()
        
        return f"Divers recovered: {len(diversWithHealthIssues)}"

    def diver_catch_report (self, diver_name: str):
        listToOutput = []
        diverFound = [diver for diver in self.divers if diver.name == diver_name]
        listToOutput.append(f"**{diver_name} Catch Report**")

        for fish in diverFound[0].catch:
            listToOutput.append(fish.fish_details())

        return "\n".join(listToOutput)

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]

        sorted_divers = sorted(
            healthy_divers,
            key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )

        result = ["**Nautical Catch Challenge Statistics**"]
        result.extend(str(diver) for diver in sorted_divers)

        return "\n".join(result)


# nautical_catch_challenge = NauticalCatchChallengeApp()

# # Dive into competition
# print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
# print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
# print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# # Swim into competition
# print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
# print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# # Conduct fishing competitions
# print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# # Check health recovery
# print(nautical_catch_challenge.health_recovery())

# # Conduct fishing competitions
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# # View catch reports
# print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# # View competition statistics
# print(nautical_catch_challenge.competition_statistics())

