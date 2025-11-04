from project.climbers.base_climber import BaseClimber
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.base_peak import BasePeak
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak

class SummitQuestManagerApp ():
    def __init__ (self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []
    
    def register_climber (self, climber_type: str, climber_name: str):
        if not climber_type in ["ArcticClimber", "SummitClimber"]:
            return f"{climber_type} doesn't exist in our register."
        
        climberFound = [climber for climber in self.climbers if climber.name == climber_name]

        if climberFound:
            return f"{climber_name} has been already registered."
        
        if climber_type == "ArcticClimber":
            newClimber = ArcticClimber(climber_name)
            self.climbers.append(newClimber)
        elif climber_type == "SummitClimber":
            newClimber = SummitClimber(climber_name)
            self.climbers.append(newClimber)
        return f"{climber_name} is successfully registered as a {climber_type}."
    
    def peak_wish_list (self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in ["ArcticPeak", "SummitPeak"]:
            return f"{peak_type} is an unknown type of peak."
        
        if peak_type == "ArcticPeak":
            newPeak = ArcticPeak(peak_name, peak_elevation)
            self.peaks.append(newPeak)
        elif peak_type == "SummitPeak":
            newPeak = SummitPeak(peak_name, peak_elevation)
            self.peaks.append(newPeak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."
    
    def check_gear (self, climber_name: str, peak_name: str, gear: list[str]):
        peakFound = [peak for peak in self.peaks if peak.name == peak_name]
        climberFound = [climber for climber in self.climbers if climber.name == climber_name]

        neededGear = peakFound[0].get_recommended_gear()
        for item in gear:
            if item in neededGear:
                neededGear.remove(item)
        
        if not neededGear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climberFound[0].is_prepared = False
            neededGear.sort()
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(neededGear)}."
    
    def perform_climbing (self, climber_name: str, peak_name: str):
        climberFound = [climber for climber in self.climbers if climber.name == climber_name]
        if not climberFound:
            return f"Climber {climber_name} is not registered yet."
        
        peakFound = [peak for peak in self.peaks if peak.name == peak_name]
        if not peakFound:
            return f"Peak {peak_name} is not part of the wish list."
        
        if not climberFound[0].is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        
        if not climberFound[0].can_climb():
            climberFound[0].rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
        
        climberFound[0].climb(peakFound[0])
        #climberFound[0].conquered_peaks.append(peakFound[0].name)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peakFound[0].difficulty_level}."
    
    def get_statistics(self):
        listToOutput = []

        successful_climbers = [climber for climber in self.climbers if climber.conquered_peaks]
        
        successful_climbers.sort(key=lambda c: (-len(c.conquered_peaks), c.name))
        
        totalConqueredPeaks = []
        for climber in successful_climbers:
            for peak in climber.conquered_peaks:
                if peak.name not in totalConqueredPeaks:
                    totalConqueredPeaks.append(peak.name)

        listToOutput.append(f"Total climbed peaks: {len(totalConqueredPeaks)}\n{', '.join(totalConqueredPeaks)}")
        listToOutput.append("**Climber's statistics:**")

        for climber in successful_climbers:
            conquered_peak_names = sorted(peak.name for peak in climber.conquered_peaks)
            climber_info = f"{climber.__class__.__name__}: /// Climber name: {climber.name} * Left strength: {climber.strength} * Conquered peaks: {', '.join(conquered_peak_names)} ///"
            listToOutput.append(climber_info)
        
        return "\n".join(listToOutput)

# Create an instance of SummitQuestManagerApp
climbing_app = SummitQuestManagerApp()

# Register climbers
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber", "Dave"))
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

# Perform climbing
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))

# Get statistics
print(climbing_app.get_statistics())

