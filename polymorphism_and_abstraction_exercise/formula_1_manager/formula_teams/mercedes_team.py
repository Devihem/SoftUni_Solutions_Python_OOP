from oop.polymorphism_and_abstraction_exercise.formula_1_manager.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    expenses_per_race = -200_000
    sponsors_reward = {'Petronas': {1: 1_000_000,
                                    3: 500_000},
                       'TeamViewer': {5: 100_000,
                                      7: 50_000}}

    def calculate_revenue_after_race(self, race_pos: int):
        return self.revenue_calculator(race_pos)
